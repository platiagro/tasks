# -*- coding: utf-8 -*-
import json
import multiprocessing
import os
import warnings

from database import insert_task
from notebook import create_persistent_volume_claim, copy_file_inside_pod

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

            task_id = insert_task(
                name=name,
                description=description,
                tags=tags,
                image=image,
                commands=commands,
                arguments=arguments,
                is_default=True,
            )

            if task_id is None:
                warnings.warn(f"{name} already exists. Skipping...")
            else:
                print(f"Creating {name}...", flush=True)

                # mounts a volume for the task in the notebook server
                create_persistent_volume_claim(
                    name=f"task-{task_id}",
                    mount_path=f"/home/jovyan/{name}",
                )

                # Prepare jobs to copy task files and artifacts
                jobs = []
                path = task.get("path")
                if path:
                    for root, dirs, files in os.walk(path):
                        for filename in files:
                            # Local filepath
                            filepath = os.path.join(root, filename)
                            # Filepath inside pod
                            pod_root = root.lstrip(path)
                            destination_path = os.path.join(name, pod_root, filename)

                            # copy_file_inside_pod(filepath, destination_path)

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
