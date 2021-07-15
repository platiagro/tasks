import io
import json
import os
import shutil
from typing import Mapping

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


def iris_testdata():
    data = {
        "data": {
            "ndarray": [[5.1, 3.5, 1.4, 0.2]],
            "names": ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"],
        },
    }
    return data


def iris_testdata_full():
    data = {
        "data": {
            "ndarray": [[5.1, 3.5, 1.4, 0.2, "Iris-setosa"]],
            "names": ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"],
        },
    }
    return data


def titanic():
    name = "titanic.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def titanic_testdata():
    data = {
        "data": {
            "ndarray": [[1, 3, "Braund, Mr. Owen Harris", "male", 22, 1, 0, "A/5 21171", 7.25, None, "S"]],
            "names": ["PassengerId", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],
        },
    }
    return data


def titanic_testdata_full():
    data = {
        "data": {
            "ndarray": [[1, 0, 3, "Braund, Mr. Owen Harris", "male", 22, 1, 0, "A/5 21171", 7.25, None, "S"]],
            "names": ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],
        },
    }
    return data



def boston():
    name = "boston.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def boston_testdata():
    data = {
        "data": {
            "ndarray": [[0.00632, 18.0, 2.31, 0, 0.5379999999999999, 6.575, 65.2, 4.09, 1, 296, 15.3, 396.9, 4.98]],
            "names": ["crim", "zn", "indus", "chas", "nox", "rm", "age", "dis", "rad", "tax", "ptratio", "black", "lstat"],
        },
    }
    return data


def hotel_bookings():
    name = "hotel_bookings.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def hotel_bookings_testdata():
    data = {
        "data": {
            "ndarray": [["Resort Hotel", 342, 2015, "July", 27, 1, 0, 0, 2, 0, 0, "BB", "PRT", "Direct", "Direct", 0, 0, 0, "C", "C", 3, "No Deposit", None, None, 0, "Transient", 0, 0, 0, "Check-Out", "01-07-15"]],
            "names": ["hotel", "lead_time", "arrival_date_year", "arrival_date_month", "arrival_date_week_number", "arrival_date_day_of_month", "stays_in_weekend_nights", "stays_in_week_nights", "adults", "children", "babies", "meal", "country", "market_segment", "distribution_channel", "is_repeated_guest", "previous_cancellations", "previous_bookings_not_canceled", "reserved_room_type", "assigned_room_type", "booking_changes", "deposit_type", "agent", "company", "days_in_waiting_list", "customer_type", "adr", "required_car_parking_spaces", "total_of_special_requests", "reservation_status", "reservation_status_date"],
        },
    }
    return data


def hotel_bookings_testdata_full():
    data = {
        "data": {
            "ndarray": [["Resort Hotel", 0, 342, 2015, "July", 27, 1, 0, 0, 2, 0, 0, "BB", "PRT", "Direct", "Direct", 0, 0, 0, "C", "C", 3, "No Deposit", None, None, 0, "Transient", 0, 0, 0, "Check-Out", "01-07-15"]],
            "names": ["hotel", "is_canceled","lead_time", "arrival_date_year", "arrival_date_month", "arrival_date_week_number", "arrival_date_day_of_month", "stays_in_weekend_nights", "stays_in_week_nights", "adults", "children", "babies", "meal", "country", "market_segment", "distribution_channel", "is_repeated_guest", "previous_cancellations", "previous_bookings_not_canceled", "reserved_room_type", "assigned_room_type", "booking_changes", "deposit_type", "agent", "company", "days_in_waiting_list", "customer_type", "adr", "required_car_parking_spaces", "total_of_special_requests", "reservation_status", "reservation_status_date"],
        },
    }
    return data
    

def imdb():
    name = "imdb.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def imdb_testdata():
    data = {
        "strData": "Un-bleeping-believable! Meg Ryan doesn't even look her usual pert lovable self in this, which normally makes me forgive her shallow ticky acting schtick. Hard to believe she was the producer on this dog. Plus Kevin Kline: what kind of suicide trip has his career been on? Whoosh... Banzai!!! Finally this was directed by the guy who did Big Chill? Must be a replay of Jonestown - hollywood style. Wooofff!",
    }
    return data


def coco():
    name = "coco.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def yolo():
    name = "yolo.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def beans_disease():
    name = "beans_disease.zip"
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


def football_teams():
    name = "football_teams.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)

def report_contexts():
    name = "reports_contexts.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))


def report_contexts_test_data():
    data = {
        "data": {
            "ndarray": ["Quantas plantas da ninha existem ?", "Qual herbicida é melhor contra planta da ninha ?"],
        },
    }
    return data


def document_reader_test_data():
    data = {
        "data": {
            "ndarray": [["Na região da Amazônia, o fertilizante foliar Ômega utilizado na dessecação pré-colheita do feijão, var. Imperador Vermelho, realizado com 84,2 porcento de vagens maduras, resultou em dessecação eficaz (97%) quando utilizado na dose de 4.000 mL.ha-1 , com desempenho similar a Trunfo (1.500 mL.ha-1 ) e Reglone (2.000 mL.ha-1 ). O aumento da dose de Ômega para 5.000 ou 10.000 mL.ha-1 não resultou em diferença significativa na dessecação das plantas (Figura 6);","Qual o resultado da utilização do fertilizante foliar Ômega, quando utilizado cerrado?"]],
            "names":["context","question"]
        },
    }
    return data


def squad_bert_chuncked():
    name = "squad_bert_chuncked_pt.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name, df=pd.read_csv(path))

def squad_bert_chuncked_test():
    data = {
        "data": {
            "ndarray": ["Quantas plantas da ninha existem ?", "Qual herbicida é melhor contra planta da ninha ?"],
        },
    }
    return data


def paracrawl():
    name = "paracrawl_en_pt_test.csv"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)
    
def paracrawl_test_data():
    data = {
        "data": {
            "ndarray": ["Qual o principal objetivo do projeto PLATIA?", "O CPDQ é o maior centro de pesquisa do Brasil"],
        },
    }
    return data


def hymenoptera():
    name = "hymenoptera.zip"
    url = f"https://raw.githubusercontent.com/platiagro/datasets/master/samples/{name}"
    content = requests.get(url).content

    os.makedirs("/tmp/data", exist_ok=True)

    path = f"/tmp/data/{name}"
    with open(path, "wb") as f:
        f.write(content)

    metadata(name=name)


def moving_squares_monitoring():
    name = "moving_squares_monitoring.csv"
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
