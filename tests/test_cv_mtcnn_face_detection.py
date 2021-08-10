import logging
import os
import unittest
import uuid

import papermill
import numpy as np

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

    def test_experiment_face_detection_with_people(self):
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
                input_square_transformation_size=128,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        for ext in ['png', 'jpg']:

            data = datasets.image_testdata(kind='people', ext=ext)

            with server.Server() as s:
                response = s.test(data=data, timeout=10)
            
            if 'tensor' in response.keys():
                tensor_shape = response["tensor"]['shape']

                self.assertEqual(tensor_shape[1], 5) # outputs 5 features

            else: # is a ndarray
                ndarray = response["ndarray"]

                self.assertEqual(len(ndarray[0]), 5) # 5 features
            
            names = response["names"]
            self.assertEqual(len(names), 5) # 5 feature names
    
    def test_experiment_face_detection_without_people(self):
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
                input_square_transformation_size=128,
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        for ext in ['png', 'jpg']:

            data = datasets.image_testdata(kind='objects', ext=ext)

            with server.Server() as s:
                response = s.test(data=data, timeout=10)
            
            if 'tensor' in response.keys():
                tensor_shape = response["tensor"]['shape']

                self.assertEqual(tensor_shape[1], 5) # outputs 5 features

            else: # is a ndarray
                ndarray = response["ndarray"]

                self.assertEqual(len(ndarray[0]), 5) # 5 features
            
            names = response["names"]
            self.assertEqual(len(names), 5) # 5 feature names

    def test_experiment_face_detection_default_params(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/football_teams.zip",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        data = datasets.image_testdata(kind='people', ext='jpg')

        with server.Server() as s:
            response = s.test(data=data, timeout=10)
        
        if 'tensor' in response.keys():
            tensor_shape = response["tensor"]['shape']

            self.assertEqual(tensor_shape[1], 5) # output 5 features

        else: # is a ndarray
            ndarray = response["ndarray"]

            self.assertEqual(len(ndarray[0]), 5) # 5 features
        
        names = response["names"]
        self.assertEqual(len(names), 5) # 5 feature names

    def test_experiment_face_detection_cuda(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/football_teams.zip",
                device="cuda",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        data = datasets.image_testdata(kind='people', ext='jpg')

        with server.Server() as s:
            response = s.test(data=data, timeout=10)
        
        if 'tensor' in response.keys():
            tensor_shape = response["tensor"]['shape']

            self.assertEqual(tensor_shape[1], 5) # output 5 features

        else: # is a ndarray
            ndarray = response["ndarray"]

            self.assertEqual(len(ndarray[0]), 5) # 5 features
        
        names = response["names"]
        self.assertEqual(len(names), 5) # 5 feature names
