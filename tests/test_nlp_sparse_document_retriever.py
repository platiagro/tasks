import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestSparseDocumentRetriever(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.report_contexts()

        os.chdir("tasks/nlp-sparse-document-retriever")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_report_contexts(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/reports_contexts.csv",
                column = "context",
                question = "Qual é o melhor herbicida para erva da ninha ?",
                retriever_type = "tfidf",
                bm25_k1 = 2,
                bm25_b = 0.75 ,
                top = 10,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.report_contexts_test_data()
        with server.Server() as s:
            response = s.test(data=data)
        ndarray = response["ndarray"]
        #self.assertEqual(len(ndarray[0]), 1)  # 1 feature
