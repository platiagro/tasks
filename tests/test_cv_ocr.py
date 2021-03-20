import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestCVOCR(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.ocr()

        os.chdir("tasks/cv-ocr")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_ocr_output_image(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/ocr_dataset.zip",
                target="target",
                filter_type="incluir",
                model_features="input_image",
                bbox_conf=60,
                segmentation_mode="Considere um único bloco de texto uniforme",
                ocr_engine="Mecanismo de redes neurais com apenas LSTM",
                language="por",
                bbox_return="image",
                image_return_format=".jpg"

            ),
        )

    def test_experiment_ocr_output_nparray(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/ocr_dataset.zip",
                target="target",
                filter_type="incluir",
                model_features="input_image",
                bbox_conf=60,
                segmentation_mode="Considere um único bloco de texto uniforme",
                ocr_engine="Mecanismo de redes neurais com apenas LSTM",
                language="por",
                bbox_return="np_array",
                image_return_format="N/A"

            ),
        )
