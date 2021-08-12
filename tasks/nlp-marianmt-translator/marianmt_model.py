from transformers import MarianMTModel, MarianTokenizer
import spacy
from spacy.lang.en import English
import torch
import numpy as np
import pandas as pd
from tqdm import tqdm
from nltk.translate.bleu_score import sentence_bleu
import random
from typing import List


class MarianMTTranslator:
    
    
    def __init__(self,hyperparams):
        def verify_args():
            possible_models_list = ["Helsinki-NLP/opus-mt-ROMANCE-en","Helsinki-NLP/opus-mt-en-ROMANCE"]
            if not all(isinstance(s, str) for s in self.models_list): 
                raise ValueError(f"{self.models_list} must be a list of strings") 
            if (len(self.models_list) not in [1,2]):
                raise ValueError(f"{self.models_list} have length 1 or 2")
            if self.models_list[0] not in possible_models_list:
                raise ValueError(f"Position on 0 of models_list is {self.models_list[0]} and must be in the options {possible_models_list}") 
            if (len(self.models_list)==2) and self.models_list[1] not in possible_models_list:
                raise ValueError(f"Position on 1 of models_list is {self.models_list[1]} and must be in the options {possible_models_list}") 
            if type(self.max_length) != int:
                raise ValueError(f"hyperparams['max_length'] must be an integer")
            if type(self.seed) != int:
                raise ValueError(f"hyperparams['seed'] must be an integer")
            
        #------ Getting Args
        self.models_list = hyperparams['models_list']
        self.max_length = hyperparams['max_length']
        self.inference_batch_size = hyperparams['inference_batch_size']
        self.target_language = hyperparams['target_language']
        self.seed = hyperparams.get('seed',42)
        verify_args()

        #------- Creating Model Tokenizer
        self.model1,self.tokenizer1,self.model2,self.tokenizer2 = self._create_models_and_tokenizers()

        #------- Data
        self.X = None
        self.y_target = None

        #------- Others
        self.nlp = English()
        self.nlp.add_pipe('sentencizer')
        dev = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(dev)
        self.prefixes_dict = {"Alemão": "de",
                                "Catalão": "ca",
                                "Espanhol": "es",
                                "Francês": "fr",
                                "Inglês": "en",
                                "Italiano": "it",
                                "Latim": "la",
                                "Português": "pt_br",
                                "Romeno": "ro"}
        #------- Results
        self.y_pred = None
        self.avg_bleu = None
        self.bleu_array = None
        self.df_result  = None

        # Configurando semente de randomização
        self._seed_parameters()
    
    def _create_models_and_tokenizers(self):
        
        model1 = MarianMTModel.from_pretrained(self.models_list[0])
        tokenizer1 = MarianTokenizer.from_pretrained(self.models_list[0])
        if len(self.models_list) == 1:
            model2 = None
            tokenizer2 = None
        elif len(self.models_list) == 2:
            model2 = MarianMTModel.from_pretrained(self.models_list[1])
            tokenizer2 = MarianTokenizer.from_pretrained(self.models_list[1])
        else:
            raise ValueError("Is excpeted that the argiment models_list has the length 1 or 2")
        
        return model1,tokenizer1,model2,tokenizer2
        
    def _seed_parameters(self):
        random.seed(self.seed)
        np.random.seed(self.seed)
        torch.random.manual_seed(self.seed)
        torch.cuda.manual_seed(self.seed)
        torch.backends.cudnn.deterministic = True

    def _chunkstring_spacy(self,text):
        chunck_sentences = []
        doc = self.nlp(str(text))
        for sent in doc.sents:
            chunck_sentences.append(sent.text)
        return chunck_sentences
    
    def predict(self,text_array:List[str]):
        
        if (not self.model2) and (not self.tokenizer2):
            translated_text = self._translate(text_array=text_array,
                                              tokenizer=self.tokenizer1,
                                              model=self.model1,
                                              target_prefix = self.prefixes_dict[self.target_language])
        else:
            english_text = self._translate(text_array=text_array,
                                              tokenizer=self.tokenizer1,
                                              model=self.model1,
                                              target_prefix = 'en')
            translated_text = self._translate(text_array=english_text,
                                              tokenizer=self.tokenizer2,
                                              model=self.model2,
                                              target_prefix = self.prefixes_dict[self.target_language])
            
            
        
        return translated_text

    def _translate(self, text_array:List[str],tokenizer,model,target_prefix):
        #Creating template func
        template_func = lambda text: f"{text}" if target_prefix == "en" else f">>{target_prefix}<< {text}"
        
        # Move o modelo para a GPU
        model.to(self.device)
        model.eval()

        result = [''] * len(text_array)
        
        #0) Remover espaços em excesso
        text_array_batch = [' '.join(sentence.split()).replace('"','').strip() for sentence in text_array]

        #1) Zerando os vetores 
        batchs = []
        id_identifier = []
        tranlations = []   

        #2) Separando documento a cada fim de sentença de forma inteligentge
        doctext_chuncks = {i:self._chunkstring_spacy(elem) for i, elem in enumerate(text_array_batch)}
        
        #3) Controladno tamanho dos chuncks
        splited_max_sentences_dict = {}
        for row_id, sentences in doctext_chuncks.items():
            
            splited_max_sentences = []
            for sentence in sentences:
                sentence_length = len(sentence.split(' '))
                #neste caso se a sentença do chunck é maior que o max permitido faz chuncks do chunck
                if  sentence_length > self.max_length:
                    for i in range(int((sentence_length / self.max_length)+1)):
                        splited_max_sentences.append(' '.join(sentence.split(' ')[i*self.max_length:(i+1)*self.max_length]))
                #caso não inclui o propio chunck
                else:
                    splited_max_sentences.append(sentence)
                
                splited_max_sentences_dict[row_id] = splited_max_sentences


        #4) Colocando o prefixo de tradução
        for row_id,sentences in splited_max_sentences_dict.items():
            for sentence in sentences:
                final_sent = template_func(sentence)
                batchs.append(final_sent)
                id_identifier.append(row_id)
        
        #5) Tradução utilizando o MarianMT
        for i in range(0, len(batchs), self.inference_batch_size):
            #tokenized_text = self.tokenizer.prepare_translation_batch(batchs[i:i+64], max_length=self.max_length)
            batch_inputs = tokenizer(batchs[i:i + self.inference_batch_size],
                                            max_length=self.max_length,
                                            return_tensors='pt',
                                            padding=True,
                                            truncation=True
                                            )
            batch_inputs = batch_inputs.to(self.device)
 
            translated = model.generate(**batch_inputs)
            tranlations.extend(tokenizer.batch_decode(translated,skip_special_tokens=True))
        
        #6) Remontando o batch
        dict_result  = {i:'' for i in np.unique(id_identifier)}
        for tranlation,id in zip(tranlations,id_identifier):
            dict_result[id] += tranlation
        result = np.array(list(dict_result.values()))

        return result


    def _calc_bleu(self):

        results = np.zeros(len(self.y_target))
        for iter in zip(enumerate(self.y_target),self.y_pred):
            aux,pred = iter
            row_number = aux[0]
            target = aux[1]
            bleu_score = sentence_bleu([target],pred)
            results[row_number] = bleu_score

        return results, np.mean(results) 

    
    def get_result_dataframe(self,df_input:pd.DataFrame,input_column_name:str,output_column_name:str,reference_column_name:None):
        
        #if (not reference_column_name) or (reference_column_name not in df_input.columns):
        #    raise ValueError(f"A coluna {reference_column_name} não existe em {df_input.columns}")
        
        self.X = df_input[input_column_name].to_numpy()
        self.y_target = df_input[reference_column_name].to_numpy() if reference_column_name else None
        self.y_pred = self.predict(self.X)
        self.df_result = df_input.copy()
        self.df_result.insert(df_input.shape[1], output_column_name, self.y_pred)
        
        if type(self.y_target) == np.ndarray:
            self.bleu_array,self.avg_bleu = self._calc_bleu()
            self.df_result.insert(df_input.shape[1], 'bleu_score', self.bleu_array)

        return self.df_result
