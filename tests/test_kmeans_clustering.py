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

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        notebook_path = "tasks/kmeans-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
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
        notebook_path = "tasks/kmeans-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
            ),
        )

    def test_boston(self):
        notebook_path = "tasks/kmeans-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",

                n_clusters=3,
                n_init=10,
                max_iter=300,
                algorithm="auto",
            ),
        )
