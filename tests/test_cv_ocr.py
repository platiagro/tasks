import os
import unittest
import uuid
from unittest import mock

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


@mock.patch("mlflow.log_metric")
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

    def test_experiment_ocr_output_data(self, mock_log_metrics):
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

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        for ext in ['png', 'jpg']:
            data = datasets.image_testdata(kind='text',  ext=ext)

            with server.Server() as s:
                response = s.test(data=data, timeout=10)

            print(response)
            for bbox in response['ndarray']:
                xmin, ymin, xmax, ymax, text = bbox
                self.assertGreater(xmax, xmin, "BoundingBox incorreta.")
                self.assertGreater(ymax, ymin, "BoundingBox incorreta.")
        mock_log_metrics.assert_any_call()

    """
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
    """
