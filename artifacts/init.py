# -*- coding: utf-8 -*-
import asyncio
import multiprocessing
from json import load
from os import environ

from controllers.notebook import put_file_in_notebook
from controllers.tasks import create_task

DEFAULT_IMAGE = f'platiagro/platiagro-experiment-image:0.2.0'
DEPLOYMENT_NOTEBOOK = "config/Deployment.ipynb"
EXPERIMENT_NOTEBOOK = "config/Experiment.ipynb"
CONFIG_PATH = "/samples/config.json"


def insert_tasks():
    with open(CONFIG_PATH) as f:
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


if __name__ == "__main__":
    t = multiprocessing.Process(target=insert_tasks)
    t.start()
    t.join()

    jobs = []
    with open(CONFIG_PATH) as f:
        tasks = load(f)
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
                t = multiprocessing.Process(
                    target=put_file_in_notebook,
                    args=(name, experiment_notebook, "Experiment.ipynb")
                )
                jobs.append(t)
                t = multiprocessing.Process(
                    target=put_file_in_notebook,
                    args=(name, deployment_notebook, "Deployment.ipynb")
                )
                jobs.append(t)

            if artifacts and len(artifacts) > 0:
                for artifact in artifacts:
                    a_name = artifact["name"]
                    t = multiprocessing.Process(
                        target=put_file_in_notebook,
                        args=(name, f"/artifacts/{a_name}", a_name)
                    )
                    jobs.append(t)

    # Start the threads
    for j in jobs:
        j.start()
    # Ensure all of the threads have finished
    for j in jobs:
        j.join()
    print("done!", flush=True)
