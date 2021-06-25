import torch
import nltk
from tqdm import tqdm
from multiprocessing import cpu_count
from typing import List, Union, Optional
import numpy as np
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from transformers import T5ForConditionalGeneration
from nlgeval import NLGEval
from gensim.models import KeyedVectors
nltk.download('stopwords')

class Metrics_Calculator(object):

    def __init__(self,hparams,glove_comparer):

      
        super(Metrics_Calculator, self).__init__()
        self.nlg_eval = NLGEval(metrics_to_omit=['EmbeddingAverageCosineSimilairty', 'EmbeddingAverageCosineSimilarity','GreedyMatchingScore','SkipThoughtCS','VectorExtremaCosineSimilarity'])
        self.list_dict_track  = {"data":[]}
        self.hparams = hparams
        self.glove_comparer = glove_comparer

        
    def build_json_results(self,
                           context,
                           generated_question_list,
                           target_question_list,
                           row_mean_metrics):

        """
        Cria json para cada linha que será salvo para monitorar as métricas em self.list_dict_track
        """
        new_info = {}
        new_info["context"] =context
        new_info["generated_question_list"] =generated_question_list
        new_info["target_question_list"] =target_question_list
        new_info["row_mean_metrics"] =row_mean_metrics

        
        return new_info

    def track_metrics_row(self,original_target,gen_target_options_list):
        """ 
        Calcula as métricas para cada par question-context
        """
        bleu_1_list = []
        bleu_2_list = []
        bleu_3_list = []
        bleu_4_list = []
        CIDEr_list = []
        ROUGE_L_list = []
        cossine_similarity_list = []

        for gen_target_option in gen_target_options_list:
          
          metrics_dict = self.nlg_eval.compute_individual_metrics(ref=[original_target],hyp=gen_target_option)#ref:List[str] , hyp:str
          bleu_1_list.append(metrics_dict['Bleu_1'])
          bleu_2_list.append(metrics_dict['Bleu_2'])
          bleu_3_list.append(metrics_dict['Bleu_3'])
          bleu_4_list.append(metrics_dict['Bleu_4'])
          CIDEr_list.append(metrics_dict['CIDEr'])
          ROUGE_L_list.append(metrics_dict['ROUGE_L'])
          cs = self.glove_comparer.compare_sentences_with_cossine_similarity(original_target,gen_target_option)
          cossine_similarity_list.append(cs)
          
          

        row_metrics_dict = {"Bleu_1":np.mean(bleu_1_list),
                             "Bleu_2":np.mean(bleu_2_list),
                             "Bleu_3":np.mean(bleu_3_list),
                             "Bleu_4":np.mean(bleu_4_list),
                             "CIDEr":np.mean(CIDEr_list),
                             "ROUGE_L":np.mean(ROUGE_L_list),
                             "Glove_Cossine_Similarity":np.mean(cossine_similarity_list)}

        return row_metrics_dict


    
    def generate_sentences_and_track_metrics_batch(self,logits,original_targets_batch,original_sources_batch,save_track_dict=False):
        """
        Calcula métricas para todo o batch
        """
        batch_bleu_1_list = []
        batch_bleu_2_list = []
        batch_bleu_3_list = []
        batch_bleu_4_list = []
        batch_CIDEr_list = []
        batch_ROUGE_L_list = []
        batch_Glove_Cossine_Similarity_list = []


        #batch
        for i,(original_target,original_source) in enumerate(zip(original_targets_batch,original_sources_batch)):
          #linha
          relevant_logits = logits[i*self.hparams.num_gen_sentences:self.hparams.num_gen_sentences+i*self.hparams.num_gen_sentences]
          gen_target_options_list = [self.hparams.tokenizer.decode(l, skip_special_tokens=True) for l in relevant_logits]
          row_metrics_dict = self.track_metrics_row(original_target=original_target,gen_target_options_list=gen_target_options_list)

          if save_track_dict:
            self.list_dict_track["data"].append(self.build_json_results(context=original_source,
                                  generated_question_list=gen_target_options_list,
                                  target_question_list=original_target,
                                  row_mean_metrics = row_metrics_dict))
          
          batch_bleu_1_list.append(row_metrics_dict['Bleu_1'])
          batch_bleu_2_list.append(row_metrics_dict['Bleu_2'])
          batch_bleu_3_list.append(row_metrics_dict['Bleu_3'])
          batch_bleu_4_list.append(row_metrics_dict['Bleu_4'])
          batch_CIDEr_list.append(row_metrics_dict['CIDEr'])
          batch_ROUGE_L_list.append(row_metrics_dict['ROUGE_L'])
          batch_Glove_Cossine_Similarity_list.append(row_metrics_dict['Glove_Cossine_Similarity'])


        batch_metrics_dict = {"Batch_Bleu_1":np.mean(batch_bleu_1_list),
                              "Batch_Bleu_2":np.mean(batch_bleu_2_list),
                              "Batch_Bleu_3":np.mean(batch_bleu_3_list),
                              "Batch_Bleu_4":np.mean(batch_bleu_4_list),
                              "Batch_CIDEr":np.mean(batch_CIDEr_list),
                              "Batch_ROUGE_L":np.mean(batch_ROUGE_L_list),
                              "Batch_Glove_Cossine_Similarity":np.mean(batch_Glove_Cossine_Similarity_list)
                             }

        return batch_metrics_dict


