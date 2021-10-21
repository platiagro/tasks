import os
import torch
import numpy as np
import pandas as pd
from typing import List

# MRR Metric
from mrr import MRR

# Base similarity model
from models.paraphrase_multilingual import ParaphraseMultilingual
from models.bm25 import BM25
from models.tf_idf import TfIDF
from models.word2vec import Word2Vec

# Defining paths
ROOT_DIR = os.path.join(os.getcwd())
DATA_DIR = os.path.join(ROOT_DIR, "data")

MODEL_MAPPING = {
    'paraphrase_multilingual': ParaphraseMultilingual,
    'bm25': BM25,
    'tf_idf': TfIDF,
    'word2vec': Word2Vec,
}


class Retriever(object):
    '''Retriever Caller'''
    def __init__(self, similarity_model, **kwargs):

        # Retrieve kwargs
        self.device = kwargs.get('device', torch.device('cpu'))
        self.similarity_model = similarity_model

    def _batchify_contexts(self, contexts: List[str], batch_size: int):
        '''
        Produces batches of contexts with size batch_size

        Params:
            - contexts: list of contexts
            - batch_size: batch size

        Returns:
            - contexts_batched: list of contexts batches
        '''

        # Batch contexts
        contexts_batched = []
        for i in range(0, 2+len(contexts)//batch_size):

            # Get batch
            batch = contexts[i*batch_size:(i+1)*batch_size]

            if len(batch) == 0: break

            # Save batch
            contexts_batched.append(batch)

        return contexts_batched

    def retrieve_top(self, contexts: list, question: str, topn = 10, context_ids = list, batch_size: int = 32) -> tuple:
        '''
        Retrieve the topn contexts ids and scores that has higher match with
        the given question

        The topn contexts are sorted by the similarity score

        Params:
            - contexts: list of contexts
            - question: question
            - topn: max topn number of contexts to retrieve
            - context_ids: list of context ids to retrieve. Must be passed if qgenerated_df is not passed
            - batch_size: batch size for the similarity model

        Returns:
            - topn_ids: list of topn ids
            - topn_scores: list of topn scores
        '''
        
        # Verify context_ids has same length as contexts
        assert len(context_ids) == len(contexts), 'context_ids must have same length as contexts'

        # Batch contexts
        contexts_batched = self._batchify_contexts(contexts, batch_size)

        # Retrieve the similarity scores
        scores_batched = self.similarity_model(contexts_batched, [question]*len(contexts_batched))

        # Debatch scores
        scores = []
        for batch_score in scores_batched:
            scores += list(batch_score)

        # Transform into numpy array
        scores = np.array(scores)
        
        # Ordenate the scores arguments (highest to lowest)
        scores_args = np.argsort(scores)[::-1]

        # Get topn contexts ids and scores
        topn_contexts_ids = []
        topn_contexts_scores = []

        for arg in scores_args:

            # If found the topn, break
            if len(topn_contexts_ids) >= topn:
                break

            # Get context id
            context_id = context_ids[arg]

            # Add to topn if not already in
            if context_id not in topn_contexts_ids:
                topn_contexts_ids.append(context_id)
                topn_contexts_scores.append(scores[arg])

        # Softmax scores
        topn_contexts_scores = np.exp(topn_contexts_scores) / np.sum(np.exp(topn_contexts_scores))

        return topn_contexts_ids, topn_contexts_scores

    def evaluate(self, batch_hypothesis_ids: List[List[int]], batch_reference_id: List[int], mrr_ranks: List[int] = [10]):
        """
        Calculate the mrr@rank for a batch of batch_hypothesis_ids and contexts.

            Params:
                batch_hypothesis_ids: Batch of hypothesis ids (as numpy array) ordered by its relevance
                batch_reference_id: Batch of reference id (as a integer) of the correct id of response
                mrr_ranks: MRR ranks to calculate

                Example inuputs:
                    >>> batch_hypothesis_ids = [[1, 0, 2], [0, 2, 1], [1, 0, 2]]
                    >>> batch_reference_id = [2, 2, 1]
        
            Returns:
                dict: scores
        """
        
        # Initialize score dict
        scores = {}

        # Iterate over mrr_ranks
        for mrr_rank in mrr_ranks:

            # Initialize calculator
            calculator = MRR(max_rank=mrr_rank)
            
            # Calculate score
            score = calculator(batch_hypothesis_ids, batch_reference_id)

            # Free memory
            del calculator

            # Save score
            scores[f'mrr@{mrr_rank}'] = score

        return scores
