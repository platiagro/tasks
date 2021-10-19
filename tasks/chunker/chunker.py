# Typing
from typing import List

# NLTK
from nltk import sent_tokenize
from nltk import word_tokenize
import nltk

# Class
class Chunker(object):
    '''This class gets a context and preprocess into smaller windows of sentences or words'''

    def __init__(self, chunkenizer: str = 'word', chunk_size: int = 96, chunk_overlap: int = 32):
        """
        Initialize the class.

        Params:
            chunkenizer (str): The chunkenizer to use.
            chunk_size (int): The number of chunks to aggregate into a single context.
            chunk_overlap (int): The number of chunks to overlap between contexts.
        """

        # Verify chunkenizer
        assert chunkenizer in ['word', 'sentence'], 'Chunkenizer must be either the str "word" or "sentence"'

        # Set tokenizer
        if chunkenizer == 'word':
            self.chunkenizer = lambda x : x.split()
        else:
            self.chunkenizer = sent_tokenize

        # Set the window size
        self.chunk_size = chunk_size

        # Set the sentence overlap
        self.chunk_overlap = chunk_overlap

        # Dowaload NLTK data
        self._download_data()

    def _download_data(self):
        """
        Download the NLTK data.
        """

        nltk.download('punkt')

    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize a text into chunks of sentences or words.
        """

        # Tokenize the text into chunks
        chunks = self.chunkenizer(text)

        # Set step of chunk
        step = self.chunk_size - self.chunk_overlap

        # Aggregate chuncks
        aggreated_chuncks = []
        for i in range(0, len(chunks), step):

            # Get the chunk
            chunk = chunks[i:i+self.chunk_size]

            # Set chunk context
            chunk_context = ' '.join(chunk)

            # Append the chunk context
            aggreated_chuncks.append(chunk_context)

            # Break if the chunk gets last element
            if i + self.chunk_size == len(chunks):
                break

        return aggreated_chuncks

    def chunkenize(self, contexts: List[str]) -> List[List[str]]:
        """
        Chunkenize contexts for use in the document retriever.
        Ex:
            >>> contexts = ['Eu adoro maracujá. Toda sexta feira eu vou à feira. Como maçã todos os dias. Me chamo Lucas e gosto de barcos. Não vou à praia. Vou à praia.']
            >>> Chunker(chunkenizer='sentence', chunk_size=4, chunk_overlap=2).prepare(contexts)
                [
                    [
                        'Eu adoro maracujá. Toda sexta feira eu vou à feira. Como maçã todos os dias. Me chamo Lucas e gosto de barcos.', 
                        'Como maçã todos os dias. Me chamo Lucas e gosto de barcos. Não vou à praia. Vou à praia.', 
                    ]
                ]

        Params:
            contexts (List[str]): The list of contexts to prepare.

        Returns:
            List[List[str]]: The prepared contexts.
        """

        # Tokenize the contexts into sentences
        tokenized_contexts = [self._tokenize(context) for context in contexts]

        return tokenized_contexts

    def __call__(self, contexts: List[str]) -> List[List[str]]:
        '''Apply prepare method'''

        return self.chunkenize(contexts)
