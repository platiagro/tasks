import logging
import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestMTCNNFaceDetection(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.football_teams()

        os.chdir("tasks/cv-mtcnn-face-detection")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_face_detection_output_image(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/football_teams.zip",
                image_size=64,
                margin=5,
                min_face_size=10,
                factor=0.709,
                keep_all=True,
                device="cpu",
                seed=7,
                inference_batch_size=2,
                input_square_transformation_size=16,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        data = datasets.image_testdata(kind='people', ext='png')
        
        with server.Server() as s:
            response = s.test(data=data, timeout=30)
        
        if 'tensor' in response.keys():
            tensor_shape = response["tensor"]['shape']
            self.assertEqual(tensor_shape, [1, 5]) # 1 output, 5 features

        else: # is a ndarray
            ndarray = response["ndarray"]
            self.assertEqual(len(ndarray[0]), 5) # 5 features
        
        names = response["names"]
        self.assertEqual(len(names), 5) # 5 feature names
