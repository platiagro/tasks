# -*- coding: utf-8 -*-
"""Tasks controller."""
import re
from json import dumps, loads
from os.path import join

from werkzeug.exceptions import BadRequest

from controllers.notebook import create_persistent_volume_claim
from database import db_session
from jupyter import create_new_file
from models.task import Task
from object_storage import BUCKET_NAME, put_object
from utils import get_data, uuid_alpha

PREFIX = "tasks"
VALID_TAGS = ["DATASETS", "DEFAULT", "DESCRIPTIVE_STATISTICS", "FEATURE_ENGINEERING",
              "PREDICTOR", "COMPUTER_VISION", "NLP"]
DEPLOYMENT_NOTEBOOK = loads(get_data("artifacts", "config/Deployment.ipynb"))
EXPERIMENT_NOTEBOOK = loads(get_data("artifacts", "config/Experiment.ipynb"))


def create_task(**kwargs):
    """
    Creates a new task in our database/object storage.

    Parameters
    ----------
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    dict
        The task attributes.

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
    experiment_notebook = kwargs.get("experiment_notebook", None)
    deployment_notebook = kwargs.get("deployment_notebook", None)
    is_default = kwargs.get("is_default", None)
    copy_from = kwargs.get("copy_from", None)

    if not isinstance(name, str):
        raise BadRequest("name is required")

    has_notebook = experiment_notebook or deployment_notebook

    if copy_from and has_notebook:
        raise BadRequest("Either provide notebooks or a task to copy from")

    if len(tags) == 0:
        tags = ["DEFAULT"]

    if any(tag not in VALID_TAGS for tag in tags):
        valid_str = ",".join(VALID_TAGS)
        raise BadRequest(f"Invalid tag. Choose any of {valid_str}")

    # check if image is a valid docker image
    raise_if_invalid_docker_image(image)

    check_comp_name = db_session.query(Task).filter_by(name=name).first()
    if check_comp_name:
        raise BadRequest("a task with that name already exists")

    task_id = str(uuid_alpha())

    # loads a sample notebook if none was sent
    if experiment_notebook is None and "DATASETS" not in tags:
        experiment_notebook = EXPERIMENT_NOTEBOOK

    if deployment_notebook is None and "DATASETS" not in tags:
        deployment_notebook = DEPLOYMENT_NOTEBOOK

    # The new task must have its own task_id, experiment_id and operator_id.
    # Notice these values are ignored when a notebook is run in a pipeline.
    # They are only used by JupyterLab interface.
    init_notebook_metadata(task_id, deployment_notebook, experiment_notebook)

    # saves new notebooks to object storage
    if "DATASETS" not in tags:
        obj_name = f"{PREFIX}/{task_id}/Experiment.ipynb"
        experiment_notebook_path = f"minio://{BUCKET_NAME}/{obj_name}"
        put_object(obj_name, dumps(experiment_notebook).encode())

        obj_name = f"{PREFIX}/{task_id}/Deployment.ipynb"
        deployment_notebook_path = f"minio://{BUCKET_NAME}/{obj_name}"
        put_object(obj_name, dumps(deployment_notebook).encode())

        # create deployment notebook and experiment_notebook on jupyter
        create_jupyter_files(task_name=name,
                             deployment_notebook=dumps(deployment_notebook).encode(),
                             experiment_notebook=dumps(experiment_notebook).encode())
    else:
        experiment_notebook_path = None
        deployment_notebook_path = None

    # mounts a volume for the task in the notebook server
    create_persistent_volume_claim(name=f"task-{task_id}",
                                   mount_path=f"/home/jovyan/{name}")

    # saves task info to the database
    task = Task(uuid=task_id,
                name=name,
                description=description,
                tags=tags,
                image=image,
                commands=commands,
                arguments=arguments,
                experiment_notebook_path=experiment_notebook_path,
                deployment_notebook_path=deployment_notebook_path,
                is_default=is_default)
    db_session.add(task)
    db_session.commit()

    return task.as_dict()


def create_jupyter_files(task_name, deployment_notebook, experiment_notebook):
    """
    Creates jupyter notebook files on jupyter server.

    Parameters
    ----------
    task_name : str
    deployment_notebook : bytes
        The notebook content.
    experiment_notebook : bytes
        The notebook content.
    """
    # always try to create tasks folder to guarantee its existence
    create_new_file(PREFIX, is_folder=True)

    path = f"{PREFIX}/{task_name}"
    create_new_file(path=path, is_folder=True)

    if deployment_notebook is not None:
        deployment_notebook_path = join(path, "Deployment.ipynb")
        create_new_file(path=deployment_notebook_path,
                        is_folder=False,
                        content=deployment_notebook)

    if experiment_notebook is not None:
        experiment_notebook_path = join(path, "Experiment.ipynb")
        create_new_file(path=experiment_notebook_path,
                        is_folder=False,
                        content=experiment_notebook)


def init_notebook_metadata(task_id, deployment_notebook, experiment_notebook):
    """
    Sets random experiment_id and operator_id to notebooks metadata.
    Dicts are passed by reference, so no need to return.

    Parameters
    ----------
    task_id : str
    deployment_notebook : dict
    experiment_notebook : dict
    """
    experiment_id = uuid_alpha()
    operator_id = uuid_alpha()

    # sets these values to notebooks
    if deployment_notebook is not None:
        deployment_notebook["metadata"]["experiment_id"] = experiment_id
        deployment_notebook["metadata"]["operator_id"] = operator_id
        deployment_notebook["metadata"]["task_id"] = task_id
    if experiment_notebook is not None:
        experiment_notebook["metadata"]["experiment_id"] = experiment_id
        experiment_notebook["metadata"]["operator_id"] = operator_id
        experiment_notebook["metadata"]["task_id"] = task_id


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
        raise BadRequest("invalid docker image name")
