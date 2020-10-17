import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestRFESelector(unittest.TestCase):

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
        notebook_path = "tasks/rfe-selector/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                min_features=3,
                n_folds=10,
            ),
        )

    def test_experiment_titanic(self):
        notebook_path = "tasks/rfe-selector/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                min_features=3,
                n_folds=10,
            ),
        )

    def test_boston(self):
        notebook_path = "tasks/rfe-selector/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/boston.csv",
                target="medv",

                min_features=3,
                n_folds=10,
            ),
        )
