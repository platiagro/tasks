from platiagro import download_artifact
from gensim.models import KeyedVectors
from sys import platform
from platiagro.io import unzip_to_folder
import torch

class GloveEmbeddings(object):
    """
    Classes reponsável por criar a matriz de glove embeddings com os textos fornecidos
    """
    def __init__(self,glove_dim:int,glove_weights_file_name:str,device:str):
        super(GloveEmbeddings , self).__init__()
        
        self.device = device
        self.glove_dim = glove_dim
        self.glove_weights_file_name = glove_weights_file_name
        self.glove_path  = None
        self.glove_infos = None
        
        self._extract_glove_properties()
        
    def _set_glove_path(self):
        """
        Configura o caminho dos pesos para a PLATIA dependendo se é um arquivo .zip ou .txt
        """
        
        if ".zip" not in self.glove_weights_file_name and ".txt" not in self.glove_weights_file_name:
            raise TypeError("Os pesos Glove devem estar em um arquivo .txt ou comprimidos em um arquivo .zip")
        
        if ".zip" in self.glove_weights_file_name:
            unzip_to_folder(f"./{self.glove_weights_file_name}","./")
            name_without_extension = self.glove_weights_file_name.split(".")[0]
            self.glove_path = f"./{name_without_extension}.txt"
            self.glove_weights_file_name = f"{name_without_extension}.txt"
        
        if ".txt" in self.glove_weights_file_name:
            self.glove_path = f"./{self.glove_weights_file_name}"
            

    def _load_glove_vector(self):
        """
        Carrega os vetores glove no formato word2vec
        """
        self._set_glove_path()
        try: 
            glove = KeyedVectors.load_word2vec_format(self.glove_path,no_header=False)
        except ValueError:
            glove = KeyedVectors.load_word2vec_format(self.glove_path,no_header=True)
        
        return glove
    
    def _extract_glove_properties(self):
        """
        Extrai todas as propriedades dos vetores glove considerando o mapeamento ente palavras e vetores
        """
        glove = self._load_glove_vector()
        glove_shape = glove.vectors.shape
        glove_dim = glove.vector_size
        glove_words = glove.index_to_key
        glove_vectors = torch.from_numpy(glove.vectors).to('cpu')
        glove_vocab = {word:i for i, word in enumerate(glove_words)}
        
        glove_infos = {'glove_shape':glove_shape,
                      'glove_dim':glove_dim,
                     'glove_words':glove_words,
                     'glove_vectors':glove_vectors,
                     'glove_vocab':glove_vocab}
        
        self.glove_infos = glove_infos
    
    def _separate_punctuation_from_words(self,text):
        """"
        Pontuações são separadas das palavras porque caso estejam juntas esta palavra não estará no vetor de embeddings
        """
        punctuation_list = '!(),.:;?'
        for punct in list(punctuation_list):
            text = text.replace(punct,f" {punct} ")

        return text
            
    def _tokenize_text(self,text_list: list = None):
        """
        Transforma o texto em lista de palavras
        """
        tokenize_list = list()
        for text in text_list:
            text = text[0]
            text = self._separate_punctuation_from_words(text)
            text = text.split(" ")
            tokenize_list.append(text)
        return tokenize_list


    def build_glove_matrix(self,X):
        """
        Cria as matriz de texto com palavras contida no espaço de palavras e a matrix com os ids de vetores gloves
        """
        X = self._tokenize_text(X)
        glove_matrix = []
        word_filtered_matrix = []

        for token_line in X:
            token_phrase = [
                self.glove_infos['glove_vocab'][word] for word in token_line if (word in self.glove_infos['glove_vocab'])
            ]
            filtered_words = [word for word in token_line if (word in self.glove_infos['glove_vocab'])]
            word_filtered_matrix.append(filtered_words)
            glove_matrix.append(token_phrase)

        return glove_matrix, word_filtered_matrix
