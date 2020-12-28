import string
from collections import defaultdict
from functools import reduce
from re import sub
import nltk
import unidecode
from ftfy import fix_text
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


class Preprocessor:

    def __init__(self,preprocessing_tasks,model_parameters):

        self.preprocessing_tasks = preprocessing_tasks
        self.model_parameters = model_parameters
        self.stopwords = None
        self._external_downloads()
        

    def _external_downloads(self):  
        """Baixando stop words do idioma especificado e a wordnet para lemmatizaton

        """
        if self.preprocessing_tasks['remove_stop_words']:
            # Download stopwords from nltk
            nltk.download('stopwords')

            # Get a list of stopwords for the defined language
            self.stopwords = nltk.corpus.stopwords.words(self.model_parameters['language'])

        if self.preprocessing_tasks['lemmatization']:
            nltk.download('wordnet')


    def _tokenize_text(self, text_list: list = None):
        """Tokenize Text without the hyperparâmeters defined.

        Args:
            text_list (list): a list of texts to be used.

        Returns:
            A list of tokenized text without punctuation.
        """

        tokenize_list = list()
        for text in text_list:
            text = fix_text(text)
            text = sub("<.*?>", " ", text) if self.preprocessing_tasks['remove_html'] else text
            text = sub("{.*?}", " ", text) if self.preprocessing_tasks['remove_css'] else text
            text = unidecode.unidecode(text) if self.preprocessing_tasks['remove_accents'] else text
            text = sub("/\r\n|\n|\r|", "", text) if self.preprocessing_tasks['remove_line_breaks'] else text
            text = (
                sub("[" + string.punctuation + "]", "", text)
                if self.preprocessing_tasks['remove_punctuation']
                else text
            )
            text = sub(" +", " ", text)  # only to avoid multiple spaces
            text = text.split(" ")

            tokenize_list.append(text)

        return tokenize_list


    def _top_tokens_stopwords(self,sentence_list: list):
        """Selects the most relevant stops words of the tokerized texts.

        Args:
            sentence_list (list): list of tokens.
            percentage (float): percentage threshold.
        """
        percentage = self.preprocessing_tasks['top_words_percentage']
        vocabulary = defaultdict(int)

        for sample in sentence_list:
            for token in sample:
                vocabulary[token] += 1

        all_tokens = sorted(vocabulary.items(), key=lambda token: token[1], reverse=True)
        top_tokens = all_tokens[: int(len(all_tokens) * percentage)]

        return [token[0] for token in top_tokens]


    def _remove_specific_tokens(self,sentence_list: list, tokens_to_be_removed: list = None):
        """Removes specific tokens from a token list.

        Args:
            sentence_list (list): list of tokens from which other tokens will be removed.
            tokens_to_be_removed (list): list of tokens that need to be removed.
        """
        sentence_list_ = list()
        sentence_list_ = [x for x in sentence_list if x not in tokens_to_be_removed]

        return sentence_list_


    def _apply_stemming(self,sentence_list: list):
        ps = PorterStemmer()
        sentence_list = [
            [ps.stem(word) for word in token_list] for token_list in sentence_list
        ]
        return sentence_list


    def _apply_lemmatization(self,sentence_list: list):
        lemmatizer = WordNetLemmatizer()
        sentence_list = [
            [lemmatizer.lemmatize(word) for word in token_list]
            for token_list in sentence_list
        ]
        return sentence_list


    def _apply_casing(self,sentence_list: list, case: str):
        if case == "Lower":
            sentence_list = [
                [word.lower() for word in token_list] for token_list in sentence_list
            ]
        elif case == "Upper":
            sentence_list = [
                [word.upper() for word in token_list] for token_list in sentence_list
            ]
        else:
            pass
        return sentence_list


    def _token_restructuring(self,sentence_list: list):
        """Reduce a nested list of tokens to a single list (1D).

        Args:
            sentence_list (list): list to be work on.
        """
        return reduce(lambda x, y: x + y, sentence_list)
    
    def preprocess(self, X):
        """Perform Preprocessing Tasks.

        Args:
            X (list): List of text data to be preprocesed.
        """
        vocab = self._tokenize_text(X)
        top_tokens = self._top_tokens_stopwords(vocab) if self.preprocessing_tasks['remove_top_words'] else None
        vocab = self._remove_specific_tokens(vocab, top_tokens) if self.preprocessing_tasks['remove_top_words'] else vocab
        vocab = self._remove_specific_tokens(vocab, self.stopwords) if self.preprocessing_tasks['remove_stop_words'] else vocab
        vocab = self._apply_stemming(vocab) if self.preprocessing_tasks['stemming'] else vocab
        vocab = self._apply_lemmatization(vocab) if (self.preprocessing_tasks['lemmatization'] and not self.preprocessing_tasks['stemming']) else vocab
        vocab = self._apply_casing(vocab,self.preprocessing_tasks['case'])
        text = [' '.join(tokens) for tokens in vocab]
        return text
