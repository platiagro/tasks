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

# LANGUAGE/MODEL CONFIGURATIONS #

# Models (https://huggingface.co/models)
MODELS = {
    'ROMANCE-en': 'Helsinki-NLP/opus-mt-ROMANCE-en',
    'en-ROMANCE': 'Helsinki-NLP/opus-mt-en-ROMANCE',
    'NORTH_EU-NORTH_EU': 'Helsinki-NLP/opus-mt-NORTH_EU-NORTH_EU',
    'en-de': 'Helsinki-NLP/opus-mt-en-de',
    'de-en': 'Helsinki-NLP/opus-mt-de-en',
    'en-zh': 'Helsinki-NLP/opus-mt-en-zh',
    'zh-en': 'Helsinki-NLP/opus-mt-zh-en',
    'en-jap': 'Helsinki-NLP/opus-mt-en-jap',
    'jap-en': 'Helsinki-NLP/opus-mt-jap-en',
    'en-hi': 'Helsinki-NLP/opus-mt-en-hi',
    'hi-en': 'Helsinki-NLP/opus-mt-hi-en',
    'en-ar': 'Helsinki-NLP/opus-mt-en-ar',
    'ar-en': 'Helsinki-NLP/opus-mt-ar-en',
    'en-kj': 'Helsinki-NLP/opus-mt-en-kj',
    'kj-en': 'Helsinki-NLP/opus-mt-kj-en',
}

# Languages
LANG_PT = {'language': 'português','code': 'pt',}
LANG_EN = {'language': 'inglês','code': 'en',}
LANG_ES = {'language': 'espanhol','code': 'es',}
LANG_FR = {'language': 'francês','code': 'fr',}
LANG_IT = {'language': 'italiano','code': 'it',}
LANG_RO = {'language': 'romeno','code': 'ro',}
LANG_DE = {'language': 'alemão','code': 'de',}
LANG_LA = {'language': 'latim','code': 'la',}
LANG_NL = {'language': 'holandês','code': 'nl',}
LANG_FY = {'language': 'frísio','code': 'fy',}
LANG_AF = {'language': 'africâner','code': 'af',}
LANG_DA = {'language': 'dinamarquês','code': 'da'}
LANG_IS = {'language': 'islandês','code': 'is',}
LANG_NO = {'language': 'norueguês','code': 'no',}
LANG_SV = {'language': 'sueco','code': 'sv',}
LANG_CA = {'language': 'catalão','code': 'ca',}
LANG_CMN = {'language': 'chinês','code': 'cmn',}
LANG_JAP = {'language': 'japonês','code': 'jap',}
LANG_KJ = {'language': 'zulu','code': 'kj',}
LANG_HI = {'language': 'híndi','code': 'hi',}
LANG_AR = {'language': 'árabe','code': 'ar',}

# Models mapping
MODEL_MAP = {
    # Neolatin
    (LANG_PT['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_PT['language']): MODELS['en-ROMANCE'],
    (LANG_ES['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_ES['language']): MODELS['en-ROMANCE'],
    (LANG_FR['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_FR['language']): MODELS['en-ROMANCE'],
    (LANG_IT['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_IT['language']): MODELS['en-ROMANCE'],
    (LANG_CA['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_CA['language']): MODELS['en-ROMANCE'],
    (LANG_RO['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_RO['language']): MODELS['en-ROMANCE'],
    (LANG_LA['language'], LANG_EN['language']): MODELS['ROMANCE-en'],
    (LANG_EN['language'], LANG_LA['language']): MODELS['en-ROMANCE'],
    
    # North Europe
    (LANG_DE['language'], LANG_NL['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_NL['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_FY['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_FY['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_AF['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_AF['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_DA['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DA['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_IS['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_IS['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_NO['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_NO['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_DE['language'], LANG_SV['language']): MODELS['NORTH_EU-NORTH_EU'],
    (LANG_SV['language'], LANG_DE['language']): MODELS['NORTH_EU-NORTH_EU'],
    
    # German
    (LANG_EN['language'], LANG_DE['language']): MODELS['en-de'],
    (LANG_DE['language'], LANG_EN['language']): MODELS['de-en'],
    
    # Chinese
    (LANG_EN['language'], LANG_CMN['language']): MODELS['en-zh'],
    (LANG_CMN['language'], LANG_EN['language']): MODELS['zh-en'],
    
    # Japonese
    (LANG_EN['language'], LANG_JAP['language']): MODELS['en-jap'],
    (LANG_JAP['language'], LANG_EN['language']): MODELS['jap-en'],
    
    # Zulu
    (LANG_EN['language'], LANG_KJ['language']): MODELS['en-kj'],
    (LANG_KJ['language'], LANG_EN['language']): MODELS['kj-en'],
    
    # Híndi
    (LANG_EN['language'], LANG_HI['language']): MODELS['en-hi'],
    (LANG_HI['language'], LANG_EN['language']): MODELS['hi-en'],
    
    # Árabe
    (LANG_EN['language'], LANG_AR['language']): MODELS['en-ar'],
    (LANG_AR['language'], LANG_EN['language']): MODELS['ar-en'],
}

# Language prefixes
LANGUAGE_PREFIX = {
    LANG_PT['language']: '>>'+LANG_PT['code']+'<<',
    LANG_EN['language']: '>>'+LANG_EN['code']+'<<',
    LANG_ES['language']: '>>'+LANG_ES['code']+'<<',
    LANG_FR['language']: '>>'+LANG_FR['code']+'<<',
    LANG_IT['language']: '>>'+LANG_IT['code']+'<<',
    LANG_DE['language']: '>>'+LANG_DE['code']+'<<',
    LANG_NL['language']: '>>'+LANG_NL['code']+'<<',
    LANG_FY['language']: '>>'+LANG_FY['code']+'<<',
    LANG_AF['language']: '>>'+LANG_AF['code']+'<<',
    LANG_DA['language']: '>>'+LANG_DA['code']+'<<',
    LANG_IS['language']: '>>'+LANG_IS['code']+'<<',
    LANG_NO['language']: '>>'+LANG_NO['code']+'<<',
    LANG_SV['language']: '>>'+LANG_SV['code']+'<<',
    LANG_CA['language']: '>>'+LANG_CA['code']+'<<',
    LANG_RO['language']: '>>'+LANG_RO['code']+'<<',
    LANG_LA['language']: '>>'+LANG_LA['code']+'<<',
    LANG_CMN['language']: '>>'+LANG_CMN['code']+'<<',
    LANG_JAP['language']: '>>'+LANG_JAP['code']+'<<',
    LANG_KJ['language']: '>>'+LANG_KJ['code']+'<<',
    LANG_HI['language']: '>>'+LANG_HI['code']+'<<',
    LANG_AR['language']: '>>'+LANG_AR['code']+'<<',
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