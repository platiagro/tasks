# Transformers
from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch.nn as nn
import torch

# Typing
from typing import List

# Instantiate class
class ParaphraseMultilingual(nn.Module):
    """Compute sentence similarity between sentences using the pre-treined paraphrase-xlm-r-multilingual-v1"""
    def __init__(self, **kwargs):

        super(ParaphraseMultilingual, self).__init__()

        # Set model name
        self.model_name = 'sentence-transformers/paraphrase-xlm-r-multilingual-v1'

        # Get hparams
        self.device = kwargs.get('device', torch.device('cpu'))

        # Initialize model
        self._init_model()

    def __name__(self):
        return "ParaphraseMultilingual"

    def _save_embeddings(self, sentences: List[str], embeddings):
        """Save embeddings to internal dict"""

        for i, sentence in enumerate(sentences):
            self._precomputed_embeddings[sentence] = embeddings[i].detach().cpu().numpy()

    def _get_precomputed_embeddings(self, sentences: List[str]):
        """Get precomputed embeddings from internal dict"""

        # Get precomputed embeddings
        embeddings = []
        for sentence in sentences:
            embeddings.append(self._precomputed_embeddings[sentence])

        return torch.tensor(np.array(embeddings)).to(self.device)
    
    def _init_model(self):
        """Initialize model"""

        # Load model
        self.model = AutoModel.from_pretrained(self.model_name).to(self.device)
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # torch cossine similarity
        self.similarity = nn.CosineSimilarity(dim=1, eps=1e-6).to(self.device)

        # Precomputed embeddings
        self._precomputed_embeddings = {}

    def _calculate_mean_pooling(self, model_output, attention_mask):
        """Mean pooling - Take attention mask into account for correct averaging"""

        token_embeddings = model_output[0] # First element of model_output contains all token embeddings

        # Calculate pooling
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def _calculate_similarities(self, hypothesis_sentences: List[str], reference_sentece: str) -> float:
        """Calculate cossine similarities between hypothesis and reference sentence"""

        # Verify if all hypothesis sentences are already precomputed
        precomputed = False
        for hypothesis_sentence in hypothesis_sentences:
            if hypothesis_sentence not in self._precomputed_embeddings.keys():
                precomputed = False
                break
            else:
                precomputed = True

        # Tokenize hypothesis and reference sentences
        if not precomputed:
            encoded_input = self.tokenizer(hypothesis_sentences + [reference_sentece], padding=True, truncation=True, return_tensors='pt')
        else:
            encoded_input = self.tokenizer([reference_sentece], padding=True, truncation=True, return_tensors='pt')

        # Move to device
        encoded_input['attention_mask'] = encoded_input['attention_mask'].to(self.device)
        encoded_input['input_ids'] = encoded_input['input_ids'].to(self.device)

        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Get dense representention embeddings
        embeddings = self._calculate_mean_pooling(model_output, encoded_input['attention_mask'])

        # Get reference sentence embedding and hypothesis sentence embeddings
        if not precomputed:
            hypothesis_embeddings = embeddings[:-1]
            self._save_embeddings(hypothesis_sentences, hypothesis_embeddings)
        else:
            hypothesis_embeddings = self._get_precomputed_embeddings(hypothesis_sentences)

        reference_embedding = embeddings[-1].unsqueeze(0)

        # Similarities
        similarities = self.similarity(hypothesis_embeddings, reference_embedding)

        # Clear memory
        del encoded_input, model_output, embeddings, hypothesis_embeddings, reference_embedding

        return similarities.cpu().detach().numpy()

    def forward(self, batch_hypothesis_sentences: List[List[str]], batch_reference_sentece: List[str]) -> list:
        """Calculate similarity between batch of sentences
            
            >>> batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
            >>> batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']
            >>> model = ParaphraseMultilingual()
            >>> model(batch_hypothesis_sentences, batch_reference_sentece)
                [[0.9557419, 0.46725664], [0.84086704]]

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

# from time import time

# # Sentences we want sentence embeddings for
# batch_hypothesis_sentences = [['Esta é uma sentença de exemplo', 'Todas as sentenças são cobertas'], ['Esta é uma sentença de exemplo 2']]
# batch_reference_sentece = ['Esta sentença é um exemplo', 'Esta é a referencia do exemplo 2']

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# sent_sim = ParaphraseMultilingual(device=device)

# st = time()
# print(sent_sim(batch_hypothesis_sentences, batch_reference_sentece), time()-st)
# st = time()
# print(sent_sim(batch_hypothesis_sentences, batch_reference_sentece), time()-st)
# st = time()
# print(sent_sim(batch_hypothesis_sentences, batch_reference_sentece), time()-st)