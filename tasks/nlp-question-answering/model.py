import os
import sys
import torch
import numpy as np
#from nlgeval import NLGEval
from multiprocessing import cpu_count
from transformers import AutoModelForQuestionAnswering
from torch.utils.data import DataLoader
import pytorch_lightning as pl



class Reader(pl.LightningModule):

    def __init__(self,hparams,datasets):
        super(Reader, self).__init__()

        self.hparams = hparams
        self.datasets = datasets
        pl.utilities.seed.seed_everything(seed = self.hparams.seed)

        # ---------- Model
        self.model = AutoModelForQuestionAnswering.from_pretrained(self.hparams.model_name)
            
    def predict(self):
        pass
    def forward(self,token_ids,attention_mask,token_type_ids,start_positions=None,end_positions=None):
        if self.hparams.testing  == False:
            output = self.model(input_ids=token_ids, attention_mask=attention_mask, token_type_ids=token_type_ids,start_positions=start_positions, end_positions=end_positions)
        else:
            output = self.model(input_ids=token_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        return output

    def training_step(self, batch, batch_idx):
        self.hparams.testing  = False
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids,start_positions,end_positions)
        loss = output['loss']
        #pred_start_logits = output['start_logits']
        #pred_end_logits = output['end_logits']
        batch_metrics_dict = {'loss':loss}

        return batch_metrics_dict

    def validation_step(self, batch, batch_idx):
        self.hparams.testing  = False
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids,start_positions, end_positions)
        loss = output['loss']
        pred_start_logits = output['start_logits']
        pred_end_logits = output['end_logits']

        #Calc Metrics and Saving Results
        batch_metrics_dict = {}
        batch_metrics_dict['valid_loss'] = loss.item() 

        #include special values to batch metrics dict
        batch_metrics_dict['loss']  = loss

        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict
  

    def test_step(self, batch, batch_idx):
        self.hparams.testing  = True
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids)
        pred_start_logits = output['start_logits']
        pred_end_logits = output['end_logits']

        return batch_metrics_dict
    
    def training_epoch_end(self, outputs):
        if not outputs:
            return {}
        epoch_dict = self.get_epoch_results(outputs,'train')

    def validation_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'valid')
        #return epoch_dict #must do to save checkpoints

    def test_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'test')


    def get_epoch_results(self,outputs,step='train'):

        tensorboard_logs = {}

        if step != "test":
            temp_avg_loss_batch = [x["loss"] for x in outputs]
            avg_loss = torch.stack(temp_avg_loss_batch).mean()
            tensorboard_logs[f"avg_{step}_loss"] =  avg_loss.item()
            
        for key, value in tensorboard_logs.items():
            self.log(key, value, on_epoch=True, prog_bar=True, logger=True)

        return tensorboard_logs

    def configure_optimizers(self):
        return torch.optim.AdamW(
            [p for p in self.parameters() if p.requires_grad],
            lr=self.hparams.learning_rate, eps=self.hparams.eps)

    def train_dataloader(self):

        # shuffle = False if self.hparams.overfit else True
        return DataLoader(self.datasets['train_dataset'], batch_size=self.hparams.train_batch_size, shuffle=True,num_workers=cpu_count())

    def val_dataloader(self):
        return DataLoader(self.datasets['valid_dataset'], batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())

    def test_dataloader(self):
        return DataLoader(self.datasets['test_dataset'], batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())