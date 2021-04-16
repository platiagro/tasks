import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestAutoKerasAutoCV(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.beans_disease()

        os.chdir("tasks/cv-autokeras-autocv-image-classification")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_beans_disease(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset = "/tmp/data/beans_disease.zip",
                num_epochs = 2,
                trials = 3,
                batch_size = 2,
                target_size = 256,

                brightness_range = None,
                channel_shift_range = 0.0,
                cval = 0.0,
                data_format = "channels_last",
                dtype = 'float32',
                featurewise_center = False,
                featurewise_std_normalization = False,
                fill_mode = 'nearest',
                horizontal_flip = False,
                preprocessing_function = None,
                rescale = 1./255,
                rotation_range = 0,
                samplewise_center = False,
                samplewise_std_normalization = False,
                shear_range = 0.0,
                vertical_flip = False,
                zca_whitening = False,
                zca_epsilon = 1e-06,
                zoom_range = 0.0,
                height_shift_range = 0.0,
                width_shift_range = 0.0
            ),
        )
