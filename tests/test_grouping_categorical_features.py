import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestGroupingCategoricalFeatures(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.titanic()
        datasets.hotel_bookings()

    def tearDown(self):
        datasets.clean()

    def test_experiment_titanic(self):
        experiment_path = "grouping-categorical-features/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                high_cardinality_features="Pclass",

                method="kmeans",

                threshold=0.1,
                n=10,
            ),
        )

    def test_hotel_bookings(self):
        experiment_path = "grouping-categorical-features/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",
                target="is_canceled",

                high_cardinality_features="hotel",

                method="kmeans",

                threshold=0.1,
                n=10,
            ),
        )

