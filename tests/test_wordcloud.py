import os
import unittest
import uuid

import papermill
import pandas as pd
import numpy as np
from base64 import b64encode
import io
from PIL import Image

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

TEMPORARY_DIR = "tmp"
LOCAL_TEST_DATA_PATH = f"/{TEMPORARY_DIR}/data/landspaces.csv"
LOCAL_OUTPUT_DATA_PATH = f"/{TEMPORARY_DIR}/data/"
EXPERIMENT_NOTEBOOK = "Experiment.ipynb"
DEPLOYMENT_NOTEBOOK = "Deployment.ipynb"
DEV_DIR = "/dev/null"


class TestWordCloud(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.landspaces()

        os.chdir("tasks/wordcloud")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    """
    def test_experiment_default_parameters(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                background_color="white",
                max_words=200,
                stopwords="",
                max_font_size=None,
                width=1920,
                height=1080
            ),
        )

        # Verify output data
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "wordcloud_img_0.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )


        data = datasets.landspaces_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        images = []
        for raw_str in response["ndarray"]:
            raw_bytes = bytes(raw_str, "latin1")
            img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
            images.append(img)
            
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0].size, (1920, 1080))

    def test_experiment_custom_stopwords(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                background_color="black",
                max_words=200,
                stopwords="Activation,Landscapes,Topological,Summary,Neural,Network",
                max_font_size=None,
                width=1920,
                height=1080
            ),
        )

        # Verify output data
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "wordcloud_img_0.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )


        data = datasets.landspaces_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        images = []
        for raw_str in response["ndarray"]:
            raw_bytes = bytes(raw_str, "latin1")
            img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
            images.append(img)
            
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0].size, (1920, 1080))
    """

    def test_experiment_csv_input_deployment(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                background_color="black",
                max_words=200,
                stopwords="",
                max_font_size=None,
                width=1920,
                height=1080
            ),
        )

        # Verify output data
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "wordcloud_img_0.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )


        data = datasets.landspaces_test_data()
        str_data = data['strData']
        df = pd.DataFrame({"filename": ["test_df"], "text": [str_data]})
        buff = io.BytesIO()
        df.to_json(buff)
        data = {
            'binData': buff.getvalue()
        }

        with server.Server() as s:
            response = s.test(data=data)

        images = []
        for raw_str in response["ndarray"]:
            raw_bytes = bytes(raw_str, "latin1")
            img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
            images.append(img)
            
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0].size, (1920, 1080))
    """

        self.assertEqual(type(response), str)
        self.assertTrue("topological" in response)

    def test_experiment_papers_text_filter(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                extract = "text",
                text_filter_begin = "abstract",
                text_filter_end = "introduction",
                initial_page = None,
                final_page = None,
            ),
        )

        # Verify output data
        
        out_data = pd.read_csv(LOCAL_OUTPUT_DATA_PATH + "results.csv")
        self.assertEqual(out_data.columns.tolist(), ['filename', 'text'])

        self.assertTrue("investigation of the graph" in out_data.loc[0, 'text'])
        self.assertTrue("This paper implements" in out_data.loc[2, 'text'])

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.pdf_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        self.assertEqual(type(response), str)
        self.assertTrue("abstract" in response)
    
    def test_experiment_papers_text_pages(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                extract = "text",
                text_filter_begin = "",
                text_filter_end = "",
                initial_page = 2,
                final_page = 3,
            ),
        )

        # Verify output data
        
        out_data = pd.read_csv(LOCAL_OUTPUT_DATA_PATH + "results.csv")
        self.assertEqual(out_data.columns.tolist(), ['filename', 'text'])

        
        #self.assertEqual("" ,out_data.loc[0, 'text'])
        self.assertTrue("Periodic" in out_data.loc[0, 'text'])

        #self.assertEqual("" ,out_data.loc[2, 'text'])
        self.assertTrue("Greenshields" in out_data.loc[2, 'text'])


        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )
        data = datasets.pdf_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        self.assertEqual(type(response), str)
        self.assertTrue("simplicial homology" in response)
    
    def test_experiment_papers_figures(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                extract = "figures",
                text_filter_begin = "",
                text_filter_end = "",
                initial_page = None,
                final_page = None,
            ),
        )

        # Verify output data
        
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "doc1_fig1.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.pdf_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        images = []
        for raw_str in response["ndarray"]:
            raw_bytes = bytes(raw_str, "latin1")
            img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
            images.append(img)


        self.assertEqual(images[0].size, (10000, 4000))
        self.assertEqual(images[2].size, (1252, 648))
        self.assertEqual(len(images), 7)

    def test_experiment_papers_prints(self):
        papermill.execute_notebook(
            EXPERIMENT_NOTEBOOK,
            DEV_DIR,
            parameters=dict(
                dataset=LOCAL_TEST_DATA_PATH,
                extract = "prints",
                text_filter_begin = "",
                text_filter_end = "",
                initial_page = None,
                final_page = None,
            ),
        )

        # Verify output data
        
        out_data = Image.open(LOCAL_OUTPUT_DATA_PATH + "doc1_page1.png")
        self.assertEqual(out_data.format, "PNG")

        # Deployment pipeline
        papermill.execute_notebook(
            DEPLOYMENT_NOTEBOOK,
            DEV_DIR,
        )

        data = datasets.pdf_testdata()
        with server.Server() as s:
            response = s.test(data=data)

        images = []
        for raw_str in response["ndarray"]:
            raw_bytes = bytes(raw_str, "latin1")
            img = Image.open(io.BytesIO(raw_bytes), formats=["JPEG"])
            images.append(img)

        self.assertEqual(images[0].size, (1224, 1584))
        self.assertEqual(images[2].size, (1224, 1584))
        self.assertEqual(len(images), 6)

"""