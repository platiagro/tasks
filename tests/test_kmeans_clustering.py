import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


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

    def test_experiment_iris(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
            ),
        )

    def test_experiment_titanic(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
            ),
        )

    def test_experiment_boston(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
            ),
        )
