# -*- coding: utf-8 -*-
"""Kubeflow notebook server utility functions."""
import tarfile
import time
from tempfile import TemporaryFile

from ast import literal_eval
from kubernetes import client
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
from werkzeug.exceptions import InternalServerError

from kube_config import load_kube_config

NOTEBOOK_NAMESPACE = "anonymous"
NOTEBOOK_NAME = "server"


def create_persistent_volume_claim(name, mount_path):
    """
    Creates a persistent volume claim and mounts it in the default notebook server.
    Parameters
    ----------
    name : str
    mount_path : str
    """
    load_kube_config()

    v1 = client.CoreV1Api()
    custom_api = client.CustomObjectsApi()

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
        v1.create_namespaced_persistent_volume_claim(
            namespace=NOTEBOOK_NAMESPACE,
            body=body,
        )

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
        )
    except ApiException as e:
        body = literal_eval(e.body)
        message = body["message"]
        raise InternalServerError(f"Error while trying to patch notebook server: {message}")


def put_artifact_in_jupyter(artifacts, mount_path):
    load_kube_config()
    api_instance = client.CoreV1Api()

    while True:
        try:
            api_instance.read_namespaced_pod(name="server-0",
                                             namespace=NOTEBOOK_NAMESPACE)
            break
        except ApiException:
            time.sleep(5)

    exec_command = ['tar', 'xvf', '-', '-C', mount_path]
    resp = stream(api_instance.connect_get_namespaced_pod_exec,
                  "server-0",
                  NOTEBOOK_NAMESPACE,
                  command=exec_command,
                  container='server',
                  stderr=True, stdin=True,
                  stdout=True, tty=False,
                  _preload_content=False)

    with TemporaryFile() as tar_buffer:
        with tarfile.open(fileobj=tar_buffer, mode='w') as tar:
            for artifact in artifacts:
                name = artifact["name"]
                tar.add(f"/artifacts/{name}", arcname=f"{name}")

        tar_buffer.seek(0)
        commands = []
        commands.append(tar_buffer.read())

        while resp.is_open():
            resp.update(timeout=1)
            if resp.peek_stdout():
                print("STDOUT: %s" % resp.read_stdout())
            if resp.peek_stderr():
                print("STDERR: %s" % resp.read_stderr())
            if commands:
                c = commands.pop(0)
                # print("Running command... %s\n" % c)
                resp.write_stdin(c.decode(errors='ignore'))
            else:
                break
        resp.close()
