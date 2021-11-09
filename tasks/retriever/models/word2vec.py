# Transformers
import spacy
import numpy as np
import torch.nn as nn

# Typing
from typing import List

# Instantiate class
class Word2Vec(nn.Module):
    """Compute sentence similarity between sentences using the spacy Word2Vec representation"""
    def __init__(self, **kwargs):

        super(Word2Vec, self).__init__()

        # Get hparams
        model_size = kwargs.get("model_size", "lg")

        # Assure model size is valid
        assert model_size in ["sm", "md", "lg"], "Model size must be either 'sm', 'md' or 'lg'."

        # Save model name
        self.model_name = f'pt_core_news_{model_size}'

        # Initialize model
        self._init_model()

    def __name__(self):
        return "Word2Vec"
    
    def _init_model(self):
        """Initialize model"""

        # Load model
        self.model = spacy.load(self.model_name)

        # Precomputed docs
        self._precomputed_docs = {}

    def _save_docs(self, sentences: List[str], docs):
        """Save docs to internal dict"""

        for i, sentence in enumerate(sentences):
            self._precomputed_docs[sentence] = docs[i]

    def _get_precomputed_docs(self, sentences: List[str]):
        """Get precomputed docs from internal dict"""

        # Get precomputed embeddings
        docs = []
        for sentence in sentences:
            docs.append(self._precomputed_docs[sentence])

        return docs

    def _calculate_similarities(self, hypothesis_sentences: List[str], reference_sentece: str) -> np.array:
        """Calculate similarities between hypothesis and reference sentence"""

        # Verify if all hypothesis sentences are already precomputed
        precomputed = False
        for hypothesis_sentence in hypothesis_sentences:
            if hypothesis_sentence not in self._precomputed_docs.keys():
                precomputed = False
                break
            else:
                precomputed = True
        
        # Retrieve the document representations for hypothesis sentences and reference sentence
        if not precomputed:
            hypothesis_docs = [self.model(hypothesis_sentence) for hypothesis_sentence in hypothesis_sentences]
            self._save_docs(hypothesis_sentences, hypothesis_docs)
        else:
            hypothesis_docs = self._get_precomputed_docs(hypothesis_sentences)
            
        reference_doc = self.model(reference_sentece)

        # Similarities
        similarities = np.array([reference_doc.similarity(hypothesis_doc) for hypothesis_doc in hypothesis_docs])

        return similarities

    def forward(self, batch_hypothesis_sentences: List[List[str]], batch_reference_sentece: List[str]) -> List:
        """Calculate similarity between batch of sentences
            
            >>> batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
            >>> batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']
            >>> model = Word2Vec()
            >>> model(batch_hypothesis_sentences, batch_reference_sentece)
                [[0.79393229,  0.15021144], [0.86997343]]

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
            
            # Calculate similarity
            similarities = self._calculate_similarities(hypothesis_sentences, reference_sentece)

            # Add to Batch similarities
            batch_similarities.append(similarities)

        return batch_similarities
