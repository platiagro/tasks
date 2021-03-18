import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestVarianceThreshold(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()
        datasets.boston()

        os.chdir("tasks/variance-threshold")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                threshold=0.0,
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
        self.assertEqual(len(ndarray[0]), 12)  # 12 features
        self.assertEqual(len(names), 12)

    def test_experiment_titanic(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                threshold=0.0,
            )
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
        self.assertEqual(len(ndarray[0]), 12)  # 12 features
        self.assertEqual(len(names), 12)

    def test_boston(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",
                target="medv",

                threshold=0.0,
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
        self.assertEqual(len(ndarray[0]), 13)  # 13 features
        self.assertEqual(len(names), 13)
