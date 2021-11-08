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
class TestIsolationForestClustering(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()
        datasets.boston()
        datasets.hotel_bookings()

        os.chdir("tasks/isolation-forest-clustering")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",

                filter_type="remover",
                model_features="Species",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
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
        self.assertEqual(len(ndarray[0]), 5)  # 4 features + 1 anomaly score
        mock_log_metrics.assert_any_call()
        self.assertEqual(len(names), 5)

    def test_experiment_titanic(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",

                filter_type="remover",
                model_features="Survived",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
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
        self.assertEqual(len(ndarray[0]), 12)  # 11 features + 1 anomaly score
        self.assertEqual(len(names), 12)
        mock_log_metrics.assert_any_call()

    def test_experiment_boston(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",

                filter_type="remover",
                model_features="medv",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
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
        self.assertEqual(len(ndarray[0]), 14)  # 13 features  + 1 anomaly score
        self.assertEqual(len(names), 14)
        mock_log_metrics.assert_any_call()

    def test_hotel_bookings(self, mock_log_metrics):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",

                filter_type="remover",
                model_features="is_canceled",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.hotel_bookings_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 32)  # 31 features + 1 anomaly score
        self.assertEqual(len(names), 32)
        mock_log_metrics.assert_any_call()
