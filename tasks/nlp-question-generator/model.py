import torch
from tqdm import tqdm
from multiprocessing import cpu_count
from typing import List, Union, Optional
import numpy as np
import pandas as pd
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from transformers import T5ForConditionalGeneration
from vident.qgenerator.metrics_calculator import Glove_Embeddings_Comparer, Metrics_Calculator

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
        self.model.to(self.hparams.device)

        # #----------Metrics Trackers
        # if self.hparams.track_metrics == True:
        #     glove_comparer = Glove_Embeddings_Comparer(glove_weights_path=self.hparams.glove_weights_path,device=self.hparams.device)
        #     self.valid_metrics_calculator = Metrics_Calculator(self.hparams,glove_comparer)
        #     self.test_metrics_calculator = Metrics_Calculator(self.hparams,glove_comparer)
    

    def forward(self, source_token_ids, source_mask, target_token_ids=None,
                target_mask=None,info_requested='loss',num_gen_sentences = None):
        

        if info_requested=='loss':

            # TODO calcular a loss dado os target_token_ids
            outputs = self.model(input_ids = source_token_ids, attention_mask = source_mask,labels = target_token_ids)
            
            
            # loss, predicted_token_ids = outputs[:2]
            loss = outputs[0]
            result =  loss
        if info_requested=='logits':
            #num_return_sequences must be 1
            if info_requested=='logits':

                num_gen_sentences = num_gen_sentences if num_gen_sentences else self.hparams.num_gen_sentences

                decoder_output = self.model.generate(
                                input_ids =source_token_ids,
                                attention_mask=source_mask, 
                                max_length= self.hparams.target_max_length,
                                do_sample=True,  
                                num_return_sequences=num_gen_sentences,
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
        batch_metrics_dict = {}
        batch_metrics_dict['train_loss'] = loss.item() 
        batch_metrics_dict = {'loss':loss}
        return batch_metrics_dict

   
    def validation_step(self, batch, batch_nb):
        # batch
        source_token_ids, source_masks, target_token_ids, target_masks, original_sources, original_targets = batch
         
        # fwd
        loss = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='loss')
        #logits = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='logits')

        batch_metrics_dict = {}
        batch_metrics_dict['valid_loss'] = loss.item() 

        #include special values to batch metrics dict
        batch_metrics_dict['loss']  = loss

        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict

    def test_step(self, batch, batch_nb):

        # batch
        source_token_ids, source_masks, target_token_ids, target_masks, original_sources, original_targets = batch

        # fwd
        #logits = self.forward(source_token_ids, source_masks, target_token_ids,info_requested='logits')

        #Calc Metrics and Saving Results
        batch_metrics_dict = {}


        #include special values to batch metrics dict
        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict
    
    def get_epoch_results(self,outputs,step='train'):
        
        tensorboard_logs = {}

        if step != "test":
            temp_avg_loss_batch = [x["loss"] for x in outputs]
            avg_loss = torch.stack(temp_avg_loss_batch).mean()
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
        shuffle = False if self.hparams.overfit else True
        return DataLoader(self.hparams.train_dataset, batch_size=self.hparams.train_batch_size, shuffle=shuffle,num_workers=cpu_count())
    
    def val_dataloader(self):

        return DataLoader(self.hparams.valid_dataset, batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())
    
    def test_dataloader(self):

        return DataLoader(self.hparams.test_dataset, batch_size=self.hparams.eval_batch_size,shuffle=False, num_workers=cpu_count())

