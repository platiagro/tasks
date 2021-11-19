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
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/titanic.csv"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestRandomForestClassifier(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.iris()
        datasets.titanic()

        os.chdir("tasks/random-forest-classifier")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment_iris(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset="/tmp/data/iris.csv",
                target="Species",

                filter_type="remover",
                model_features="",

                one_hot_features="",

                n_estimators=10,
                criterion="gini",
                max_depth=None,
                max_features="auto",
                class_weight=None,

                method="predict_proba",
            ),
        )

        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.iris_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 8)  # 4 features + 1 class + 3 probas
        self.assertEqual(len(names), 8)

    def test_experiment_titanic(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset="/tmp/data/titanic.csv",
                target="Survived",

                filter_type="remover",
                model_features="",

                one_hot_features="",

                random_search = "Não",
                n_estimators=10,
                criterion="gini",
                max_depth=None,
                max_features="auto",
                class_weight=None,

                method="predict_proba",
            ),
        )


        out_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
        self.assertEqual(out_data.columns.tolist(), ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
        self.assertEqual(out_data.loc[0, 'Sex'], "male")


        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.titanic_testdata()
        with server.Server() as s:
            response = s.test(data=data)
        names = response["names"]
        ndarray = response["ndarray"]
        self.assertEqual(len(ndarray[0]), 14)  # 11 features + 1 class + 2 probas
        self.assertEqual(len(names), 14)
