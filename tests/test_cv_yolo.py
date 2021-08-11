import os
import unittest
import uuid

import papermill

from tests import datasets, server
import numpy as np
import logging

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

EXPERIMENT_DATASET = "/tmp/data/yolo.zip"

class TestCVYOLO(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.yolo()

        os.chdir("tasks/cv-yolo")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")
    
    def test_yolo_default_params(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset=EXPERIMENT_DATASET,
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

                self.assertEqual(tensor_shape[1], 6) # outputs 6 features

            else: # is a ndarray
                ndarray = response["ndarray"]

                self.assertEqual(len(ndarray[0]), 6) # 6 features
            
            names = response["names"]
            self.assertEqual(len(names), 6) # 6 feature names
    
    def test_yolo_tiny_portuguese(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset=EXPERIMENT_DATASET,
                language="português",
                yolo_weight_type="tiny",
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

                self.assertEqual(tensor_shape[1], 6) # outputs 6 features

            else: # is a ndarray
                ndarray = response["ndarray"]

                self.assertEqual(len(ndarray[0]), 6) # 6 features
            
            names = response["names"]
            self.assertEqual(len(names), 6) # 6 feature names

    def test_yolo_empty_output(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset=EXPERIMENT_DATASET,
                score_threshold=0.9999,
                iou_threshold=0.9999,
                yolo_weight_type="tiny",
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )


        data = datasets.image_testdata(kind='text', ext='png')

        with server.Server() as s:
            response = s.test(data=data, timeout=10)
        
        if 'tensor' in response.keys():
            tensor_shape = response["tensor"]['shape']

            self.assertEqual(tensor_shape[1], 6) # outputs 6 features

        else: # is a ndarray
            ndarray = response["ndarray"]

            self.assertEqual(len(ndarray[0]), 6) # 6 features
        
        names = response["names"]
        self.assertEqual(len(names), 6) # 6 feature names