class Glove_Embeddings_Comparer(object):
    """
    Classes reponsável por criar a matriz de glove embeddings com os textos fornecidos
    """
    def __init__(self,glove_weights_path:str,device:str):
        super(Glove_Embeddings_Comparer , self).__init__()
        
        self.device = device
        self.glove_path  = glove_weights_path
        self.glove = None
        self.glove_infos = None
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.extract_glove_properties()
        

    def load_glove_vector(self):
        """
        Carrega os vetores glove no formato word2vec
        """

        #glove = KeyedVectors.load_word2vec_format(self.glove_path)
        try: 
            glove = KeyedVectors.load_word2vec_format(self.glove_path,no_header=False)
            print("load_word2vec_format with no_header=False")
        except ValueError:
            glove = KeyedVectors.load_word2vec_format(self.glove_path,no_header=True)
            print("load_word2vec_format with no_header=True")
        
        return glove
    
    def extract_glove_properties(self):
        """
        Extrai todas as propriedades dos vetores glove considerando o mapeamento ente palavras e vetores
        """
        glove = self.load_glove_vector()
        glove_shape = glove.vectors.shape
        glove_dim = glove.vector_size
        glove_words = glove.index_to_key
        glove_vectors = torch.from_numpy(glove.vectors).to(self.device)
        glove_vocab = {word:i for i, word in enumerate(glove_words)}
        
        glove_infos = {'glove_shape':glove_shape,
                      'glove_dim':glove_dim,
                     'glove_words':glove_words,
                     'glove_vectors':glove_vectors,
                     'glove_vocab':glove_vocab}
        

        self.glove = glove
        self.glove_infos = glove_infos
    
    def separate_punctuation_from_words(self,text):
        """"
        Pontuações são separadas das palavras porque caso estejam juntas esta palavra não estará no vetor de embeddings
        """
        punctuation_list = '!(),.:;?'
        for punct in list(punctuation_list):
            text = text.replace(punct,f" {punct} ")

        text = text.strip()
        return text
    
    def tokenize_text(self,text: list = None):
        """
        Transforma o texto em lista de palavras
        """
        text = self.separate_punctuation_from_words(text)
        tokenize_list = text.split(" ")
        tokenize_list = [token for token in tokenize_list if ((token not in self.stopwords) and (token in self.glove_infos['glove_vocab']))]
        return tokenize_list

    def cosine_similarity_calculator(self,a, b):
        """
        Caclula a similaridade de cossenos entre dois vetores
        """
        nominator = np.dot(a, b)
        
        a_norm = np.sqrt(np.sum(a**2))
        b_norm = np.sqrt(np.sum(b**2))
        
        denominator = a_norm * b_norm
        
        cosine_similarity = nominator / denominator
        
        return cosine_similarity

    def compare_sentences_with_cossine_similarity(self,text1,text2):
        """
        Compara duas sentenças com similaridade de cossenos
        """
        tokenize_list1 = self.tokenize_text(text1)
        tokenize_list2 = self.tokenize_text(text2)

        embeddigns_sentence1 = [self.glove.get_vector(t1) for t1 in tokenize_list1]
        embeddigns_sentence1_mean = np.mean(embeddigns_sentence1,axis=0)
        embeddigns_sentence2 = [self.glove.get_vector(t2) for t2 in tokenize_list2]
        embeddigns_sentence2_mean = np.mean(embeddigns_sentence2,axis=0)
        cosine_similarity = self.cosine_similarity_calculator(embeddigns_sentence1_mean,embeddigns_sentence2_mean)
        cosine_similarity = np.float64(cosine_similarity)
        return cosine_similarity

    
    def batch_average_cossine_similarity(self,list_ref_texts,list_gen_texts):
        pass


