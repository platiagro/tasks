import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

class TestSparseDocumentRetriever(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.reports_contexts_small()

        os.chdir("tasks/nlp-document-reader")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment(self):

        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/reports_contexts_small.csv",
                question = "Qual é o melhor herbicida para erva da ninha ?",
                top = 10,
                column_retriever_score = "retriever_score",
                column_reader_score = "reader_score",
                retriever_reader_pipeline = False,
                reader_score_weight = 0.8,
                remove_no_answer_found = True,
                ntops_overall = 5,
                column_context = "context",
                column_doc_id = "doc_id",
                column_answer_start = "answer_start",
                column_answer_end= "answer_end",
                train_from_zero = False,
                train_from_squad = False,
                dev_size_from_data= 0.2,
                test_size_from_dev= 0.5,
                batch_dataset_preparation = 30 ,
                model_name= "neuralmind/bert-large-portuguese-cased",
                train_batch_size= 2,
                eval_batch_size= 2,
                max_length= 384,
                doc_stride= 128,
                learning_rate= 3.0e-5,
                eps= 1.0e-08,
                seed = 13,
                num_gpus= 0,
                profiler= True,
                max_epochs= 2,
                accumulate_grad_batches= 16,
                check_val_every_n_epoch= 1,
                progress_bar_refresh_rate= 1,
                gradient_clip_val= 1.0,
                fast_dev_run= False,
                monitor= 'avg_train_loss',
                min_delta= 0.01,
                patience= 1,
                verbose= False,
                mode= 'min'
            ),
        )

        papermill.execute_notebook(
            "Deployment.ipynb",
            "/dev/null",
        )

        data = datasets.report_contexts_test_data()

        with server.Server() as s:
            response = s.test(data=data)

        names = response["names"]    
        ndarray = response["ndarray"]
        print(ndarray[0])
        self.assertEqual(len(ndarray[0]), 5)
        self.assertEqual(len(names), 5)