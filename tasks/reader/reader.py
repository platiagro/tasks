# Transformers
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import numpy as np
import torch.nn as nn
import torch

# Typing
from typing import List

# Pandas
import pandas as pd

# Abstract class for model
class Bert(nn.Module):
    
    def __init__(self):

        super(Bert, self).__init__()

        # Model variable
        self.model = None

# Instantiate class
class Reader(nn.Module):
    """Reader model for question answering from a given set of contexts"""
    def __init__(self, **kwargs):

        super(Reader, self).__init__()

        # Get kwargs
        checkpoint_path = kwargs.get('checkpoint_path', None)

        # Set device
        self.device = kwargs.get('device', torch.device('cpu'))

        # Initialize model
        self._init_model(checkpoint_path)
    
    def _init_model(self, checkpoint_path: str = None):
        """Initialize model"""

        # Load model
        self.bert = Bert()
        self.bert.model = AutoModelForQuestionAnswering.from_pretrained("pierreguillou/bert-large-cased-squad-v1.1-portuguese").to(self.device)

        # Override with checkpoint
        if checkpoint_path:
            checkpoint = torch.load(checkpoint_path)
            self.bert.load_state_dict(checkpoint['state_dict'])
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("pierreguillou/bert-large-cased-squad-v1.1-portuguese")

        # Model prediction pipeline
        device_id = -1 if self.device == torch.device('cpu') else 0
        self.pipeline = pipeline("question-answering", model=self.bert.model, tokenizer=self.tokenizer, device=device_id)

    def read(self, batch_questions: List[str], contexts: List[str]) -> tuple:
        """
        Given a list of questions and a list of context, find the question's answers.
        
            Returns:
                tuple: (answers, answer_prob)
        """

        # Get answers
        batch_answers = {question: [] for question in batch_questions}
        batch_answers_prob = {question: [] for question in batch_questions}

        for context in contexts:
            
            # Get answer
            pipeline_answers = self.pipeline(question=batch_questions, context=context)

            if isinstance(pipeline_answers, dict):
                pipeline_answers = [pipeline_answers]

            # For each question
            for question, pipeline_answer in zip(batch_questions, pipeline_answers):

                # Append
                batch_answers[question].append(pipeline_answer['answer'])
                batch_answers_prob[question].append(pipeline_answer['score'])
        
        # Retrieve best answers
        answers = []
        answers_prob = []
        answers_arg = []

        for question in batch_questions:

            # Get best answer arg
            best_answer_arg = np.argmax(batch_answers_prob[question])

            # Append
            answers.append(batch_answers[question][best_answer_arg])
            answers_prob.append(batch_answers_prob[question][best_answer_arg])
            answers_arg.append(best_answer_arg)

        return answers, answers_prob, answers_arg

    def forward(self, batch_questions: List[str], contexts: List[str]) -> tuple:
        """Apply read method to a batch of contexts"""

        return self.read(batch_questions, contexts)
