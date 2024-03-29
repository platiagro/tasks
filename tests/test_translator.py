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
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/paracrawl_en_pt_test.csv"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestTranslator(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.paracrawl()

        os.chdir("tasks/translator")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_gpu(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_translated'])
        self.assertEqual(type(out_data.loc[0, 'text_translated']), type("string"))

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
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)
    
    def test_experiment_eval(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "text_english",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_translated'])
        self.assertEqual(type(out_data.loc[0, 'text_translated']), type("string"))

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
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_multiple_translation_step(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "holandês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_translated'])
        self.assertEqual(type(out_data.loc[0, 'text_translated']), type("string"))

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
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_cpu(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cpu",
                batch_size = 4,
            ),
        )

        # Verify output data
        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['text_english', 'text_portuguese', 'text_translated'])
        self.assertEqual(type(out_data.loc[0, 'text_translated']), type("string"))

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
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)
