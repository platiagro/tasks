import os
import unittest
import uuid

import papermill
import pandas as pd
import numpy as np
from base64 import b64encode
import io
from PIL import Image

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

TEMPORARY_DIR = "tmp"
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/yolo.zip"
LOCAL_OUTPUT_DATA_PATH = f"/{TEMPORARY_DIR}/data/"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestDataAugmentation(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.yolo()

        os.chdir("tasks/data-augmentation")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_default_parameters(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                image_path="image_path",
                augmentation_rate=5,
                horizontal_flip=True,
                vertical_flip=True,
                crop=True,
                color_jitter=True,
                perspective=True,
                rotate=True
            ),
        )

        # Verify output data
        files = os.listdir(LOCAL_OUTPUT_DATA_PATH + "yolo/test/")

        # 6 transformations * augmentation_rate + original_image
        self.assertEqual(len(files), 6*5 + 1)
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "yolo/test/sunflower_transformed_img_3.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )


        #data = datasets.landspaces_test_data()
        for ext in ['png', 'jpg']:

            data = datasets.image_testdata(kind='objects', ext=ext)

            with server.Server() as s:
                response = s.test(data=data, timeout=10)

            images = []
            for raw_str in response["ndarray"]:
                raw_bytes = bytes(raw_str, "latin1")
                img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
                images.append(img)
                
            self.assertEqual(len(images), 5*6)
            self.assertEqual(images[0].size, (930, 1048))

    def test_experiment_no_crop_parameters(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                image_path="image_path",
                augmentation_rate=5,
                horizontal_flip=True,
                vertical_flip=True,
                crop=False,
                color_jitter=True,
                perspective=True,
                rotate=True
            ),
        )

        # Verify output data
        files = os.listdir(LOCAL_OUTPUT_DATA_PATH + "yolo/test/")

        # 6 transformations * augmentation_rate + original_image
        self.assertEqual(len(files), 5*5 + 1)
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "yolo/test/sunflower_transformed_img_0.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )


        #data = datasets.landspaces_test_data()
        for ext in ['png', 'jpg']:

            data = datasets.image_testdata(kind='objects', ext=ext)

            with server.Server() as s:
                response = s.test(data=data, timeout=10)

            images = []
            for raw_str in response["ndarray"]:
                raw_bytes = bytes(raw_str, "latin1")
                img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
                images.append(img)
                
            self.assertEqual(len(images), 5*5)
            self.assertEqual(images[0].size, (930, 1048))