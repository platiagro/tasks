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
class TestKmeansClustering(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()
        datasets.boston()

        os.chdir("tasks/kmeans-clustering")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self, mock_log_metrics):
        mock_log_metrics.assert_any_call()
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",

                filter_type="remover",
                model_features="Species",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
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
        self.assertEqual(len(ndarray[0]), 8)  # 4 features + 1 cluster + 3 distance to clusters
        self.assertEqual(len(names), 8)

    def test_experiment_titanic(self, mock_log_metrics):
        mock_log_metrics.assert_any_call()
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",

                filter_type="remover",
                model_features="Survived",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
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
        self.assertEqual(len(ndarray[0]), 15)  # 11 features+ 1 cluster + 3 distance to clusters
        self.assertEqual(len(names), 15)

    def test_experiment_boston(self, mock_log_metrics):
        mock_log_metrics.assert_any_call()
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",

                filter_type="remover",
                model_features="medv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
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
        self.assertEqual(len(ndarray[0]), 17)  # 13 features+ 1 cluster + 3 distance to clusters
        self.assertEqual(len(names), 17)
