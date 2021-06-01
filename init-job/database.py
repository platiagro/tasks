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
                       pool_size=5,
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
    name = kwargs.get("name")
    description = kwargs.get("description")
    tags = kwargs.get("tags", ["DEFAULT"])
    image = kwargs.get("image")
    commands = kwargs.get("commands")
    arguments = kwargs.get("arguments")
    is_default = kwargs.get("is_default")
    parameters = kwargs.get("parameters", [])
    experiment_notebook_path = kwargs.get("experiment_notebook_path")
    deployment_notebook_path = kwargs.get("deployment_notebook_path")
    cpu_limit = kwargs.get("cpu_limit")
    cpu_request = kwargs.get("cpu_request")
    memory_limit = kwargs.get("memory_limit")
    memory_request = kwargs.get("memory_request")
    readiness_probe_initial_delay_seconds = kwargs.get("readiness_probe_initial_delay_seconds", 60)

    conn = engine.connect()
    text = f'SELECT uuid FROM tasks WHERE name="{name}" LIMIT 1'
    result = conn.execute(text)
    row = result.fetchone()
    if row:
        return row[0]

    # saves task info to the database
    task_id = str(uuid_alpha())
    created_at = datetime.datetime.now()
    arguments_json = json.dumps(arguments)
    commands_json = json.dumps(commands)
    parameters_json = json.dumps(parameters)
    tags_json = json.dumps(tags)

    text = (
        "INSERT INTO tasks (uuid, name, description, image, commands, arguments, parameters, tags, "
        "experiment_notebook_path, deployment_notebook_path, cpu_limit, cpu_request, memory_limit, memory_request, "
        "readiness_probe_initial_delay_seconds, is_default, created_at, updated_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
        experiment_notebook_path,
        deployment_notebook_path,
        cpu_limit,
        cpu_request,
        memory_limit,
        memory_request,
        readiness_probe_initial_delay_seconds,
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
