import os
import unittest
import uuid

import papermill

from tests import datasets

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

    def tearDown(self):
        datasets.clean()

    def test_experiment_imdb(self):
        notebook_path = "tasks/nlp-text-pre-processor/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/imdb.csv",
                target = "label",
                language = "english",
                filter_type = "incluir",
                model_features = "text",
                case = "Lower",
                remove_stop_words = True,
                remove_top_words = True,
                top_words_percentage = 0.01,
                stemming = False,
                lemmatization = True,
                remove_punctuation = True,
                remove_line_braks = True,
                remove_accents = True,
                remove_html = True,
                remove_css = True,
            ),
        )
       
       
       
