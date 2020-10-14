import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestDescriptiveAnalysis(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.hotel_bookings()

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        experiment_path = "feature-tools/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",
                date=None,
                group=["SepalLengthCm"],
            ),
        )

    def test_experiment_hotel_bookings(self):
        experiment_path = "feature-tools/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",
                target="is_canceled",
                date="reservation_status_date",
                group=["hotel"],
            ),
        )
