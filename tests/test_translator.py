import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


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

    def test_experiment_paracrawl_gpu(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)
    
    def test_experiment_paracrawl_eval(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "text_english",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_multiple_translation_step(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "holandês" ,
                device = "cuda",
                batch_size = 4,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_cpu(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_translated",
                expected_column_name = "",
                source_language =  "português",
                target_language = "inglês" ,
                device = "cpu",
                batch_size = 4,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )
        data = datasets.paracrawl_test_data()
        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray), 2)  # 2 translated texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)