class T5Finetuner(pl.LightningModule):

    def __init__(self, 
                 hparams):
      
        super(T5Finetuner, self).__init__()


        self.hparams = hparams

        # ---------- fixing seeds
        # self.seed_everything()
        pl.utilities.seed.seed_everything(seed = self.hparams.seed)


        # ---------- Model
        self.model = T5ForConditionalGeneration.from_pretrained(self.hparams.model_name)

        #----------Other infos
        self.i = 0
        self.step = "Experiment"
        self.softmax = torch.nn.Softmax(dim=1)
        self.loss_funtion =  torch.nn.CrossEntropyLoss()


        #----------Metrics Trackers
        if self.hparams.track_metrics == True:
            glove_comparer = Glove_Embeddings_Comparer(glove_weights_path=self.hparams.glove_weights_path,device=self.hparams.device)
            self.valid_metrics_calculator = Metrics_Calculator(self.hparams,glove_comparer)
            self.test_metrics_calculator = Metrics_Calculator(self.hparams,glove_comparer)

    def predict(self,X_context:np.ndarray,num_gen_sentences=10):
        self.step = "Deployment"
        self.model.eval()
        self.hparams["all_data"] = {'X_test':np.array(X_context),'y_test':[]}
        self.hparams.num_gen_sentences = num_gen_sentences
        result = {}
        j = 0
        for i,batch in enumerate(tqdm(self.test_dataloader())):
            source_token_ids, source_masks, original_source = batch
            logits = self.forward(source_token_ids, source_masks,info_requested='logits')
            gen_quesitons = [self.hparams.tokenizer.decode(l, skip_special_tokens=True) for l in logits]
            questions_per_context = [gen_quesitons[s:s+self.hparams.num_gen_sentences] for s in list(range(0,len(gen_quesitons),self.hparams.num_gen_sentences))]
            result_batch = {j+k:{'context':original_source[k],'questions':questions_per_context[k]} for k in range(len(original_source))}
            result.update(result_batch)
            j +=len(batch)

        return result
    

    def forward(self, source_token_ids, source_mask, target_token_ids=None,
                target_mask=None,info_requested='loss'):
        

        if info_requested=='loss':

            # TODO calcular a loss dado os target_token_ids
            outputs = self.model(input_ids = source_token_ids, attention_mask = source_mask,labels = target_token_ids)
            
            # loss, predicted_token_ids = outputs[:2]
            loss = outputs[0]
            result =  loss
        if info_requested=='logits':
            #num_return_sequences must be 1
            if info_requested=='logits':
                decoder_output = self.model.generate(
                                input_ids =source_token_ids,
                                attention_mask=source_mask, 
                                max_length= self.hparams.target_max_length,
                                do_sample=True,  
                                num_return_sequences=self.hparams.num_gen_sentences,
                                temperature = self.hparams.temperature,
                                top_p=self.hparams.top_p, 
                                top_k=0)

            result =  decoder_output

        return result

    def training_step(self, batch, batch_nb):
        # batch
        source_token_ids, source_masks, target_token_ids, target_masks, original_sources, original_targets = batch
         
        # fwd
        loss = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='loss')  
        batch_metrics_dict = {'loss':loss}
        return batch_metrics_dict

   
    def validation_step(self, batch, batch_nb):
        # batch
        source_token_ids, source_masks, target_token_ids, target_masks, original_sources, original_targets = batch
         
        # fwd
        loss = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='loss')
        logits = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='logits')

        #Calc Metrics and Saving Results
        batch_metrics_dict = self.valid_metrics_calculator.generate_sentences_and_track_metrics_batch(logits,original_targets,original_sources,save_track_dict=True)

        tensorboard_logs = {'valid_'+key: value for (key, value) in batch_metrics_dict.items()}
        tensorboard_logs['valid_loss'] = loss.item() 

        #include special values to batch metrics dict
        batch_metrics_dict['loss']  = loss
        batch_metrics_dict['log'] = tensorboard_logs

        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict

    def test_step(self, batch, batch_nb):

        # batch
        source_token_ids, source_masks, target_token_ids, target_masks, original_sources, original_targets = batch

        # fwd
        logits = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='logits')

        #Calc Metrics and Saving Results
        batch_metrics_dict = self.test_metrics_calculator.generate_sentences_and_track_metrics_batch(logits,original_targets,original_sources,save_track_dict=True)

        tensorboard_logs = {'test_'+key: value for (key, value) in batch_metrics_dict.items()}

        #include special values to batch metrics dict
        batch_metrics_dict['log'] = tensorboard_logs
        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict
    
    def get_epoch_results(self,outputs,step='train'):
        
        tensorboard_logs = {}

        if step != "test":
            temp_avg_loss_batch = [x["loss"] for x in outputs]
            avg_loss = torch.stack(temp_avg_loss_batch).mean()

        if step != "train":
            temp_avg_bleu1_batch = [x["Batch_Bleu_1"] for x in outputs]
            temp_avg_bleu2_batch = [x["Batch_Bleu_2"] for x in outputs]
            temp_avg_bleu3_batch = [x["Batch_Bleu_3"] for x in outputs]
            temp_avg_bleu4_batch = [x["Batch_Bleu_4"] for x in outputs]
            temp_avg_cider_batch = [x["Batch_CIDEr"] for x in outputs]
            temp_avg_rougeL_batch = [x["Batch_ROUGE_L"] for x in outputs] 
            temp_avg_glove_cossine_similarity = [x["Batch_Glove_Cossine_Similarity"] for x in outputs] 

            avg_bleu1 = np.stack(temp_avg_bleu1_batch).mean()
            avg_bleu2 = np.stack(temp_avg_bleu2_batch).mean()
            avg_bleu3 = np.stack(temp_avg_bleu3_batch).mean()
            avg_bleu4 = np.stack(temp_avg_bleu4_batch).mean()
            avg_cider = np.stack(temp_avg_cider_batch).mean()
            avg_rougeL = np.stack(temp_avg_rougeL_batch).mean()
            avg_glove_cossine_similarity = np.stack(temp_avg_glove_cossine_similarity).mean()

            tensorboard_logs[f"avg_{step}_bleu1"] = avg_bleu1
            tensorboard_logs[f"avg_{step}_bleu2"] = avg_bleu2
            tensorboard_logs[f"avg_{step}_bleu3"] = avg_bleu3
            tensorboard_logs[f"avg_{step}_bleu4"] = avg_bleu4
            tensorboard_logs[f"avg_{step}_cider"] = avg_cider
            tensorboard_logs[f"avg_{step}_rougeL"] = avg_rougeL
            tensorboard_logs[f"avg_{step}_rougeL"] = avg_glove_cossine_similarity

        if step != "test":
            tensorboard_logs[f"avg_{step}_loss"] =  avg_loss.item()

        epoch_dict = tensorboard_logs.copy()
        epoch_dict['log'] =  tensorboard_logs

        for key, value in epoch_dict.items():
            self.log(key, value, on_epoch=True, prog_bar=True, logger=True)

        return epoch_dict

    def training_epoch_end(self, outputs):
        if not outputs:
            return {}
        epoch_dict = self.get_epoch_results(outputs,'train') 
        

    def validation_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'valid')
        return epoch_dict #must do to save checkpoints

    def test_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'test')

    
    def configure_optimizers(self):
        return torch.optim.AdamW(
            [p for p in self.parameters() if p.requires_grad],
            lr=self.hparams.learning_rate, eps=self.hparams.eps)

    def train_dataloader(self):
        self.train_dataset = self.hparams.CustomDataset(PREFIX=self.hparams.PREFIX,
                    tokenizer=self.hparams.tokenizer,
                    X_context=self.hparams.all_data['X_train'],
                    y_question=self.hparams.all_data['y_train'],
                    source_max_length=self.hparams.source_max_length,
                    target_max_length=self.hparams.target_max_length,
                    step=self.step,
                    )
        shuffle = False if self.hparams.overfit else True
        return DataLoader(self.train_dataset, batch_size=self.hparams.train_batch_size, shuffle=shuffle,num_workers=cpu_count())
    
    def val_dataloader(self):
        self.valid_dataset = self.hparams.CustomDataset(PREFIX=self.hparams.PREFIX,
                            tokenizer=self.hparams.tokenizer,
                            X_context=self.hparams.all_data['X_valid'],
                            y_question=self.hparams.all_data['y_valid'],
                            source_max_length=self.hparams.source_max_length,
                            target_max_length=self.hparams.target_max_length,
                            step=self.step,
                            )
        return DataLoader(self.valid_dataset, batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())
    
    def test_dataloader(self):
        self.test_dataset = self.hparams.CustomDataset(PREFIX=self.hparams.PREFIX,
                            tokenizer=self.hparams.tokenizer,
                            X_context=self.hparams.all_data['X_test'],
                            y_question=self.hparams.all_data['y_test'],
                            source_max_length=self.hparams.source_max_length,
                            target_max_length=self.hparams.target_max_length,
                            step=self.step,
                            )
        return DataLoader(self.test_dataset, batch_size=self.hparams.eval_batch_size,shuffle=False, num_workers=cpu_count())

