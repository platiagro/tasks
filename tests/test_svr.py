import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestSVR(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.boston()

    def tearDown(self):
        datasets.clean()

    def test_boston(self):
        experiment_path = "svr/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",
                target="medv",

                filter_type = "remover",
                model_features = "",

                one_hot_features = "",

                kernel = "rbf",
                degree = 3,
                gamma = "auto",
                C = 1.0,
                max_iter = -1,
            ),
        )
