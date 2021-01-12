# -*- coding: utf-8 -*-
import datetime
import json
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_HOST = os.getenv("MYSQL_DB_HOST", "mysql.platiagro")
DB_NAME = os.getenv("MYSQL_DB_NAME", "platiagro")
DB_USER = os.getenv("MYSQL_DB_USER", "root")
DB_PASS = os.getenv("MYSQL_DB_PASSWORD", "")
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URL,
                       convert_unicode=True,
                       pool_size=20,
                       pool_recycle=300)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def insert_task(**kwargs):
    """
    Inserts a new task in database. Avoids duplicate task names.

    Parameters
    ----------
    **kwargs
        Arbitrary keyword arguments.

    Returns
    ------
    str or None
        Inserted task_id or None when the task already exists.
    """
    name = kwargs.get("name", None)
    description = kwargs.get("description", None)
    tags = kwargs.get("tags", ["DEFAULT"])
    image = kwargs.get("image", None)
    commands = kwargs.get("commands", None)
    arguments = kwargs.get("arguments", None)
    is_default = kwargs.get("is_default", None)
    parameters = kwargs.get("parameters", [])

    conn = engine.connect()
    text = f'SELECT * FROM tasks WHERE name="{name}" LIMIT 1'
    result = conn.execute(text)
    if result.fetchone():
        return None

    # saves task info to the database
    task_id = str(uuid_alpha())
    created_at = datetime.datetime.now()
    arguments_json = json.dumps(arguments)
    commands_json = json.dumps(commands)
    parameters_json = json.dumps(parameters)
    tags_json = json.dumps(tags)
    experiment_notebook = f'Experiment.ipynb'
    deployment_notebook = f'Deployment.ipynb'
    text = (
        f"INSERT INTO tasks (uuid, name, description, image, commands, arguments, parameters, tags, experiment_notebook_path, deployment_notebook_path, is_default, created_at, updated_at) "
        f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    conn.execute(
        text,
        task_id,
        name,
        description,
        image,
        commands_json,
        arguments_json,
        parameters_json,
        tags_json,
        experiment_notebook,
        deployment_notebook,
        is_default,
        created_at,
        created_at,
    )
    conn.close()

    return task_id


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
