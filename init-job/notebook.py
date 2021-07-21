# -*- coding: utf-8 -*-
"""Kubeflow notebook server utility functions."""
import json
import os
import random
import re
import tarfile
import time
import uuid
import warnings
from tempfile import TemporaryFile

from ast import literal_eval
from kubernetes import client
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream

from kube_config import load_kube_config

KF_PIPELINES_NAMESPACE = os.getenv("KF_PIPELINES_NAMESPACE", "anonymous")
NOTEBOOK_NAME = "server"
NOTEBOOK_NAMESPACE = "anonymous"
NOTEBOOK_POD_NAME = "server-0"
NOTEBOOK_CONAINER_NAME = "server"


class ApiClientForJsonPatch(client.ApiClient):
    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, async_req=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True, _request_timeout=None):
        header_params["Content-Type"] = self.select_header_content_type(["application/json-patch+json"])
        return super().call_api(resource_path, method, path_params, query_params, header_params, body,
                                post_params, files, response_type, auth_settings, async_req, _return_http_data_only,
                                collection_formats, _preload_content, _request_timeout)


def create_persistent_volume_claim(name):
    """
    Creates a persistent volume claim.

    Parameters
    ----------
    name : str
    """
    print(f"Creating volume {name}...", flush=True)
    load_kube_config()

    api_instance = client.CoreV1Api()

    try:
        api_instance.read_namespaced_persistent_volume_claim(
            name=name,
            namespace=NOTEBOOK_NAMESPACE,
        )
        warnings.warn(f"Volume {name} already exists...")
        return
    except ApiException:
        pass

    try:
        body = {
            "metadata": {
                "name": name,
            },
            "spec": {
                "accessModes": [
                    "ReadWriteOnce",
                ],
                "resources": {
                    "requests": {
                        "storage": "10Gi",
                    },
                }
            },
        }
        api_instance.create_namespaced_persistent_volume_claim(
            namespace=NOTEBOOK_NAMESPACE,
            body=body,
        )
    except ApiException as e:
        body = literal_eval(e.body)
        message = body["message"]
        raise Exception(f"Error while trying to patch notebook server: {message}")


def create_config_map(task_id, experiment_notebook_content):
    """
    Create a ConfigMap with the notebook of the given task.

    Parameters
    ----------
    task_id : str
    experiment_notebook_content : str
    """
    config_map_name = f"configmap-{task_id}"

    load_kube_config()
    v1 = client.CoreV1Api()

    body = {
        "metadata": {
            "name": config_map_name,
        },
        "data": {
            "Experiment.ipynb": experiment_notebook_content
        }
    }

    v1.create_namespaced_config_map(
        namespace=KF_PIPELINES_NAMESPACE,
        body=body,
    )

    warnings.warn(f"ConfigMap of task {task_id} created!")


