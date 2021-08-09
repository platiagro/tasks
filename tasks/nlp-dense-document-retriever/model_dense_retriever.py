import os
import sys
import torch
from time import time
from pickle import load, dump
from typing import List, Union
import numpy as np
from torch.cuda import is_available as cuda_is_available
from transformers import DPRReader, DPRReaderTokenizer


class EnglishDPRRetriever(object):
    def __init__(self,
                dpr_fn:str,
                tokenizer_fn:str,
                tokenizer_max_len:int,
                ):

        self.dpr = DPRReader.from_pretrained(dpr_fn)
        self.tokenizer_max_len  = tokenizer_max_len
        self.tokenizer  = DPRReaderTokenizer.from_pretrained(tokenizer_fn, max_len=tokenizer_max_len)
        device = 'cuda' if cuda_is_available() else 'cpu'
        self.dpr.to(device)
        self.device = device
    
    def __call__(self,
                questions: str,
                passages: List[str],
                inner_batch_size: int=1,
                top: int=None):
        ''' Both "questions" and "passages" must be in English
            For each question, return the ids of the passages ordered by relevance
            up to top, if specified
        '''
        assert inner_batch_size > 0, f'Passage batch size ({inner_batch_size}) should be at least 1.'
        tokenizer = self.tokenizer
        model = self.dpr
        model.eval()

        if isinstance(questions, str):
            questions = [questions]

        retrieved_ids = []
        retrieved_relevances = []
        with torch.no_grad():
            for question in questions:
                relevances = []
                for i in range(0, len(passages), inner_batch_size):
                    batch_passages = passages[i: i + inner_batch_size]
                    titles = [f'{len(relevances)}'] * len(batch_passages)

                    encoded_inputs = tokenizer(
                        questions=question,
                        titles=titles,
                        texts=batch_passages,
                        return_tensors='pt',
                        padding=True,
                        max_length=self.tokenizer_max_len,
                        truncation=True
                    )
                    
                    
                    for input_key in encoded_inputs:
                        encoded_inputs[input_key] = encoded_inputs[input_key].to(self.device)

                    outputs = model(return_dict=True, **encoded_inputs)
                    outputs = outputs.relevance_logits
                    relevances += outputs
                relevances = [r.item() for r in relevances]
                ids = np.argsort(relevances)[::-1]
                relevances = [relevances[index] for index in ids]
                retrieved_ids.append(ids[:top])
                retrieved_relevances.append(relevances[:top])
        assert len(retrieved_ids) == len(retrieved_relevances)
        retrieved_relevances = np.array(retrieved_relevances)
        retrieved_ids = np.array(retrieved_ids)
        return retrieved_ids, retrieved_relevances