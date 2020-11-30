import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestNLPTextPreProcessor(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.ocr()

    def tearDown(self):
        datasets.clean()

    def test_experiment_ocr_output_image(self):
        notebook_path = "tasks/cv-ocr/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/ocr_dataset.zip",
                target = "target_OCR" ,
                filter_type = "incluir",
                model_features = "input_image",
                bbox_conf = 60,
                segmentation_mode = "Assume a single uniform block of text.",
                ocr_engine = "Neural nets LSTM engine only.",
                language = "por",
                bbox_return = "image",
                image_return_format = ".jpg"

            ),
        )
       
       
    def test_experiment_ocr_output_nparray(self):
        notebook_path = "tasks/cv-ocr/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/ocr_dataset.zip",
                target = "target_OCR" ,
                filter_type = "incluir",
                model_features = "input_image",
                bbox_conf = 60,
                segmentation_mode = "Assume a single uniform block of text.",
                ocr_engine = "Neural nets LSTM engine only.",
                language = "por",
                bbox_return = "np_array",
                image_return_format = "N/A"

            ),
        )
       
       
