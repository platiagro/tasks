import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestMonitoringUnsupervisedMulticlass(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.moving_squares_monitoring()

        os.chdir("tasks/monitoring-unsupervised-multiclass")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_moving_squares_monitoring(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/moving_squares_monitoring.csv",

                n_target=50,
                n_ref=5 * n_target,
                K=3,
            ),
        )
