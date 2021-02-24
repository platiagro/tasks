import os
import shutil

import requests


def iris():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/iris.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/iris.csv", "wb") as f:
        f.write(content)


def titanic():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/titanic.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/titanic.csv", "wb") as f:
        f.write(content)


def boston():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/boston.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/boston.csv", "wb") as f:
        f.write(content)


def hotel_bookings():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/hotel_bookings.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/hotel_bookings.csv", "wb") as f:
        f.write(content)


def imdb():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/imdb.csv"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/imdb.csv", "wb") as f:
        f.write(content)


def coco():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/coco.zip"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/coco.zip", "wb") as f:
        f.write(content)


def ocr():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/ocr_dataset.zip"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/ocr_dataset.zip", "wb") as f:
        f.write(content)


def face_detection():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/football_teams.zip"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/football_teams.zip", "wb") as f:
        f.write(content)


def paracrawl():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/paracrawl_en_pt_test.xlsx"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/paracrawl_en_pt_test.xlsx", "wb") as f:
        f.write(content)

    response = requests.post(
        "http://localhost:8080/datasets",
        files={"file": open("/tmp/data/paracrawl_en_pt_test.xlsx", "rb")},
    )
    response.raise_for_status()
    return response.json()


def hymenoptera():
    url = "https://raw.githubusercontent.com/platiagro/datasets/master/samples/hymenoptera_data.zip"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    with open("/tmp/data/hymenoptera_data.zip", "wb") as f:
        f.write(content)


def clean():
    shutil.rmtree("/tmp/data")
