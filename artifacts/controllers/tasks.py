# -*- coding: utf-8 -*-
"""Tasks controller."""
import random
import re
import uuid
from datetime import datetime
from json import dumps

from controllers.notebook import create_persistent_volume_claim
from database import engine

VALID_TAGS = ["DATASETS", "DEFAULT", "DESCRIPTIVE_STATISTICS",
              "FEATURE_ENGINEERING", "PREDICTOR", "COMPUTER_VISION", "NLP"]


def create_task(**kwargs):
    """
    Creates a new task in our database/object storage.
    Parameters
    ----------
    **kwargs
        Arbitrary keyword arguments.
    Raises
    ------
    BadRequest
        When the `**kwargs` (task attributes) are invalid.
    """
    name = kwargs.get("name", None)
    description = kwargs.get("description", None)
    tags = kwargs.get("tags", ["DEFAULT"])
    image = kwargs.get("image", None)
    commands = kwargs.get("commands", None)
    arguments = kwargs.get("arguments", None)
    is_default = kwargs.get("is_default", None)

    if not isinstance(name, str):
        raise Exception("name is required")

    if len(tags) == 0:
        tags = ["DEFAULT"]

    if any(tag not in VALID_TAGS for tag in tags):
        valid_str = ",".join(VALID_TAGS)
        raise Exception(f"Invalid tag. Choose any of {valid_str}")

    # check if image is a valid docker image
    raise_if_invalid_docker_image(image)

    conn = engine.connect()
    text = f'SELECT * FROM tasks WHERE name="{name}" LIMIT 1'
    result = conn.execute(text)
    if result.fetchone():
        raise Exception("a task with that name already exists")

    # saves task info to the database
    task_id = str(uuid_alpha())
    created_at = datetime.now()
    arguments_json = dumps(arguments).replace('\\', '\\\\')
    commands_json = dumps(commands)
    tags_json = dumps(tags)
    experiment_notebook = f'/home/jovyan/{name}/Experiment.ipynb'
    deployment_notebook = f'/home/jovyan/{name}/Deployment.ipynb'
    text = (
        f"INSERT INTO tasks (uuid, name, description, image, commands, arguments, tags, experiment_notebook_path, deployment_notebook_path, is_default, created_at, updated_at) "
        f"VALUES ('{task_id}', '{name}', '{description}', '{image}', '{commands_json}', '{arguments_json}', '{tags_json}', '{experiment_notebook}', '{deployment_notebook}', {is_default}, '{created_at}', '{created_at}')"
    )
    conn.execute(text)
    conn.close()

    # mounts a volume for the task in the notebook server
    create_persistent_volume_claim(name=f"task-{task_id}",
                                   mount_path=f"/home/jovyan/{name}")

    return


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


def raise_if_invalid_docker_image(image):
    """
    Raise an error if a str does not meet the standards for a docker image name.
    Example: (username/organization)/name-of-the-image:tag
    Parameters
    ----------
    image : str or None
        The image name.
    Raises
    ------
    BadRequest
        When a given image is a invalid one.
    """
    pattern = re.compile("[a-z0-9.-]+([/]{1}[a-z0-9.-]+)+([:]{1}[a-z0-9.-]+){0,1}$")

    if image and pattern.match(image) is None:
        raise Exception("invalid docker image name")
