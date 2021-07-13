import os 
import yaml
import torch
import numpy as np
import pandas as pd
import pytorch_lightning as pl
from torch.utils.data import DataLoader

from sklearn.model_selection import train_test_split
from pytorch_lightning.callbacks import ModelCheckpoint,EarlyStopping,GPUStatsMonitor
from transformers import AutoModelForQuestionAnswering,AutoTokenizer
from typing import List
from multiprocessing import cpu_count
from torch.utils.data import Dataset

from io_utils import IO_Utils
# from nlgeval import NLGEval
from dataset import CustomDataset
from model import Reader

class Reader_Caller():
    """Modelo Abstrato Herdado por todos os outros modelos"""
    def __init__(self, cfg):
        #self.config = Config.from_json(cfg)
        self.config = cfg
        self.io_utils = IO_Utils()
        self.MODEL = None

        # Checagem da ordem das chamadas
        self.build_called = False
        self.train_called = False
        self.load_called = False
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        
    ###########################################################################
    #                                                                         #
    #                            Required Methods                             #
    #                                                                         #
    ###########################################################################

    def build(self,**kwargs):
        """
        Reponsável por criar os argumentos da classe
        """
        # Checagem das Chamadas
        self.build_called = True

        # Rcuperando Caminhos
        self.data_dirpath = self.config['dirpaths']['data_dirpath']
        self.log_dirpath = self.config['dirpaths']['log_dirpath']
        self.cwd_dirpath = self.config['dirpaths']['cwd_dirpath']

        # Rcuperando Parâmetros
        self.hparams = self.config['params']['hparams']
        self.lightning_params = self.config['params']['lightning_params']
        self.early_stop_callback_params = self.config['params']['early_stop_callback_params']
        self.prepare_data_params = self.config['params']['prepare_data_params']
        #-
        self.test_size_from_dev = self.prepare_data_params['test_size_from_dev']
        self.batch_dataset_preparation = self.prepare_data_params['batch_dataset_preparation']
        #-
        self.model_name = self.hparams['model_name']
        self.train_batch_size = self.hparams['train_batch_size']
        self.eval_batch_size = self.hparams['eval_batch_size']
        self.max_length = self.hparams['max_length']
        self.doc_stride = self.hparams['doc_stride']
        self.learning_rate = self.hparams['learning_rate']
        self.eps = self.hparams['eps']
        self.seed = self.hparams['seed']
        #-
        self.num_gpus = self.lightning_params['num_gpus'] if torch.cuda.is_available() else 0
        self.profiler = self.lightning_params['profiler']
        self.max_epochs = self.lightning_params['max_epochs']
        self.accumulate_grad_batches = self.lightning_params['accumulate_grad_batches']
        self.check_val_every_n_epoch = self.lightning_params['check_val_every_n_epoch']
        self.progress_bar_refresh_rate = self.lightning_params['progress_bar_refresh_rate']
        self.gradient_clip_val = self.lightning_params['gradient_clip_val']
        self.fast_dev_run = self.lightning_params['fast_dev_run']
        #-
        self.monitor = self.early_stop_callback_params['monitor']
        self.min_delta = self.early_stop_callback_params['min_delta']
        self.patience = self.early_stop_callback_params['patience']
        self.verbose = self.early_stop_callback_params['verbose']
        self.mode = self.early_stop_callback_params['mode']

        # Criando parâmetros adicionais
        self.tokenizer = AutoTokenizer.from_pretrained(self.config['params']['hparams']['model_name'])
        self.softmax = torch.nn.Softmax(dim=1)
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

        # Trainer
        if self.fast_dev_run:
            self.TRAINER = pl.Trainer(
                gpus=self.num_gpus,
                checkpoint_callback=False,
                fast_dev_run=True  # Disable checkpoint saving.
            )
        else:
            checkpoint_callback = ModelCheckpoint(
            dirpath=self.data_dirpath, save_top_k=-1
            )

            early_stop_callback = EarlyStopping(
                monitor=self.early_stop_callback_params['monitor'],
                min_delta=self.early_stop_callback_params['min_delta'],
                patience=self.early_stop_callback_params['patience'],
                verbose=self.early_stop_callback_params['verbose'],
                mode=self.early_stop_callback_params['mode']
                )

            gpu_stats = GPUStatsMonitor() 
            tb_logger = pl.loggers.TensorBoardLogger(f"{self.log_dirpath}")

            self.TRAINER = pl.Trainer(
            gpus= self.lightning_params['num_gpus'],
            profiler=self.lightning_params['profiler'],
            max_epochs=self.lightning_params['max_epochs'],
            accumulate_grad_batches = self.lightning_params['accumulate_grad_batches'],
            check_val_every_n_epoch=self.lightning_params['check_val_every_n_epoch'],
            progress_bar_refresh_rate=self.lightning_params['progress_bar_refresh_rate'],
            callbacks = [early_stop_callback,gpu_stats,checkpoint_callback],
            resume_from_checkpoint=None,
            logger = tb_logger
            )

    def forward(self,**kwargs):

        def verify_args(question,topn_contexts):
            if not question:
                raise ValueError("question é um argumento obrigatório")
            if not topn_contexts:
                raise ValueError("topn_contexts é um argumento obrigatório")
            if not all(isinstance(elem, str) for elem in topn_contexts):
                raise ValueError(f"topn_contexts deve ser uma lista de strings mas é {topn_contexts}")
            if type(question) != str:
                raise ValueError(f"question deve ser uma string")
        # Checagem das Chamadas
        if not (self.build_called and (self.train_called or self.load_called)):
            raise AssertionError("Para chamar o método forward é nececssário chamar o método build e em seguida o método train ou o método load")

        # Recuperando variáveis kwargs
        question = kwargs.get('question',None)
        topn_contexts = kwargs.get('topn_contexts',None)
        verify_args(question,topn_contexts)

        list_questions = [question]*len(topn_contexts)
        chunckfied_encoded_samples = self._chunckfy_with_stride(list_questions,topn_contexts)
        #(['input_ids', 'token_type_ids', 'attention_mask','overflow_to_sample_mapping'])

        # Initialize Vectors to create dataframe
        question_list = []
        context_list = []
        answer_list = []
        answer_prob_list = []

        #Context control vector
        context_ids_list = []

        for chunck_id, context_id in enumerate(chunckfied_encoded_samples['overflow_to_sample_mapping']):
            context = topn_contexts[context_id]
            input_id_chunck = np.array([chunckfied_encoded_samples['input_ids'][chunck_id]])
            attention_mask_chunck = np.array([chunckfied_encoded_samples['attention_mask'][chunck_id]])
            token_type_chunck = np.array([chunckfied_encoded_samples['token_type_ids'][chunck_id]])
            answer, answer_prob = self._get_answer(input_id_chunck,attention_mask_chunck,token_type_chunck)
            #searching the answer with best prob on chuncks
            if context_id not in context_ids_list:
                question_list.append(question)
                context_list.append(context)
                answer_list.append(answer)
                answer_prob_list.append(answer_prob)
            else:
                if (answer not in ['[CLS]','[SEP]']) and (answer_prob>answer_prob_list[context_id]):
                    answer_list[context_id] = answer
                    answer_prob_list[context_id] = answer_prob
                    

            context_ids_list.append(context_id)

        df_result = pd.DataFrame({
                                'question': question_list,
                                'context': context_list,
                                'answer': answer_list,
                                'answer_prob': answer_prob_list})
        
        
        df_result['index'] = df_result.index        
        
        df_result = df_result.sort_values(by='answer_prob', ascending=False).reset_index(drop=True)
                                    
        return df_result
      

    def load_model(self,**kwargs):
        def verify_args(checkpoint_path):
            if not checkpoint_path:
                raise ValueError("checkpoint_path é um argumento obrigatório")

        # Checagem das Chamadas
        if not (self.build_called ):
            raise AssertionError("Para chamar o método load é nececssário chamar o método build")
        self.load_called = True

        # Recuperando variáveis kwargs
        checkpoint_path = kwargs.get('checkpoint_path',None)
        verify_args(checkpoint_path)

        # Atualizando parâmetros de treinamento
        hparams = self.hparams.copy()
        #hparams['tokenizer'] = self.tokenizer
        hparams['device'] = self.device
        hparams['testing'] = True
        datasets = {}

        # Carrgando o modelo
        self.MODEL = Reader.load_from_checkpoint(checkpoint_path = checkpoint_path,map_location=self.device,hparams=hparams,datasets=datasets)
        self.MODEL.to(self.device)

    def train(self,**kwargs):
        def verify_args(train_path,valid_path,test_path):
            if not train_path:
                raise ValueError("train_path é um argumento obrigatório")
            if not valid_path:
                raise ValueError("valid_path é um argumento obrigatório")
            if not test_path:
                raise ValueError("test_path é um argumento obrigatório")
        
        # Checagem das Chamadas
        if not (self.build_called ):
            raise AssertionError("Para chamar o método train é nececssário chamar o método build")
        self.train_called = True

        # Recuperando variáveis kwargs
        MODEL_PATH = kwargs.get('MODEL_PATH',None)
        train_path = kwargs.get('train_path',None)
        valid_path = kwargs.get('valid_path',None)
        test_path = kwargs.get('test_path',None)
        verify_args(train_path,valid_path,test_path)

        # Criando datasets
        df_result_train= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,train_path))
        df_result_valid= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,valid_path))
        df_result_test= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,test_path))
        train_dataset = CustomDataset(
                            df = df_result_train,
                            tokenizer = self.tokenizer,
                            max_length = self.max_length,
                            stage= 'Experiment')
            
        valid_dataset = CustomDataset(
                            df = df_result_valid,
                            tokenizer = self.tokenizer,
                            max_length = self.max_length,
                            stage= 'Experiment')

        test_dataset = CustomDataset(
                            df = df_result_test,
                            tokenizer = self.tokenizer,
                            max_length = self.max_length,
                            stage= 'Experiment')
        
        # Atualizando parâmetros de treinamento
        hparams = self.hparams.copy()
        hparams['testing'] = False
        #hparams['tokenizer'] = self.tokenizer
        hparams['device'] = self.device
        
        datasets = {}
        datasets['train_dataset'] = train_dataset
        datasets['valid_dataset'] = valid_dataset
        datasets['test_dataset'] = test_dataset

       # Checando se o trainamento será feito do zero ou a partir de um treinamento interrompido
        if MODEL_PATH:
            self.MODEL = Reader.load_from_checkpoint(
            checkpoint_path = MODEL_PATH,
            map_location=self.device,
            hparams=hparams,
            datasets=datasets,
            )
        else:
            self.MODEL = Reader(
            hparams=hparams,
            datasets=datasets,
            )

        # Treinando Algorítimos
        self.TRAINER.fit(self.MODEL)

        return self.MODEL        

    def evaluate(self,**kwargs):
        # Checagem das Chamadas
        if not (self.build_called and (self.train_called or self.load_called)):
            raise AssertionError("Para chamar o método evaluate é nececssário chamar o método build e em seguida o método train ou o método load")

        #Testando
        self.TRAINER.test(self.MODEL)


    ###########################################################################
    #                                                                         #
    #                       Not Required Visible Methods                      #
    #                                                                         #
    ###########################################################################
    
    def prepare_data(self,**kwargs):
        def verify_args(squad_train_path,squad_dev_path):
            if not squad_train_path:
                raise ValueError("squad_train_path é um argumento obrigatório")
            if not squad_dev_path:
                raise ValueError("squad_dev_path é um argumento obrigatório")

        # Recuperando variáveis kwargs
        squad_train_path = kwargs.get('squad_train_path',None)
        squad_dev_path = kwargs.get('squad_dev_path',None)
        verify_args(squad_train_path,squad_dev_path)

        # Convertendo Json em Dataframe
        train_json = self.io_utils.read_json(os.path.join(self.data_dirpath,squad_train_path))
        dev_json = self.io_utils.read_json(os.path.join(self.data_dirpath,squad_dev_path))
        self._read_squad_json_as_dataframe(train_json)
        df_train =  self._read_squad_json_as_dataframe(train_json)
        df_dev =  self._read_squad_json_as_dataframe(dev_json)
        df_valid, df_test = train_test_split(df_dev, test_size=self.test_size_from_dev)

        # Chunck dataset
        df_result_train = self._convert_tokenized_examples_to_dataset(df=df_train)
        df_result_valid = self._convert_tokenized_examples_to_dataset(df=df_valid)
        df_result_test = self._convert_tokenized_examples_to_dataset(df=df_test)
        
        # Chunck dataset
        df_result_train = df_result_train[:10]
        df_result_valid = df_result_valid[:10]
        df_result_test = df_result_test[:10]

        # Salvando dados
        train_output = os.path.join(self.data_dirpath,'df_squad_train_bert_chuncked.csv')
        valid_output = os.path.join(self.data_dirpath,'df_squad_valid_bert_chuncked.csv')
        test_output = os.path.join(self.data_dirpath,'df_squad_test_bert_chuncked.csv')
        df_result_train.to_csv(os.path.join(train_output),index=False)
        df_result_valid.to_csv(os.path.join(valid_output),index=False)
        df_result_test.to_csv(os.path.join(test_output),index=False)
        
        return {
                'prepared_data_train_path':train_output,
                'prepared_data_valid_path':valid_output,
                'prepared_data_test_path':test_output,
                }
    
    def save_checkpoint(self,checkpoint_path):
        # Checagem das Chamadas
        if not (self.train_called):
            raise AssertionError("Para chamar o método save_checkpoint é nececssário chamar o método train")
            
        self.TRAINER.save_checkpoint(checkpoint_path)
        
    ###########################################################################
    #                                                                         #
    #                       Not Required Internal Methods                     #
    #                                                                         #
    ###########################################################################

    def _chunckfy_with_stride(self,list_questions,list_contexts):

        #Para retornar tensor precisa truncar ou fazer padding
        chunckfied_encoded_samples = self.tokenizer(
        list_questions,
        list_contexts,
        max_length=self.max_length,
        truncation="only_second",
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        stride=self.doc_stride,
        #   return_tensors='pt',
        )

        return chunckfied_encoded_samples

    def _get_answer(self,input_id_chunck,attention_mask_chunck,token_type_chunck):
        
        input_id_chunck = torch.tensor(input_id_chunck).to(torch.long).to(self.device)
        attention_mask_chunck = torch.tensor(attention_mask_chunck).to(torch.long).to(self.device)
        token_type_chunck = torch.tensor(token_type_chunck).to(torch.long).to(self.device)

        output = self.MODEL.forward(token_ids = input_id_chunck,
                                                      attention_mask = attention_mask_chunck,
                                                      token_type_ids=token_type_chunck
                                                      )
        pred_start_logit = output['start_logits']
        pred_end_logit = output['end_logits']
        
        answer_prob = (self.softmax(pred_start_logit).max().item() + self.softmax(pred_end_logit).max().item())/2
        pred_start_position = pred_start_logit.argmax().item()
        pred_end_position = pred_end_logit.argmax().item()
        answer = self.tokenizer.decode(input_id_chunck.ravel()[pred_start_position:pred_end_position+1])

        #answer = '' if answer in ['[CLS]','[SEP]'] else answer

        return answer, answer_prob

    def _prepare_train_features(self,df):
        
        # Tokenize Examples
        tokenized_examples = self._chunckfy_with_stride(list(df["question"]),list(df["context"]))

        # Since one example might give us several features if it has a long context, we need a map from a feature to
        # its corresponding example. This key gives us just that.
        sample_mapping = tokenized_examples.pop("overflow_to_sample_mapping")
        offset_mapping = tokenized_examples.pop("offset_mapping")

        # sample_mapping = tokenized_examples["overflow_to_sample_mapping"]
        # offset_mapping = tokenized_examples["offset_mapping"]

        # Let's label those examples!
        tokenized_examples["start_positions"] = []
        tokenized_examples["end_positions"] = []

        for i, offsets in enumerate(offset_mapping):
            
            # We will label impossible answers with the index of the CLS token.
            input_ids = tokenized_examples["input_ids"][i]
            

            cls_index = input_ids.index(self.tokenizer.cls_token_id)


            # Grab the sequence corresponding to that example (to know what is the context and what is the question).
            sequence_ids = tokenized_examples.sequence_ids(i)

            
            # One example can give several spans, this is the index of the example containing this span of text.
            sample_index = sample_mapping[i]
            answer = df["answer"].iloc[sample_index]
            answer_start = df["answer_start"].iloc[sample_index]
            
            # If no answers are given, set the cls_index as answer.
            if not answer_start:
                tokenized_examples["start_positions"].append(cls_index)
                tokenized_examples["end_positions"].append(cls_index)
            else:
                # Start/end character index of the answer in the text.
                start_char = answer_start
                end_char = start_char + len(answer)

                # Start token index of the current span in the text.
                token_start_index = 0
                while sequence_ids[token_start_index] !=1:
                    token_start_index += 1

                # End token index of the current span in the text.
                token_end_index = len(input_ids) - 1
                while sequence_ids[token_end_index] != 1:
                    token_end_index -= 1

                # Detect if the answer is out of the span (in which case this feature is labeled with the CLS index).
                if not (offsets[token_start_index][0] <= start_char and offsets[token_end_index][1] >= end_char):
                    tokenized_examples["start_positions"].append(cls_index)
                    tokenized_examples["end_positions"].append(cls_index)
                else:
                    # Otherwise move the token_start_index and token_end_index to the two ends of the answer.
                    # Note: we could go after the last offset if the answer is the last word (edge case).
                    while token_start_index < len(offsets) and offsets[token_start_index][0] <= start_char:
                        token_start_index += 1
                    tokenized_examples["start_positions"].append(token_start_index - 1)
                    while offsets[token_end_index][1] >= end_char:
                        token_end_index -= 1
                    tokenized_examples["end_positions"].append(token_end_index + 1)

        return tokenized_examples


    def _convert_tokenized_examples_to_dataset(self,df):        
        questions_list = []
        context_list = []
        answer_start_position_list = []
        answer_end_position_list = []
        n_splits =  len(df)//self.batch_dataset_preparation
        for chunk in np.array_split(df, n_splits):
            tokenized_examples = self._prepare_train_features(chunk)
            for input_ids in tokenized_examples['input_ids']:
                text = self.tokenizer.decode(input_ids)
                text_parts = text.split(self.tokenizer.sep_token)
                question = text_parts[0].split(self.tokenizer.cls_token)[1].strip()
                context = text_parts[1].strip()
                questions_list.append(question)
                context_list.append(context)        

            answer_start_position_list += tokenized_examples['start_positions']
            answer_end_position_list += tokenized_examples['end_positions']
        
        df_result = pd.DataFrame({'context': context_list, 'question': questions_list, 'answer_start': answer_start_position_list, 'answer_end': answer_end_position_list})
        return df_result

    def _read_squad_json_as_dataframe(self,json_file):

        context, question, answer, answer_start = [], [], [], []

        for d in json_file['data']:

            for c in d['paragraphs']:
                
                for q in c['qas']:
                    
                    for a in q['answers']:
                        
                        context.append(c['context'])
                        question.append(q['question'])
                        answer.append(a['text'])
                        answer_start.append(a['answer_start'])

        df = pd.DataFrame({'context': context, 'question': question, 'answer': answer, 'answer_start': answer_start})

        return df
 
    
