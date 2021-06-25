import os
import unittest
import uuid

import papermill

from tests import datasets, server

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
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text = "text_english",
                target = "text_portuguese",
                input_language =  "Inglês",
                target_language = "Português" ,
                seed = 42,
                max_length = 256,
                inference_batch_size = 2
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)
        ndarray = response["ndarray"]
        #self.assertEqual(len(ndarray[0]), 1)  # 1 feature
