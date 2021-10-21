# Transformers
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import torch.nn as nn

# Typing
from typing import List

# Instantiate class
class TfIDF(nn.Module):
    """Compute sentence similarity between sentences using the TF-IDF from sklearn"""
    def __init__(self, **kwargs):

        super(TfIDF, self).__init__()

        # Get hparams
        self.binary = kwargs.get('binary', True)

        # Initialize model
        self._init_model()
    
    def __name__(self):
        return "TfIDF"
    
    def _init_model(self):
        """Initialize model"""

        # Load model
        self.model = TfidfVectorizer(binary=self.binary)

    def _fit(self, sentences: List[str]):
        """Fit the model
            
            Args:
                sentences: List of sentences
        """

        # Fit model
        self.model.fit(sentences)

    def _calculate_similarities(self, hypothesis_sentences: List[str], reference_sentece: str) -> float:
        """Calculate similarities between hypothesis and reference sentence"""

        # Fit the model in hypothesis sentences
        self._fit(hypothesis_sentences)

        # Retrieve the TF-IDF for hypothesis sentences and reference sentence
        hypothesis_vectors = self.model.transform(hypothesis_sentences)
        reference_vector = self.model.transform([reference_sentece])

        # Similarities
        similarities = np.dot(reference_vector, hypothesis_vectors.T).toarray()[0]

        return similarities

    def forward(self, batch_hypothesis_sentences: List[List[str]], batch_reference_sentece: List[str]) -> float:
        """Calculate similarity between batch of sentences
            
            >>> batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
            >>> batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']
            >>> model = TfIDF()
            >>> model(batch_hypothesis_sentences, batch_reference_sentece)
                [[0.77459667,  0.0], [0.63245553]]

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


# Sentences we want sentence embeddings for
# batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
# batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']

# sent_sim = TfIDF(binary=True)
# print(sent_sim(batch_hypothesis_sentences, batch_reference_sentece))