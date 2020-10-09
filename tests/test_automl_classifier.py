import os
import unittest
import uuid

import papermill
import requests

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestAutoMLClassifier(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        experiment_path = "automl-classifier/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                filter_type = "remover",
                model_features = "",

                one_hot_features = "",

                time_left_for_this_task = 60,
                per_run_time_limit = 60,
                ensemble_size = 50,

                method = "predict_proba",
            ),
        )
