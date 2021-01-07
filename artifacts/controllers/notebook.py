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


def put_file_in_notebook(name, filePath, fileName):
    load_kube_config()
    api_instance = client.CoreV1Api()

    while True:
        try:
            api_instance.read_namespaced_pod(name="server-0",
                                             namespace=NOTEBOOK_NAMESPACE)
            break
        except ApiException:
            time.sleep(5)

    exec_command = ['tar', 'xvf', '-', '-C', f"/home/jovyan/{name}"]
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
            tar.add(filePath, arcname=fileName)

        commands = []
        commands.append(filePath)
        while resp.is_open():
            resp.update(timeout=10)
            if resp.peek_stdout():
                print("STDOUT: %s" % resp.read_stdout())
            if resp.peek_stderr():
                print("STDERR: %s" % resp.read_stderr())
            if commands:
                commands.pop(0)
                tar_buffer.seek(0)
                data = tar_buffer.read(10000)
                while data:
                    resp.write_stdin(data)
                    data = tar_buffer.read(10000)
            else:
                break
        resp.close()
