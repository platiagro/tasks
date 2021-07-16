import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestDenseDocumentRetriever(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.reports_contexts_small()

        os.chdir("tasks/nlp-dense-document-retriever")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_report_contexts(self):

        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/reports_contexts_small.csv",
                column = "context",
                question = "What is the best weed herbicide?",
                top = 5,
                inner_batch_size = 5,
                tokenizer_fn = "facebook/dpr-reader-single-nq-base",
                tokenizer_max_len = 512,
                dpr_fn = "facebook/dpr-reader-single-nq-base",

            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.report_contexts_test_data()
        print("######################################################")
        print(data)
        with server.Server() as s:
            print("######################################################")
            print("s")
            response = s.test(data=data,timeout=10)
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 4)  # 1 feature