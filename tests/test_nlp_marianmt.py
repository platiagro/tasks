import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestNLPMarianMT(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.paracrawl()

        os.chdir("tasks/nlp-marianmt-translator")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_paracrawl(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset= "/tmp/data/paracrawl_en_pt_test.xlsx",
                target="target",
                prefix = ">>pt_br<<",
                filter_type = "incluir",
                model_features="text",
                model_name = "Helsinki-NLP/opus-mt-en-ROMANCE",
                seed = 7,
                input_max_length = 127,
                output_max_length = 256,
                inference_batch_size = 2
            ),
        )

