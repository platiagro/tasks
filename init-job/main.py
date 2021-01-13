# -*- coding: utf-8 -*-
import json
import multiprocessing
import os
import warnings

from database import insert_task
from notebook import create_persistent_volume_claim, copy_file_inside_pod, \
    init_notebook_metadata, parse_parameters

CONFIG_PATH = "/tasks/config.json"


def create_tasks():
    """
    Reads config file, inserts tasks in database, and a allocates a volume.
    """
    with open(CONFIG_PATH) as f:
        tasks = json.load(f)

        for task in tasks:
            arguments = task["arguments"]
            commands = task["commands"]
            description = task["description"]
            name = task["name"]
            tags = task["tags"]
            image = task["image"]
            path = task.get("path")
            parameters = []

            if path:
                experiment_notebook_path = "Experiment.ipynb"
                deployment_notebook_path = "Deployment.ipynb"
                parameters = parse_parameters(f"{path}/{experiment_notebook_path}")
            else:
                experiment_notebook_path = None
                deployment_notebook_path = None

            task_id = insert_task(
                name=name,
                description=description,
                tags=tags,
                image=image,
                commands=commands,
                arguments=arguments,
                is_default=True,
                parameters=parameters,
                experiment_notebook_path=experiment_notebook_path,
                deployment_notebook_path=deployment_notebook_path,
            )

            if task_id is None:
                warnings.warn(f"{name} already exists. Skipping...")
            else:
                print(f"Creating {name}...", flush=True)

                # mounts a volume for the task in the notebook server
                create_persistent_volume_claim(
                    name=f"task-{task_id}",
                    mount_path=f"/home/jovyan/tasks/{name}",
                )

                # Prepare jobs to copy task files and artifacts
                jobs = []
                if path:
                    for root, dirs, files in os.walk(path):
                        for filename in files:
                            # Local filepath
                            filepath = os.path.join(root, filename)
                            # Filepath inside pod
                            pod_root = root.lstrip(path)
                            destination_path = os.path.join(name, pod_root, filename)

                            if filename in {"Experiment.ipynb", "Deployment.ipynb"}:
                                init_notebook_metadata(task_id, notebook_path=filepath)

                            t = multiprocessing.Process(
                                target=copy_file_inside_pod,
                                args=(filepath, destination_path)
                            )
                            jobs.append(t)

                # Start the jobs
                for j in jobs:
                    j.start()

                # Ensure all of the jobs have finished
                for j in jobs:
                    j.join()


def main():
    """
    Job that creates tasks in PlatIAgro from a config file.
    """
    create_tasks()

    print("done!", flush=True)


if __name__ == "__main__":
    main()
