import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


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
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "word",
                chunk_size = 5,
                chunk_overlap = 2,
                replicate_data = "sim",
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
        self.assertEqual(len(ndarray), 7)  # 7 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_sentence(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "sentence",
                chunk_size = 2,
                chunk_overlap = 1,
                replicate_data = "sim",
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
        self.assertEqual(len(ndarray), 2)  # 2 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

    def test_experiment_paracrawl_not_replicate_data(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/paracrawl_en_pt_test.csv",
                text_column_name = "text_portuguese",
                output_column_name = "text_chunk",
                chunkenizer =  "word",
                chunk_size = 5,
                chunk_overlap = 2,
                replicate_data = "não",
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
        self.assertEqual(len(ndarray), 2)  # 2 chunked lines of texts
        self.assertEqual(len(names), 3) # 1 extra feature (total of 3)

