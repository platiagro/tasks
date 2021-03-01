import io
import json
import os
import shutil

import minio
import minio.error
import pandas as pd
import platiagro.featuretypes
import requests

BUCKET_NAME = "anonymous"
PREFIX = "datasets"
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
    name = "iris.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def titanic():
    name = "titanic.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def boston():
    name = "boston.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def hotel_bookings():
    name = "hotel_bookings.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def imdb():
    name = "imdb.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def coco():
    name = "coco.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def ocr():
    name = "ocr_dataset.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def face_detection():
    name = "football_teams.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def paracrawl():
    name = "paracrawl_en_pt_test.xlsx"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def hymenoptera():
    name = "hymenoptera_data.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def metadata(name, df=None):
    root_metadata = {
        "filename": name,
        "read_only": False,
    }

    if isinstance(df, pd.DataFrame):
        root_metadata["columns"] = df.columns.tolist()
        root_metadata["total"] = len(df.index)
        root_metadata["featuretypes"] = platiagro.featuretypes.infer_featuretypes(df)

    try:
        MINIO_CLIENT.make_bucket(BUCKET_NAME)
    except minio.error.BucketAlreadyOwnedByYou:
        pass

    object_name = f"{PREFIX}/{name}/{name}.metadata"
    buffer = io.BytesIO(json.dumps(root_metadata).encode())
    MINIO_CLIENT.put_object(
        bucket_name=BUCKET_NAME,
        object_name=object_name,
        data=buffer,
        length=buffer.getbuffer().nbytes,
    )


def clean():
    shutil.rmtree("/tmp/data")
