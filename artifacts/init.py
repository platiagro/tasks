# -*- coding: utf-8 -*-
from json import load
from os import environ

from controllers.notebook import put_file_in_notebook
from controllers.tasks import create_task

DEFAULT_IMAGE = f'platiagro/platiagro-experiment-image:0.2.0'
DEPLOYMENT_NOTEBOOK = "config/Deployment.ipynb"
EXPERIMENT_NOTEBOOK = "config/Experiment.ipynb"


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
            create_task(name=name,
                        description=description,
                        tags=tags,
                        image=image,
                        commands=commands,
                        arguments=arguments,
                        is_default=True)
        except Exception as e:
            print(e)
            pass

    for task in tasks:
        artifacts = task["artifacts"]
        name = task["name"]
        tags = task["tags"]

        try:
            experiment_notebook = task["experimentNotebook"]
        except KeyError:
            experiment_notebook = None
        try:
            deployment_notebook = task["deploymentNotebook"]
        except KeyError:
            deployment_notebook = None

    # loads a sample notebook if none was sent
    if experiment_notebook is None and "DATASETS" not in tags:
        experiment_notebook = EXPERIMENT_NOTEBOOK
    if deployment_notebook is None and "DATASETS" not in tags:
        deployment_notebook = DEPLOYMENT_NOTEBOOK

    if "DATASETS" not in tags:
        put_file_in_notebook(name, experiment_notebook, "Experiment.ipynb")
        put_file_in_notebook(name, deployment_notebook, "Deployment.ipynb")

    if artifacts and len(artifacts) > 0:
        for artifact in artifacts:
            a_name = artifact["name"]
            put_file_in_notebook(name, f"/artifacts/{a_name}", a_name)
