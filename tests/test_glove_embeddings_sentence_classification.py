import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestGloveEmbeddingsSentenceClassification(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.imdb()

    def tearDown(self):
        datasets.clean()

    def test_experiment_iris(self):
        experiment_path = "tasks/glove-embeddings-sentence-classification/Experiment.ipynb"

        papermill.execute_notebook(
            experiment_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/imdb.csv",
                target="label",
                language="english",

                train_batch_size=10,
                eval_batch_size=2,
                max_epochs=200,
                accumulate_grad_batches=8,
                learning_rate=0.12,
                seed=7,
                hidden_dim=300,

                filter_type="incluir",
                model_features="text",
            ),
        )
