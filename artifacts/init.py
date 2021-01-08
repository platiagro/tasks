# -*- coding: utf-8 -*-
import multiprocessing
import os
from json import load

from controllers.notebook import put_file_in_notebook
from controllers.tasks import create_task

DEFAULT_IMAGE = f'platiagro/platiagro-experiment-image:0.2.0'
CONFIG_PATH = "/samples/config.json"


def insert_tasks():
    with open(CONFIG_PATH) as f:
        tasks = load(f)

        for task in tasks:
            arguments = task["arguments"]
            commands = task["commands"]
            description = task["description"]
            name = task["name"]
            tags = task["tags"]

            if "image" in task:
                image = task["image"]
            else:
                image = os.environ.get("PLATIAGRO_NOTEBOOK_IMAGE", DEFAULT_IMAGE)

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

            path = task.get("path")
            if path:
                for root, dirs, files in os.walk(path):
                    for filename in files:
                        t = multiprocessing.Process(
                            target=put_file_in_notebook,
                            args=(name, os.path.join(root, filename), filename)
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
