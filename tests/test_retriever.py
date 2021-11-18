import os
import unittest
import uuid

import papermill

from tests import datasets, server
import pandas as pd

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

TEMPORARY_DIR = "tmp"
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/simple_q&a.csv"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestRetriever(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.simple_qa()

        os.chdir("tasks/retriever")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_gpu(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "paraphrase_multilingual",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cuda",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)
    
    def test_experiment_cpu(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "paraphrase_multilingual",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)
    
    def test_experiment_top1(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 1,
                similarity_model =  "paraphrase_multilingual",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 questions and top 1 retrieved, total: 2
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)

    def test_experiment_tfidf(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "tf_idf",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)

    def test_experiment_bm25(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "bm25",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)

    def test_experiment_word2vec(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "word2vec",
                proba_column_name = "retriever_score",
                expected_column_name = "",
                identifier_column_name = "",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)

    def test_experiment_eval(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                topn = 2,
                similarity_model =  "paraphrase_multilingual",
                proba_column_name = "retriever_score",
                expected_column_name = "expected_retriever_answer",
                identifier_column_name = "index",
                device = "cpu",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','retriever_score'])
        self.assertEqual(out_data.loc[0, 'retriever_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data, timeout=20)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 4)  # 2 questions and top 2 retrieved, total: 4
        self.assertEqual(len(names), 6) # 1 extra feature (total of 6)