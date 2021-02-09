import os
import unittest
import uuid

import papermill

from tests import datasets

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())


class TestFineTuningAutoAugment(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.hymenoptera()

        os.chdir("tasks/cv-fast-autocv")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_hymenoptera(self):
        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hymenoptera_data.zip",
                arch_list=["resnet18", "resnet50", "vgg16"],
                aug_polices=["fa_reduced_cifar10", "fa_resnet50_rimagenet", "fa_reduced_svhn"],
                dataset_id="hymenoptera",
                checkpoint_path="/tmp/data/models-output/",
                output_graphs="/tmp/data/eval-images/",
                top_predictions=1,

                batch = 12,
                epochs = 10,
                lr = 0.001,
                gamma = 0.1,
                step_size = 7,
                momentum = 0.1,
            ),
        )
