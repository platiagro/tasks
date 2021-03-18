import os
import unittest
import uuid

import papermill

from tests import datasets, server

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
        os.chdir("../../")

    def test_experiment_imdb(self):
        os.chdir("tasks/nlp-glove-embeddings-sentence-classification")

        papermill.execute_notebook(
            "Experiment.ipynb",
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

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.imdb_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 1)  # 1 features
        self.assertEqual(len(names), 1)
