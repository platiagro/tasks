import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestLogisticRegression(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()

        os.chdir("tasks/logistic-regression")

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

                filter_type="remover",
                model_features="",

                ordinal_features="",

                penalty="l2",
                C=1.0,
                fit_intercept=True,
                class_weight=None,
                solver="liblinear",
                max_iter=100,
                multi_class="auto",

                method="predict_proba",
            ),
        )

    def test_experiment_titanic(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                filter_type="remover",
                model_features="",

                ordinal_features="",

                penalty="l2",
                C=1.0,
                fit_intercept=True,
                class_weight=None,
                solver="liblinear",
                max_iter=100,
                multi_class="auto",

                method="predict_proba",
            ),
        )
