# -*- coding: utf-8 -*-
import json
import multiprocessing
import os

from database import insert_task
from notebook import create_persistent_volume_claim, put_file_in_notebook

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

            try:
                task_id = insert_task(
                    name=name,
                    description=description,
                    tags=tags,
                    image=image,
                    commands=commands,
                    arguments=arguments,
                    is_default=True,
                )

                # mounts a volume for the task in the notebook server
                create_persistent_volume_claim(name=f"task-{task_id}",
                                               mount_path=f"/home/jovyan/{name}")
            except Exception as e:
                print(e)
                pass


def main():
    """
    Job that creates tasks in PlatIAgro from a config file.
    """
    t = multiprocessing.Process(target=create_tasks)
    t.start()
    t.join()

    # Prepare jobs to copy task files and artifacts
    jobs = []
    with open(CONFIG_PATH) as f:
        tasks = json.load(f)
        for task in tasks:
            name = task["name"]
            path = task.get("path")
            if path:
                for root, dirs, files in os.walk(path):
                    for filename in files:
                        t = multiprocessing.Process(
                            target=put_file_in_notebook,
                            args=(name, os.path.join(root, filename), filename)
                        )
                        jobs.append(t)

    # Start the threads
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    print("done!", flush=True)


if __name__ == "__main__":
    main()
