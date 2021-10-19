import os
import unittest
import uuid

import papermill
import pandas as pd

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

TEMPORARY_DIR = "tmp"
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/paracrawl_en_pt_test.csv"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestChunker(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.paracrawl()

        os.chdir("tasks/chunker")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_paracrawl_word(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "word",
                chunk_size = 5,
                chunk_overlap = 2,
                replicate_data = "sim",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_chunk'])
        self.assertEqual(out_data.loc[0, 'text_chunk'], "Deste modo, a vida civil")
        self.assertEqual(out_data.loc[1, 'text_chunk'], "vida civil de uma nação")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 7)  # 7 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_sentence(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "sentence",
                chunk_size = 2,
                chunk_overlap = 1,
                replicate_data = "sim",
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_chunk'])
        self.assertEqual(out_data.loc[0, 'text_chunk'].strip(), "Deste modo, a vida civil de uma nação amadurece, fazendo com que todos os cidadãos gozem dos frutos da tolerância genuína e do respeito mútuo.")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_not_replicate_data(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "word",
                chunk_size = 12,
                chunk_overlap = 2,
                replicate_data = "não",
            ),
        )


        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_chunk'])
        self.assertEqual(out_data.loc[0, 'text_chunk'], "['Deste modo, a vida civil de uma nação amadurece, fazendo com que', 'com que todos os cidadãos gozem dos frutos da tolerância genuína e', 'genuína e do respeito mútuo.']")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

