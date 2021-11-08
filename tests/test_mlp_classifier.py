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
class TestMLPClassifier(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()

        os.chdir("tasks/mlp-classifier")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                filter_type="remover",
                model_features="",

                one_hot_features="",

                hidden_layer_sizes=100,
                activation="relu",
                solver="adam",
                learning_rate="constant",
                max_iter=200,
                shuffle=True,

                method="predict_proba",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.iris_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 8)  # 4 features + 1 class + 3 probas
        self.assertEqual(len(names), 8)
        mock_log_metrics.assert_any_call()

    def test_experiment_titanic(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                filter_type="remover",
                model_features="",

                one_hot_features="",

                hidden_layer_sizes=100,
                activation="relu",
                solver="adam",
                learning_rate="constant",
                max_iter=200,
                shuffle=True,

                method="predict_proba",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.titanic_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 14)  # 11 features + 1 class + 2 probas
        self.assertEqual(len(names), 14)
        mock_log_metrics.assert_any_call()
