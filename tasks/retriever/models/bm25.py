# Transformers
from rank_bm25 import BM25Okapi
import numpy as np
import torch.nn as nn

# Typing
from typing import List

# Instantiate class
class BM25(nn.Module):
    """Compute sentence similarity between sentences using the BM25"""
    def __init__(self, **kwargs):

        super(BM25, self).__init__()

        # Model hparams
        self.hparams = {
            'k1': kwargs.get('k1', 2.16),
            'b': kwargs.get('b', 0.61)
        }

    def __name__(self):
        return "BM25"

    def _tokenize(self, corpus: List[str]) -> List[List[str]]:
        return [doc.split(" ") for doc in corpus]

    def _fit(self, sentences: List[str]):
        """Fit the model
            
            Args:
                sentences: List of sentences
        """

        # Fit model
        self.model = BM25Okapi(self._tokenize(sentences),
                               k1=self.hparams['k1'],
                               b=self.hparams['b'])

    def _calculate_similarities(self, hypothesis_sentences: List[str], reference_sentece: str) -> np.array:
        """Calculate similarities between hypothesis and reference sentence"""

        # Fit model
        self._fit(hypothesis_sentences)

        # Tokenize reference
        reference_tokenized = self._tokenize([reference_sentece])[0]

        # Similarities
        similarities = np.array(self.model.get_scores(reference_tokenized))

        return similarities

    def forward(self, batch_hypothesis_sentences: List[List[str]], batch_reference_sentece: List[str]) -> List:
        """Calculate similarity between batch of sentences
            
            >>> batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
            >>> batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']
            >>> model = BM25()
            >>> model(batch_hypothesis_sentences, batch_reference_sentece)
                [[0.0,  0.0], [-1.09861229]]

            Args:
                batch_hypothesis_sentences: Batch of list of hypothesis sentences
                batch_reference_sentece: Batch of reference sentences
            Returns:
                A batch of similarities
        """

        # Assure batches have same length
        assert len(batch_hypothesis_sentences) == len(batch_reference_sentece), "Hypothesis batch and reference batch must have same length."

        # Batch similarities to be calculated
        batch_similarities = []

        for hypothesis_sentences, reference_sentece in zip(batch_hypothesis_sentences, batch_reference_sentece):

            # Calculate reciprocal rank
            similarities = self._calculate_similarities(hypothesis_sentences, reference_sentece)

            # Add to Batch similarities
            batch_similarities.append(similarities)

        return batch_similarities
