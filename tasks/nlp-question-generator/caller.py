import os
import gc
import sys
import yaml
import torch
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from transformers import T5Tokenizer
from multiprocessing import cpu_count
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint,EarlyStopping,GPUStatsMonitor

# Classes and functions from the project
from dataset import CustomDataset
from model import T5Finetuner
from io_utils import IO_Utils


#TODO: Precisa Fazer
class Qgenerator_caller():
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
        #-
        self.model_name = self.hparams['model_name']
        self.num_gen_sentences = self.hparams['num_gen_sentences']
        self.no_repeat_ngram_size = self.hparams['no_repeat_ngram_size']
        self.train_batch_size = self.hparams['train_batch_size']
        self.eval_batch_size = self.hparams['eval_batch_size']
        self.source_max_length = self.hparams['source_max_length']
        self.target_max_length = self.hparams['target_max_length']
        self.temperature = self.hparams['temperature']
        self.top_p = self.hparams['top_p']
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
        self.tokenizer = T5Tokenizer.from_pretrained(self.config['params']['hparams']['model_name'])
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.MODEL = None

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
    
    def free_memory(self):
        del self.MODEL
        del self.TRAINER
        del self.tokenizer
        del self.device
        del self.hparams
        del self.config
        gc.collect()
        torch.cuda.empty_cache()

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
        hparams['device'] = self.device
        hparams['track_metrics'] = False

        # Carrgando o modelo
        self.MODEL = T5Finetuner.load_from_checkpoint(checkpoint_path = checkpoint_path,map_location=self.device,hparams=hparams)
        self.MODEL.to(self.device)

    def train(self,**kwargs):
        def verify_args(train_path,valid_path,test_path,glove_weights_path):
            if not train_path:
                raise ValueError("train_path é um argumento obrigatório")
            if not valid_path:
                raise ValueError("valid_path é um argumento obrigatório")
            if not test_path:
                raise ValueError("test_path é um argumento obrigatório")
            if not glove_weights_path:
                raise ValueError("glove_weights_path é um argumento obrigatório")
        
        # Checagem das Chamadas
        if not (self.build_called ):
            raise AssertionError("Para chamar o método train é nececssário chamar o método build")
        self.train_called = True

        # Recuperando variáveis kwargs
        MODEL_PATH = kwargs.get('MODEL_PATH',None)
        train_path = kwargs.get('train_path',None)
        valid_path = kwargs.get('valid_path',None)
        test_path = kwargs.get('test_path',None)
        glove_weights_path = kwargs.get('glove_weights_path',None)
        verify_args(train_path,valid_path,test_path,glove_weights_path)

        # Criando datasets
        df_result_train= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,train_path))
        df_result_valid= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,valid_path))
        df_result_test= self.io_utils.read_csv_to_df(filepath=os.path.join(self.data_dirpath,test_path))
    
        X_train,y_train = np.array(df_result_train['context']),np.array(df_result_train['question'])
        X_valid,y_valid = np.array(df_result_valid['context']),np.array(df_result_valid['question'])
        X_test ,y_test  = np.array(df_result_test['context']),np.array(df_result_test['question'])
            
        train_dataset = CustomDataset(PREFIX=self.hparams['PREFIX'],
            tokenizer=self.tokenizer,
            X_context=X_train,
            y_question=y_train,
            source_max_length=self.hparams['source_max_length'],
            target_max_length=self.hparams['target_max_length'],
            step='Experiment',
        )

        valid_dataset = CustomDataset(PREFIX=self.hparams['PREFIX'],
                    tokenizer=self.tokenizer,
                    X_context=X_valid,
                    y_question=y_valid,
                    source_max_length=self.hparams['source_max_length'],
                    target_max_length=self.hparams['target_max_length'],
                    step='Experiment',
            )

        test_dataset = CustomDataset(PREFIX=self.hparams['PREFIX'],
                tokenizer=self.tokenizer,
                X_context=X_test,
                y_question=y_test,
                source_max_length=self.hparams['source_max_length'],
                target_max_length=self.hparams['target_max_length'],
                step='Experiment',
            )

        
        # Atualizando parâmetros de treinamento
        hparams = self.hparams.copy()
        hparams['tokenizer'] = self.tokenizer
        hparams['device'] = self.device
        hparams['glove_weights_path'] = glove_weights_path
        hparams['overfit'] = False
        hparams['track_metrics'] = True
        hparams['train_dataset'] = train_dataset
        hparams['valid_dataset'] = valid_dataset
        hparams['test_dataset'] = test_dataset

       # Checando se o trainamento será feito do zero ou a partir de um treinamento interrompido
        if MODEL_PATH:
            self.MODEL = T5Finetuner.load_from_checkpoint(
            checkpoint_path = MODEL_PATH,
            map_location=self.device,
            hparams=hparams
            )
        else:
            self.MODEL = T5Finetuner(
            hparams=hparams
            )

        # Treinando Algorítimos
        self.TRAINER.fit(self.MODEL)
  
    def save_checkpoint(self,checkpoint_path):
        # Checagem das Chamadas
        if not (self.train_called):
            raise AssertionError("Para chamar o método save_checkpoint é nececssário chamar o método train")
            
        self.TRAINER.save_checkpoint(checkpoint_path)
        
    def evaluate(self,**kwargs):
        # Checagem das Chamadas
        if not (self.build_called and (self.train_called or self.load_called)):
            raise AssertionError("Para chamar o método evaluate é nececssário chamar o método build e em seguida o método train ou o método load")

        #Testando
        self.TRAINER.test(self.MODEL)
        
        # Salvando os resultados
        valid_results_output_path =  os.path.join(self.log_dirpath,'valid_results.json')
        test_results_output_path =  os.path.join(self.log_dirpath,'test_results.json')
        valid_results = self.MODEL.valid_metrics_calculator.list_dict_track
        test_results = self.MODEL.test_metrics_calculator.list_dict_track
        self.io_utils.dump_json(filepath=valid_results_output_path,d=valid_results)
        self.io_utils.dump_json(filepath=test_results_output_path,d=test_results)

        return {'valid_results':valid_results,
                'test_results':test_results
                }
                        
    def forward(self,**kwargs):

        def verify_args(contexts,num_gen_sentences):
      
            if not all(isinstance(elem, str) for elem in contexts):
                raise ValueError(f"contexts deve ser uma lista de strings mas é {contexts}")
            if not num_gen_sentences:
                raise ValueError("contexts é um argumento obrigatório")

        # Checagem das Chamadas
        if not (self.build_called and (self.train_called or self.load_called)):
            raise AssertionError("Para chamar o método forward é nececssário chamar o método build e em seguida o método train ou o método load")

        # Recuperando variáveis kwargs
        num_gen_sentences = kwargs.get('num_gen_sentences',None)
        contexts = kwargs.get('contexts',None)
        verify_args(contexts,num_gen_sentences)

        X_test = np.array(contexts)

        inference_dataset = CustomDataset(PREFIX=self.hparams['PREFIX'],
                tokenizer=self.tokenizer,
                X_context=X_test,
                y_question=[],
                source_max_length=self.hparams['source_max_length'],
                target_max_length=self.hparams['target_max_length'],
                step='Deployment',
            )
        
        
        with torch.no_grad():
            
            self.MODEL.eval()
            self.MODEL.to(self.device)
            inference_dataloader = DataLoader(inference_dataset, batch_size=self.hparams['eval_batch_size'], shuffle=False,num_workers=cpu_count())

            result = {}
            j = 0
            for i,batch in enumerate(tqdm(inference_dataloader)):
                source_token_ids, source_masks, original_source = batch
                batch_size = len(original_source)
                source_token_ids = source_token_ids.to(self.device)
                source_masks = source_masks.to(self.device)
                logits = self.MODEL.forward(source_token_ids, source_masks,info_requested='logits',num_gen_sentences=num_gen_sentences)
                gen_quesitons = [self.tokenizer.decode(l, skip_special_tokens=True) for l in logits]
                questions_per_context = [gen_quesitons[s:s+num_gen_sentences] for s in list(range(0,len(gen_quesitons),num_gen_sentences))]
                result_batch = {f'{j+k}':{'context':original_source[k],'questions':questions_per_context[k]} for k in range(batch_size)}
                result.update(result_batch)
                j += batch_size
                

        return result        

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
        df_result_train = df_train #self._convert_tokenized_examples_to_dataset(df=df_train)
        df_result_valid = df_valid #self._convert_tokenized_examples_to_dataset(df=df_valid)
        df_result_test = df_test #self._convert_tokenized_examples_to_dataset(df=df_test)
        #df_result = pd.concat([df_result_train, df_result_valid, df_result_test],ignore_index=True)
        

        # Salvando dados
        train_output = os.path.join(self.data_dirpath,'squad-train-v1.1.csv')
        valid_output = os.path.join(self.data_dirpath,'squad-valid-v1.1.csv')
        test_output = os.path.join(self.data_dirpath,'squad-test-v1.1.csv')
        #complete_output = os.path.join(self.data_dirpath,'squad-v1.1.csv')
            
        df_result_train.to_csv(os.path.join(train_output),index=False)
        df_result_valid.to_csv(os.path.join(valid_output),index=False)
        df_result_test.to_csv(os.path.join(test_output),index=False)
        #df_result.to_csv(os.path.join(complete_output),index=False)
        
        return {
                'prepared_data_train_path':train_output,
                'prepared_data_valid_path':valid_output,
                'prepared_data_test_path':test_output,
                }
    
    def _apply_preprocessing(self,text):
        text = " ".join(text.split()).strip()
        return text
    
    def _read_squad_json_as_dataframe(self,json_file):

        context, question, answer, answer_start = [], [], [], []

        for d in json_file['data']:

            for c in d['paragraphs']:
                
                for q in c['qas']:
                    
                    for a in q['answers']:
                        
                        context.append(self._apply_preprocessing(c['context']))
                        question.append(self._apply_preprocessing(q['question']))
                        answer.append(self._apply_preprocessing(a['text']))
                        answer_start.append(a['answer_start'])

        df = pd.DataFrame({'context': context, 'question': question, 'answer': answer, 'answer_start': answer_start})

        return df

    def build_complete_json(self,gen_questions_dict,reports_contents):

        gen_questions_dict_copy = gen_questions_dict.copy()
        for k, v in gen_questions_dict.items():
            rp_infos = reports_contents[k]
            report_name = rp_infos['report_name']
            section_name = rp_infos['section_name']
            gen_questions_dict_copy[k]['report_name'] = report_name
            gen_questions_dict_copy[k]['section_name'] = section_name
        
        return gen_questions_dict_copy