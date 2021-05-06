import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestFilterSelection(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()
        datasets.hotel_bookings()

        os.chdir("tasks/filter-selection")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                features_to_filter=["SepalLengthCm", "Species"]
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
        self.assertEqual(len(ndarray[0]), 3)  # 5 features - 2 removed
        self.assertEqual(len(names), 3)

    def test_experiment_titanic(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                features_to_filter=["Name", "Survived"]
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
        self.assertEqual(len(ndarray[0]), 10)  # 12 features - 2 removed
        self.assertEqual(len(names), 10)

    def test_experiment_hotel_bookings(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hotel_bookings.csv",
                features_to_filter=["reservation_status_date", "arrival_date_year", "is_canceled"]
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
        self.assertEqual(len(ndarray[0]), 29)  # 32 features - 3 removed
        self.assertEqual(len(names), 29)
