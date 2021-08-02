import os
import unittest
import uuid

import papermill

from tests import datasets, server

EXPERIMENT_ID = str(uuid.uuid4())
OPERATOR_ID = str(uuid.uuid4())
RUN_ID = str(uuid.uuid4())

class TestQuestionGenerator(unittest.TestCase):

    def setUp(self):
        # Set environment variables needed to run notebooks
        os.environ["EXPERIMENT_ID"] = EXPERIMENT_ID
        os.environ["OPERATOR_ID"] = OPERATOR_ID
        os.environ["RUN_ID"] = RUN_ID

        datasets.reports_contexts_small()

        os.chdir("tasks/nlp-question-generator")

    def tearDown(self):
        datasets.clean()
        os.chdir("../../")

    def test_experiment(self):

        papermill.execute_notebook(
            "Experiment.ipynb",
            "/dev/null",
            parameters=dict(
                dataset="/tmp/data/reports_contexts_small.csv",
                column_context = "context",
                column_question = "question",
                column_answer_start = "answer_start",
                column_answer_end= "answer_end",
                train_from_zero = False,
                train_from_squad = False,
                expand_context = True,
                dev_size_from_data= 0.2,
                test_size_from_dev= 0.5,
                model_name= "unicamp-dl/ptt5-base-portuguese-vocab",
                PREFIX = "gerador_perguntas:",
                num_gen_sentences = 2,
                infer_num_gen_sentences = 10,
                train_batch_size= 2,
                eval_batch_size= 8,
                infer_batch_size = 8,
                no_repeat_ngram_size= 2,
                temperature= 0.7,
                top_p= 0.92,
                source_max_length= 512,
                target_max_length= 100,
                learning_rate= 3.0e-5,
                eps= 1.0e-08,
                seed = 13,
                num_gpus= 1,
                profiler= True,
                max_epochs= 1,
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
        self.assertEqual(len(ndarray[0]), 4)
        self.assertEqual(len(names), 4)