import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


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

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        experiment_path = "isolation-forest-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
            ),
        )

    def test_experiment_titanic(self):
        experiment_path = "isolation-forest-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
            ),
        )

    def test_boston(self):
        experiment_path = "isolation-forest-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
            ),
        )

    def test_hotel_bookings(self):
        experiment_path = "isolation-forest-clustering/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",

                max_samples="auto",
                contamination=0.1,
                max_features=1.0,
            ),
        )
