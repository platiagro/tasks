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

    def tearDown(self):
        datasets.clean()

    def test_experiment_hymenoptera(self):
        notebook_path = "tasks/cv-fast-autocv/Experiment.ipynb"

        papermill.execute_notebook(
            notebook_path,
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/hymenoptera_data.zip",
                arch_list=["resnet18", "resnet50", "vgg16"],
                aug_polices=["fa_reduced_cifar10", "fa_resnet50_rimagenet", "fa_reduced_svhn"],
                dataset_id="hymenoptera",
                checkpoint_path="/tmp/data/models-output/",
                output_graphs="/tmp/data/eval-images/",
                num_of_classes=2,
                top_predictions=1,

                batch=64,
                epochs=4,
                lr=0.001,
                gamma=0.1,
                step_size=7,
                momentum=0.1,
            ),
        )
