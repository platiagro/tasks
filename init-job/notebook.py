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


def create_persistent_volume_claim(name, mount_path):
    """
    Creates a persistent volume claim and mounts it to the notebook server.

    Parameters
    ----------
    name : str
    mount_path : str
    """
    print(f"Creating volume vol-{name}...", flush=True)
    load_kube_config()

    api_instance = client.CoreV1Api()
    custom_api = client.CustomObjectsApi(api_client=ApiClientForJsonPatch())

    try:
        body = {
            "metadata": {
                "name": f"vol-{name}",
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

        print(f"Mounting volume vol-{name} in notebook server...", flush=True)
        body = [
            {
                "op": "add",
                "path": "/spec/template/spec/volumes/-",
                "value": {
                    "name": name,
                    "persistentVolumeClaim": {
                        "claimName": f"vol-{name}",
                    },
                },
            },
            {
                "op": "add",
                "path": "/spec/template/spec/containers/0/volumeMounts/-",
                "value": {
                    "mountPath": mount_path,
                    "name": name,
                },
            },
        ]

        custom_api.patch_namespaced_custom_object(
            group="kubeflow.org",
            version="v1",
            namespace=NOTEBOOK_NAMESPACE,
            plural="notebooks",
            name=NOTEBOOK_NAME,
            body=body,
            _request_timeout=5,
        )

        # Wait for the pod to be ready and have all containers running
        while True:
            try:
                pod = api_instance.read_namespaced_pod(
                    name=NOTEBOOK_POD_NAME,
                    namespace=NOTEBOOK_NAMESPACE,
                    _request_timeout=5,
                )

                if pod.status.phase == "Running" \
                    and all([c.state.running for c in pod.status.container_statuses]) \
                    and any([v for v in pod.spec.volumes if v.name == f"{name}"]):
                    print(f"Mounted volume vol-{name} in notebook server!", flush=True)
                    break
            except ApiException:
                pass
            finally:
                warnings.warn(f"Waiting for notebook server to be ready...")
                time.sleep(5)

    except ApiException as e:
        body = literal_eval(e.body)
        message = body["message"]
        raise Exception(f"Error while trying to patch notebook server: {message}")


def copy_file_inside_pod(filepath, destination_path):
    """
    Copies a local file to a pod in notebook server.
    Based on this example:
    https://github.com/prafull01/Kubernetes-Utilities/blob/master/kubectl_cp_as_python_client.py

    Parameters
    ----------
    filepath : str
    destination_path : str
    """
    print(f"Copying {filepath} to {destination_path}...", flush=True)
    load_kube_config()
    api_instance = client.CoreV1Api()

    # The following command extracts the contents of STDIN to /home/jovyan/
    exec_command = ["tar", "xvf", "-", "-C", f"/home/jovyan"]

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

    print(f"Copied {filepath} to {destination_path}!", flush=True)


def init_notebook_metadata(task_id, notebook_path):
    """
    Sets random experiment_id and operator_id to notebooks metadata.
    Dicts are passed by reference, so no need to return.

    Parameters
    ----------
    task_id : str
    notebook_path : str
    """
    experiment_id = uuid_alpha()
    operator_id = uuid_alpha()

    with open(notebook_path) as f:
        notebook = json.load(f)

    # sets these values to notebooks
    if notebook is not None:
        notebook["metadata"]["experiment_id"] = experiment_id
        notebook["metadata"]["operator_id"] = operator_id
        notebook["metadata"]["task_id"] = task_id

    with open(notebook_path, "w") as f:
        notebook = json.dump(notebook, f)


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

                if default and default != "None":
                    if default in ["True", "False"]:
                        default = default.lower()
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