# if __name__ == '__main__':

#     import os
#     data_dir  =  root_dir = os.getcwd()
#     logs_dir = os.path.join(root_dir,"lightning_logs")

#     # Colocando parâmetros de entrada no fromato esperado
#     hparams = {
#         "model_name":model_name,
#         "train_batch_size":train_batch_size,
#         "eval_batch_size":eval_batch_size,
#         "max_length":max_length,
#         "doc_stride":doc_stride,
#         "learning_rate":learning_rate,
#         "eps":eps,
#         "seed":seed,

#     }

#     lightning_params = {
#         "num_gpus":num_gpus,
#         "profiler":profiler,
#         "max_epochs":max_epochs,
#         "accumulate_grad_batches":accumulate_grad_batches,
#         "check_val_every_n_epoch":check_val_every_n_epoch,
#         "progress_bar_refresh_rate":progress_bar_refresh_rate,
#         "gradient_clip_val":gradient_clip_val,
#         "fast_dev_run":fast_dev_run,
#     }


#     early_stop_callback_params = {
#          "monitor":monitor,
#         "min_delta":min_delta,
#         "patience":patience,
#         "verbose":verbose,
#         "mode":mode,    
#     }

#     prepare_data_params = {
#          "batch_dataset_preparation":batch_dataset_preparation,
#          "test_size_from_dev":test_size_from_dev,
#     }

