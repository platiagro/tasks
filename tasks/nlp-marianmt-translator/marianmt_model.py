from transformers import MarianMTModel, MarianTokenizer
import spacy
from spacy.lang.en import English
import torch
import numpy as np
import pandas as pd
from tqdm import tqdm
import sacrebleu
import random


class MarianMTTranslator:
  def __init__(self,hyperparams,model_params):
    
    #------- Data
    self.X = None
    self.y_target = None

    #------- Hyperparams
    self.input_max_length = hyperparams['input_max_length']
    self.output_max_length = hyperparams['output_max_length']
    self.inference_batch_size = hyperparams['inference_batch_size']
    self.seed = hyperparams['seed']

    #------- Model Params
    self.model = MarianMTModel.from_pretrained(model_params['model_name'])
    self.tokenizer = MarianTokenizer.from_pretrained(model_params['model_name'])
    self.prefix = model_params['prefix']

    #------- Others
    self.nlp = English()
    self.nlp.add_pipe(self.nlp.create_pipe('sentencizer'))
    dev = "cuda:0" if torch.cuda.is_available() else "cpu"
    self.device = torch.device(dev)

    #------- Results
    self.y_pred = None
    self.avg_bleu = None
    self.bleu_array = None
    self.df_result  = None

    #Configurando semente de randomização
    random.seed(self.seed)
    np.random.seed(self.seed)
    torch.random.manual_seed(self.seed)
    torch.cuda.manual_seed(self.seed)
    torch.backends.cudnn.deterministic = True
        
  def _chunkstring_spacy(self,text):
      chunck_sentences = []
      doc = self.nlp(text)
      for sent in doc.sents:
          chunck_sentences.append(sent.text)
      return chunck_sentences

  def _predict(self,text_array=None):
      if text_array:
        self.X = text_array
      #Move o modelo para a GPU
      self.model.to(self.device)
      self.model.eval()

      result = [''] * len(self.X)
      for batch_number in tqdm(range(0, len(self.X), self.inference_batch_size)):
          #0) Controlando os intervalos
          batch_number_final = batch_number+self.inference_batch_size-1
          batch_number_final = batch_number_final if batch_number_final<len(self.X) else len(self.X)-1
          #batch_number_start = batch_number_final-batch_size+1 if (batch_number_final+1)==self.inference_batch_size else len(self.X)-batch_number_final
          batch_number_start  =batch_number
          X_batch = self.X[batch_number_start:batch_number_final+1]

          #1) Zerando os vetores 
          batchs = []
          id_identifier = []
          tranlations = []   

          #2) Separando documento a cada fim de sentença de forma inteligentge
          doctext_chuncks = {batch_number_start+i:self._chunkstring_spacy(elem) for i,elem in enumerate(X_batch)}
          
          #3) Controladno tamanho dos chuncks
          splited_max_sentences_dict = {}
          for row_id,sentences in doctext_chuncks.items():
            splited_max_sentences = []
            for sentence in sentences:
              sentence_length = len(sentence.split(' '))
              #neste caso se a sentença do chunck é maior que o max permitido faz chuncks do chunck
              if  sentence_length > self.input_max_length:
                for i in range(int((sentence_length/self.input_max_length)+1)):
                    splited_max_sentences.append(' '.join(sentence.split(' ')[i*self.input_max_length:(i+1)*self.input_max_length]))
              #caso não inclui o propio chunck
              else:
                    splited_max_sentences.append(sentence)
              
            splited_max_sentences_dict[row_id] = splited_max_sentences


          #4) Colocando o prefixo de tradução pt_br
          for row_id,sentences in splited_max_sentences_dict.items():
              for sentence in sentences:
                final_sent = ">>pt_br<<" + ' ' + sentence
                batchs.append(final_sent)
                id_identifier.append(row_id)

          #5) Tradução utilizando o MarianMT
          for i in range(0, len(batchs), 64):
              tokenized_text = self.tokenizer.prepare_translation_batch(batchs[i:i+64], max_length=self.output_max_length)

              translated = self.model.generate(input_ids=tokenized_text['input_ids'].to(self.device), 
                                                  max_length=self.output_max_length, num_beams=1, 
                                                  early_stopping=True, 
                                                  do_sample=False)
              tranlations.extend(self.tokenizer.batch_decode(translated, skip_special_tokens=True))

          
          #6) Remontando o batch
          dict_result = doctext_chuncks = {batch_number_start+i:'' for i in range(0,len(X_batch))}
          for tranlation,id in zip(tranlations,id_identifier):
              dict_result[id] += tranlation

          #7) Salvando resultado
          for row_id,document_text in dict_result.items():
            result[row_id] = document_text
          
      return np.array(result)
  
  def _calc_bleu(self):
      results = np.zeros(len(self.y_target))
      for iter in zip(enumerate(self.y_target),self.y_pred):
          aux,pred = iter
          row_number = aux[0]
          target = aux[1]
          bleu_score = sacrebleu.corpus_bleu([pred], [[target]]).score
          results[row_number] = bleu_score
      return results, np.mean(results) 

  def _construct_result_dataframe(self,step):
    if step == 'Experiment':
      self.y_pred = self._predict()
      self.bleu_array,self.avg_bleu = self._calc_bleu()
      self.df_result = pd.DataFrame({'source_text': self.X, 'target_text': self.y_target,'translated_text': self.y_pred,'bleu_score': self.bleu_array})
    if step == 'Deployment':
      self.y_pred = self._predict() 
      self.df_result = pd.DataFrame({'source_text': self.X,'translated_text': self.y_pred}) 
  
  def get_result_dataframe(self,X,y=None,step = 'Experiment'):
    
    #squeezing X if necesary
    try:
        test = X.shape[1]
        self.X = np.squeeze(X)
    except Exception as e:
        self.X = X

    #squeezing y if necesary
    try:
        test = y.shape[1] if y else 0
        self.y_target = np.squeeze(y) if y else y
    except Exception as e:
        self.y_target = y
    self._construct_result_dataframe(step)
    return self.df_result
     