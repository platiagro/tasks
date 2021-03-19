import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestNLPTextPreProcessor(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.imdb()

        os.chdir("tasks/nlp-text-pre-processor")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_imdb(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/imdb.csv",
                target="label",
                language="english",
                filter_type="incluir",
                model_features="text",
                case="Lower",
                remove_stop_words=True,
                remove_top_words=True,
                top_words_percentage=0.01,
                stemming=False,
                lemmatization=True,
                remove_punctuation=True,
                remove_line_braks=True,
                remove_accents=True,
                remove_html=True,
                remove_css=True,
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
        self.assertEqual(len(ndarray[0]), 1)  # 1 feature
        self.assertEqual(len(names), 1)