#     # Configurações
#     config = {'params':{'hparams':hparams,
#                         'lightning_params':lightning_params,
#                         'early_stop_callback_params':early_stop_callback_params,
#                         'prepare_data_params':prepare_data_params },

#             'dirpaths':{'data_dirpath':data_dir,
#                     'log_dirpath':logs_dir,
#                     'cwd_dirpath':root_dir},
#     }

#     # Criando Caller
#     reader_caller = Reader_Caller(config)
#     reader_caller.build()

#     #Preparando dados
#     squad_train_path = os.path.join(data_dir,'squad-train-v1.1.json')
#     squad_dev_path= os.path.join(data_dir,'squad-dev-v1.1.json')
#     #prepared_datapaths = reader_caller.prepare_data(squad_train_path=squad_train_path,
#     #                                                squad_dev_path=squad_dev_path)
#     prepared_datapaths = {
#     "prepared_data_train_path":os.path.join(data_dir,'df_squad_train_bert_chuncked.csv'),
#     "prepared_data_valid_path":os.path.join(data_dir,'df_squad_valid_bert_chuncked.csv'),
#     "prepared_data_test_path":os.path.join(data_dir,'df_squad_test_bert_chuncked.csv'),
#                             }
#     # Treinamento
#     _ = reader_caller.train(train_path=prepared_datapaths['prepared_data_train_path'],
#                                 valid_path=prepared_datapaths['prepared_data_valid_path'],
#                                 test_path=prepared_datapaths['prepared_data_test_path'])
#     # Avaliação
#     reader_caller.evaluate()

#     # reader_caller.load_model(checkpoint_path=os.path.join(data_dir,'epoch=0-step=0.ckpt'))

#     # Testando Exemplo
#     io_utils = IO_Utils()
#     report_contenst_txt_path = os.path.join(data_dir,'..','pdf_info_extractor','reports_contexts_texts.txt')
#     contexts_texts = io_utils.read_line_spaced_txt_file(filepath=report_contenst_txt_path)
#     topn_contexts = contexts_texts[:10]
#     df_result = reader_caller.forward(question="Qual o melhor herbicida contra erva da ninha ?",topn_contexts=topn_contexts)
    
#     import pdb;pdb.set_trace()