def patch_notebook_server(volume_mounts):
    """
    Adds a list of volume mounts to the notebook server.

    Parameters
    ----------
    volume_mounts : list
    """
    print("Adding volumes to notebook server...", flush=True)
    load_kube_config()

    api_instance = client.CoreV1Api()
    custom_api = client.CustomObjectsApi(api_client=ApiClientForJsonPatch())

    try:
        body = custom_api.get_namespaced_custom_object(
            group="kubeflow.org",
            version="v1",
            namespace=NOTEBOOK_NAMESPACE,
            plural="notebooks",
            name=NOTEBOOK_NAME,
        )
        # filters volume mounts that were already added
        volume_mounts = [m for m in volume_mounts if not any(v for v in body["spec"]["template"]["spec"]["volumes"] if m["name"] == v["name"])]
    except ApiException as e:
        body = literal_eval(e.body)
        message = body["message"]
        raise Exception(f"Error while trying to patch notebook server: {message}")

    body = []
    for v in volume_mounts:
        body.extend([
            {
                "op": "add",
                "path": "/spec/template/spec/volumes/-",
                "value": {
                    "name": v["name"],
                    "persistentVolumeClaim": {
                        "claimName": v["name"],
                    },
                },
            },
            {
                "op": "add",
                "path": "/spec/template/spec/containers/0/volumeMounts/-",
                "value": {
                    "mountPath": v["mount_path"],
                    "name": v["name"],
                },
            },
        ])

    if len(body) > 0:
        try:
            custom_api.patch_namespaced_custom_object(
                group="kubeflow.org",
                version="v1",
                namespace=NOTEBOOK_NAMESPACE,
                plural="notebooks",
                name=NOTEBOOK_NAME,
                body=body,
                _request_timeout=5,
            )
        except ApiException as e:
            body = literal_eval(e.body)
            message = body["message"]
            raise Exception(f"Error while trying to patch notebook server: {message}")

    # Wait for the pod to be ready and have all containers running
    while True:
        try:
            pod = api_instance.read_namespaced_pod(
                name=NOTEBOOK_POD_NAME,
                namespace=NOTEBOOK_NAMESPACE,
                _request_timeout=5,
            )

            if pod.status.phase == "Running" \
               and all([c.state.running for c in pod.status.container_statuses]):
                print("Mounted volumes in notebook server!", flush=True)
                break
        except ApiException:
            pass
        finally:
            warnings.warn("Waiting for notebook server to be ready...")
            time.sleep(5)


def copy_files_inside_pod(local_path, destination_path, task_name):
    """
    Copies local files to a pod in notebook server.
    Based on this example:
    https://github.com/prafull01/Kubernetes-Utilities/blob/master/kubectl_cp_as_python_client.py

    Parameters
    ----------
    local_path : str
    destination_path : str
    task_name : task_name
    """
    print(f"Copying {local_path} to {destination_path}...", flush=True)
    load_kube_config()
    api_instance = client.CoreV1Api()

    # The following command extracts the contents of STDIN to /home/jovyan/tasks
    exec_command = ["tar", "xvf", "-", "-C", "/home/jovyan/tasks"]

    container_stream = stream(
        api_instance.connect_get_namespaced_pod_exec,
        name=NOTEBOOK_POD_NAME,
        namespace=NOTEBOOK_NAMESPACE,
        command=exec_command,
        container=NOTEBOOK_CONAINER_NAME,
        stderr=True,
        stdin=True,
        stdout=True,
        tty=False,
        _preload_content=False,
    )

    with TemporaryFile() as tar_buffer:
        # Prepares an uncompressed tarfile that will be written to STDIN
        with tarfile.open(fileobj=tar_buffer, mode="w") as tar:

            for root, dirs, files in os.walk(local_path):
                for filename in files:
                    # Local filepath
                    filepath = os.path.join(root, filename)
                    # Filepath inside pod
                    pod_root = root.lstrip(local_path)
                    destination_path = os.path.join(task_name, pod_root, filename)

                    tar.add(filepath, arcname=destination_path)

        # Rewinds to beggining of tarfile
        tar_buffer.seek(0)

        # WARNING:
        # Attempts to write the entire tarfile caused connection errors for large files
        # The loop below reads/writes small chunks to prevent these errors
        data = tar_buffer.read(1000000)
        while container_stream.is_open():
            container_stream.update(timeout=10)
            if container_stream.peek_stdout():
                print("STDOUT: %s" % container_stream.read_stdout(), flush=True)
            if container_stream.peek_stderr():
                print("STDERR: %s" % container_stream.read_stderr(), flush=True)
            if data:
                container_stream.write_stdin(data)
                data = tar_buffer.read(1000000)
            else:
                break
        container_stream.close()

    print(f"Copied {local_path} to {destination_path}!", flush=True)


