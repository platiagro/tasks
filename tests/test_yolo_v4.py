import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestYOLOv4(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.coco()

    def tearDown(self):
        datasets.clean()

    def test_experiment_coco(self):
        experiment_path = "yolo_v4/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/coco.zip",
            ),
        )
