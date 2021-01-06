# -*- coding: utf-8 -*-
from json import load
from os import environ

from werkzeug.exceptions import BadRequest

from controllers.notebook import put_artifact_in_jupyter
from controllers.tasks import create_task
from models.task import DEFAULT_IMAGE


def read_notebook(notebook_path):
    """
    Reads the contents of a notebook.

    Parameters
    ----------
    notebook_path :str
        The path to the notebook file.

    Returns
    -------
    bytes
        The notebook content as bytes.
    """
    with open(notebook_path, "rb") as f:
        notebook = load(f)
    return notebook


with open("/samples/config.json") as f:
    tasks = load(f)

    for task in tasks:
        name = task["name"]
        description = task["description"]
        tags = task["tags"]

        if "image" in task:
            image = task["image"]
        else:
            image = environ.get("PLATIAGRO_NOTEBOOK_IMAGE", DEFAULT_IMAGE)

        commands = task["commands"]
        arguments = task["arguments"]

        try:
            experiment_notebook = read_notebook(task["experimentNotebook"])
        except KeyError:
            experiment_notebook = None

        try:
            deployment_notebook = read_notebook(task["deploymentNotebook"])
        except KeyError:
            deployment_notebook = None

        try:
            create_task(name=name,
                        description=description,
                        tags=tags,
                        image=image,
                        commands=commands,
                        arguments=arguments,
                        experiment_notebook=experiment_notebook,
                        deployment_notebook=deployment_notebook,
                        is_default=True)
        except BadRequest:
            pass

    for task in tasks:
        name = task["name"]
        artifacts = task["artifacts"]
        if artifacts and len(artifacts) > 0:
            put_artifact_in_jupyter(artifacts=artifacts,
                                    mount_path=f"/home/jovyan/{name}")
