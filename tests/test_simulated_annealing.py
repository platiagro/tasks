import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestSimulatedAnnealing(unittest.TestCase):

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
        notebook_path = "tasks/simulated-annealing/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                date=None,
                group=["SepalLengthCm"],
                alpha=0.5,
            ),
        )

    def test_experiment_hotel_bookings(self):
        notebook_path = "tasks/simulated-annealing/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",
                target="is_canceled",

                date="reservation_status_date",
                group=["hotel"],
                alpha=0.5,
            ),
        )