def set_notebook_metadata(notebook_path, task_id, experiment_id, operator_id):
    """
    Sets metadata values in notebook file.

    Parameters
    ----------
    notebook_path : str
    task_id : str
    experiment_id : str
    operator_id : str
    """
    print(f"Setting metadata in {notebook_path}...", flush=True)
    load_kube_config()
    api_instance = client.CoreV1Api()

    # The following command sets task_id in the metadata of a notebook
    python_script = (
        f"import json; "
        f"f = open('/home/jovyan/tasks/{notebook_path}'); "
        f"n = json.load(f); "
        f"n['metadata']['task_id'] = '{task_id}'; "
        f"n['metadata']['experiment_id'] = '{experiment_id}'; "
        f"n['metadata']['operator_id'] = '{operator_id}'; "
        f"f.close(); "
        f"f = open('/home/jovyan/tasks/{notebook_path}', 'w'); "
        f"json.dump(n, f, indent=1); "
        f"f.close()"
    )
    exec_command = [
        "python",
        "-c",
        python_script,
    ]

    container_stream = stream(
        api_instance.connect_get_namespaced_pod_exec,
        name=NOTEBOOK_POD_NAME,
        namespace=NOTEBOOK_NAMESPACE,
        command=exec_command,
        container=NOTEBOOK_CONAINER_NAME,
        stderr=True,
        stdin=False,
        stdout=True,
        tty=False,
        _preload_content=False,
    )

    while container_stream.is_open():
        container_stream.update(timeout=10)
        if container_stream.peek_stdout():
            warnings.warn("STDOUT: %s" % container_stream.read_stdout())
        if container_stream.peek_stderr():
            warnings.warn("STDERR: %s" % container_stream.read_stderr())
    container_stream.close()

    print(f"Set metadata in {notebook_path}!", flush=True)


def uuid_alpha():
    """
    Generates an uuid that always starts with an alpha char.

    Returns
    -------
    str
    """
    uuid_ = str(uuid.uuid4())
    if not uuid_[0].isalpha():
        c = random.choice(["a", "b", "c", "d", "e", "f"])
        uuid_ = f"{c}{uuid_[1:]}"
    return uuid_


def parse_parameters(notebook_path):
    """
    Parses and returns the parameters declared in a notebook.

    Parameters
    ----------
    notebook_path : str

    Returns
    -------
    list:
        A list of parameters (name, default, type, label, description).
    """
    if not os.path.exists(notebook_path):
        return []

    with open(notebook_path) as f:
        notebook = json.load(f)

    parameters = []
    cells = notebook.get("cells", [])
    for cell in cells:
        cell_type = cell["cell_type"]
        tags = cell["metadata"].get("tags", [])
        if cell_type == "code" and "parameters" in tags:
            source = cell["source"]

            parameters.extend(read_parameters_from_source(source))

    return parameters


def read_parameters_from_source(source):
    """
    Lists the parameters declared in source code.

    Parameters
    ----------
    source : list
        Source code lines.

    Returns
    -------
    list:
        A list of parameters (name, default, type, label, description).
    """
    parameters = []
    # Regex to capture a parameter declaration
    # Inspired by Google Colaboratory Forms
    # Example of a parameter declaration:
    # name = "value" #@param ["1st option", "2nd option"] {type:"string", label:"Foo Bar", description:"Foo Bar"}
    pattern = re.compile(r"^(\w+)\s*=\s*(.+)\s*#@param(?:(\s+\[.*\]))?(\s+\{.*\})")

    for line in source:
        match = pattern.search(line)
        if match:
            try:
                name = match.group(1)
                default = match.group(2)
                options = match.group(3)
                metadata = match.group(4)

                parameter = {"name": name}

                # For these comparisons below we need to make sure there are no whitespaces.
                default_str_no_whitespace = default.strip() if default else None

                if default_str_no_whitespace and default_str_no_whitespace != "None":
                    if default_str_no_whitespace in ["True", "False"]:
                        default = default_str_no_whitespace.lower()
                    parameter["default"] = json.loads(default)

                if options:
                    parameter["options"] = json.loads(options)

                # adds quotes to metadata keys
                metadata = re.sub(r"(\w+):", r'"\1":', metadata)
                parameter.update(json.loads(metadata))

                parameters.append(parameter)
            except json.JSONDecodeError:
                pass

    return parameters
