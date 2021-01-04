import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestCVYOLO(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.face_detection()

    def tearDown(self):
        datasets.clean()

    def test_experiment_ocr_output_image(self):
        notebook_path = "tasks/cv-mtcnn-face-detection/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/football_teams.zip",
            ),
        )


