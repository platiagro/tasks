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


class TestReader(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.simple_qa()

        os.chdir("tasks/reader")

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
                answer_column_name = "answer",
                proba_column_name =  "answer_score",
                expected_column_name = "" ,
                device = "cuda",
                keep_best = "sim",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','answer','answer_score'])
        self.assertEqual(type(out_data.loc[0, 'answer']), str)
        self.assertEqual(out_data.loc[0, 'answer_score'] > 0, True)

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.simple_qa_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 questions and the fact that keep_best is "sim"
        self.assertEqual(len(names), 7) # 2 extra features (total of 7)

    def test_experiment_cpu(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                answer_column_name = "answer",
                proba_column_name =  "answer_score",
                expected_column_name = "" ,
                device = "cpu",
                keep_best = "sim",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','answer','answer_score'])
        self.assertEqual(type(out_data.loc[0, 'answer']), str)
        self.assertEqual(out_data.loc[0, 'answer_score'] > 0, True)

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
        self.assertEqual(len(ndarray), 2)  # 2 questions and the fact that keep_best is "sim"
        self.assertEqual(len(names), 7) # 2 extra features (total of 7)
    
    def test_experiment_eval(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                answer_column_name = "answer",
                proba_column_name =  "answer_score",
                expected_column_name = "expected_answer" ,
                device = "cpu",
                keep_best = "sim",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','answer','answer_score'])
        self.assertEqual(type(out_data.loc[0, 'answer']), str)
        self.assertEqual(out_data.loc[0, 'answer_score'] > 0, True)

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
        self.assertEqual(len(ndarray), 2)  # 2 questions and the fact that keep_best is "sim"
        self.assertEqual(len(names), 7) # 2 extra features (total of 7)
    
    def test_experiment_all_answers(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                context_column_name = "text",
                question_column_name = "question",
                answer_column_name = "answer",
                proba_column_name =  "answer_score",
                expected_column_name = "" ,
                device = "cpu",
                keep_best = "não",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['index','text','question','expected_answer','expected_retriever_answer','answer','answer_score'])
        self.assertEqual(type(out_data.loc[0, 'answer']), str)
        self.assertEqual(out_data.loc[0, 'answer_score'] > 0, True)

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
        self.assertEqual(len(ndarray), 6)  # 2 questions and 3 contexts for each, total: 6
        self.assertEqual(len(names), 7) # 2 extra features (total of 7)