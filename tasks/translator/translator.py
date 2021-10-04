# Transformers
from transformers import MarianMTModel, MarianTokenizer
import nltk

# Torch/Math
import torch.nn as nn
import torch

# Typing
from typing import List

# Log
from tqdm.auto import tqdm

# Graph lib
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path

# Models mapping
MODEL_MAP = {
    # Neolatin
    ('português', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'português'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('espanhol', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'espanhol'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('francês', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'francês'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('italiano', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'italiano'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('catalão', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'catalão'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('romeno', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'romeno'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    ('latim', 'inglês'): 'Helsinki-NLP/opus-mt-ROMANCE-en',
    ('inglês', 'latim'): 'Helsinki-NLP/opus-mt-en-ROMANCE',
    
    # North Europe
    ('alemão', 'holandês'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('holandês', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'frísio'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('frísio', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'africâner'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('africâner', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'dinamarquês'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('dinamarquês', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'islandês'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('islandês', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'norueguês'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('norueguês', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('alemão', 'sueco'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    ('sueco', 'alemão'): 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    
    # German
    ('inglês', 'alemão'): 'Helsinki-NLP/opus-mt-en-de',
    ('alemão', 'inglês'): 'Helsinki-NLP/opus-mt-de-en',
    
    # Chinese
    ('inglês', 'chinês'): 'Helsinki-NLP/opus-mt-en-zh',
    ('chinês', 'inglês'): 'Helsinki-NLP/opus-mt-zh-en',
    
    # Japonese
    ('inglês', 'japonês'): 'Helsinki-NLP/opus-mt-en-jap',
    ('japonês', 'inglês'): 'Helsinki-NLP/opus-mt-jap-en',
    
    # Zulu
    ('inglês', 'zulu'): 'Helsinki-NLP/opus-mt-en-kj',
    ('zulu', 'inglês'): 'Helsinki-NLP/opus-mt-kj-en',
    
    # Híndi
    ('inglês', 'híndi'): 'Helsinki-NLP/opus-mt-en-hi',
    ('híndi', 'inglês'): 'Helsinki-NLP/opus-mt-hi-en',
    
    # Árabe
    ('inglês', 'árabe'): 'Helsinki-NLP/opus-mt-en-ar',
    ('árabe', 'inglês'): 'Helsinki-NLP/opus-mt-ar-en',
}

# Language prefixes
LANGUAGE_PREFIX = {
    'português': '>>pt<<',
    'inglês': '>>en<<',
    'espanhol': '>>es<<',
    'francês': '>>fr<<',
    'italiano': '>>it<<',
    'alemão': '>>de<<',
    'holandês': '>>nl<<',
    'frísio': '>>fy<<',
    'africâner': '>>af<<',
    'dinamarquês': '>>da<<',
    'islandês': '>>is<<',
    'norueguês': '>>no<<',
    'sueco': '>>sv<<',
    'catalão': '>>ca<<',
    'romeno': '>>ro<<',
    'latim': '>>la<<',
    'chinês': '>>cmn<<',
    'japonês': '>>jap<<',
    'zulu': '>>zulu<<',
    'híndi': '>>hi<<',
    'árabe': '>>ar<<',
}

# Translation Directioned Graph
LANGUAGE_GRAPH = nx.DiGraph()
LANGUAGE_GRAPH.add_edges_from(list(MODEL_MAP.keys()))


# Instantiate class
class Translator(nn.Module):
    """Translator class"""
    def __init__(self, device, source_language: str, target_language: str):

        super(Translator, self).__init__()

        # Save source/target languages
        self.translation_pair = (source_language, target_language)
        self.source_language = source_language
        self.target_language = target_language
        
        # Assert language is supported
        assert self._valid_language_path(source_language, target_language), f"Par de tradução ({self.translation_pair}) não suportado."
        
        # Get language pair path
        self.language_pair_path = self._shortest_language_pairs(source_language, target_language)

        # Set model names
        self.model_names = [MODEL_MAP[translation_pair] for translation_pair in self.language_pair_path]

        # Set device
        self.device = device

        # Initialize model
        self._init_model()
        
    def _shortest_language_pairs(self, source_language: str, target_language: str) -> List[tuple]:
        """Shortest list of language pairs that maps source -> target
        
        Params:
            source_language (str): source language
            target_language (str): source language
        
        Returns:
            A list of language pairs
        """
        try:
            # Get language path (source, ..., intermediate_i, ..., target)
            language_path = shortest_path(LANGUAGE_GRAPH, source_language, target_language)

            # Transform in language pairs (bi grams)
            language_pairs_path = list(nltk.bigrams(language_path))
        except:
            language_pairs_path = []
        
        return language_pairs_path
        

    def _valid_language_path(self, source_language: str, target_language: str) -> bool:
        """List of available language pairs
        
        Params:
            source_language (str): source language
            target_language (str): source language
        
        Returns:
            A list of supported language pairs
        """
        
        language_path = self._shortest_language_pairs(source_language, target_language)
        
        if len(language_path) == 0:
            return False
        else:
            return True
    
    def _init_model(self):
        """Initialize model"""

        # Load models
        self.models = [MarianMTModel.from_pretrained(model_name).to(self.device) for model_name in self.model_names]
        
        # Load tokenizer
        self.tokenizers = [MarianTokenizer.from_pretrained(model_name) for model_name in self.model_names]

    def _preprocess_sentence(self, sentence: str, target_language: str) -> str:
        """Preprocess a sentence
        
        Args:
            sentence: Sentence to be preprocessed
            target_language: Target language
        Returns:
            Preprocessed sentence
        """

        # Preprocess (Add mark to specify target langauge)
        return LANGUAGE_PREFIX[target_language] + ' ' + sentence

    def translate(self, batch_sentence: List[str], batch_size: int = 16, debug=False) -> List[str]:
        """
        Translate a batch of sentences into especified language
        
        Params:
            batch_sentence (List[str]): Batch of sentences to be translated
            batch_size (int): Batch size

        Returns:
            A list of translated sentences
        """
        
        # Iterate over each step of translation [(sorce, lang_1), ..., (lang_n-1, target)]
        for step_id, language_pair in enumerate(self.language_pair_path):
            
            # Get target language
            target_language = language_pair[1]

            # Preprocess sentences
            batch_sentence = [self._preprocess_sentence(sentence, target_language) for sentence in batch_sentence]

            # Output batch
            translated_batch = []

            # Log information
            if debug:
                pbar = tqdm(range(0, 2+len(batch_sentence)//batch_size), leave=False)
                pbar.set_description(f'Translating batch {language_pair}')
            else:
                pbar = range(0, 2+len(batch_sentence)//batch_size)

            # Iterate over batch size
            for batch_id in pbar:

                # Get sentences
                sentences = batch_sentence[batch_id*batch_size: (batch_id+1)*batch_size]

                if len(sentences) == 0: break

                # Tokenize batch
                encoded_input = self.tokenizers[step_id](sentences, padding=True, truncation=True, return_tensors='pt')

                # Move to device
                encoded_input['attention_mask'] = encoded_input['attention_mask'].to(self.device)
                encoded_input['input_ids'] = encoded_input['input_ids'].to(self.device)

                # Compute token embeddings
                with torch.no_grad():
                    model_output = self.models[step_id].generate(**encoded_input)

                translated_batch += [self.tokenizers[step_id].decode(translation, skip_special_tokens=True) for translation in model_output]

                # Clear memory
                del encoded_input, model_output
            
            # Update batch_sentence
            batch_sentence = translated_batch

        return translated_batch

    def forward(self, batch_sentence: List[str], batch_size: int = 16, debug=False) -> List[str]:
        """
        Translate a batch of sentences into especified language
        
        Params:
            batch_sentence (List[str]): Batch of sentences to be translated
            batch_size (int): Batch size
            debug (bool): Shows debug information

        Returns:
            A list of translated sentences
        """

        return self.translate(batch_sentence, batch_size=batch_size, debug=debug)