import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestMLPClassifier(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        experiment_path = "mlp-classifier/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                filter_type = "remover",
                model_features = "",

                one_hot_features = "",

                hidden_layer_sizes = 100,
                activation = "relu",
                solver = "adam",
                learning_rate = "constant",
                max_iter = 200,
                shuffle = True,

                method = "predict_proba",
            ),
        )

    def test_experiment_titanic(self):
        experiment_path = "mlp-classifier/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                filter_type = "remover",
                model_features = "",

                one_hot_features = "",

                hidden_layer_sizes = 100,
                activation = "relu",
                solver = "adam",
                learning_rate = "constant",
                max_iter = 200,
                shuffle = True,

                method = "predict_proba",
            ),
        )
