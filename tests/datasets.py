import os
import shutil

import minio
import requests

BUCKET_NAME = "anonymous"
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minio")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minio123")

MINIO_CLIENT = minio.Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)


def iris():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/iris.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/iris.csv", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/iris.csv", "rb")},
    )
    response.raise_for_status()
    return response.json()


def titanic():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/titanic.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/titanic.csv", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/titanic.csv", "rb")},
    )
    response.raise_for_status()
    return response.json()


def boston():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/boston.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/boston.csv", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/boston.csv", "rb")},
    )
    response.raise_for_status()
    return response.json()


def hotel_bookings():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/hotel_bookings.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/hotel_bookings.csv", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/hotel_bookings.csv", "rb")},
    )
    response.raise_for_status()
    return response.json()


def imdb():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/imdb.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/imdb.csv", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/imdb.csv", "rb")},
    )
    response.raise_for_status()
    return response.json()

def coco():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/coco.zip"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/coco.zip", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/coco.zip", "rb")},
    )
    response.raise_for_status()
    return response.json()


def clean():
    shutil.rmtree("/tmp/data")

    objects_to_delete = MINIO_CLIENT.list_objects(BUCKET_NAME, prefix="datasets", recursive=True)
    for obj in objects_to_delete:
        MINIO_CLIENT.remove_object(BUCKET_NAME, obj.object_name)
