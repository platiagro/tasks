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
class TestRandomForestRegressor(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.boston()

        os.chdir("tasks/random-forest-regressor")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_boston(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",
                target="medv",

                filter_type="remover",
                model_features="",

                one_hot_features="",

                n_estimators=10,
                criterion="mse",
                max_depth=None,
                max_features="auto",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.boston_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 14)  # 13 features + 1 prediction
        self.assertEqual(len(names), 14)
        mock_log_metrics.assert_any_call()
