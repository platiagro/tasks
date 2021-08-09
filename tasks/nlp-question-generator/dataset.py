import torch
import numpy as np
from typing import List, Union, Optional
from torch.utils.data import  Dataset

class CustomDataset(Dataset):
    def __init__(self,PREFIX,tokenizer,X_context:np.ndarray,y_question:Optional[np.ndarray]=[],
                 source_max_length: int = 32, target_max_length: int = 32,step="Experiment"):
        self.tokenizer = tokenizer
        self.X_context = X_context
        
        self.y_question = y_question
        self.source_max_length = min(source_max_length + len(PREFIX.split(' ')),512)
        self.target_max_length = target_max_length
        self.step = step
        self.PREFIX = PREFIX
        

        if step == "Experiment" and len(y_question)==0:
          raise Exception("Na fase de experimento o componente tem de haver um y de referência")

        
        if step == "Deployment" and len(y_question)>0:
          raise Exception("Na fase de implantação o componente tem deve possuir y=None")

    def __len__(self):
        return len(self.X_context)
    
    def __getitem__(self, idx):
        #Source
        original_source = self.X_context[idx]
        source = f"{self.PREFIX} {original_source}"
        source_encoder = self.encoder_plus(source,self.source_max_length)
        source_token_ids = source_encoder['input_ids']
        source_mask = source_encoder['attention_mask']
        source_token_ids = torch.tensor(source_token_ids).type(torch.long)
        source_mask = torch.tensor(source_mask).type(torch.long)

        if self.step=="Experiment":
          # Target
          original_target = self.y_question[idx]
          target = f"{original_target}"
          target_encoder = self.encoder_plus(target,self.target_max_length)
          target_token_ids = target_encoder['input_ids']
          target_mask = target_encoder['attention_mask']
          target_token_ids = torch.tensor(target_token_ids).type(torch.long)
          target_mask = torch.tensor(target_mask).type(torch.long)

          retorno = (source_token_ids, source_mask, target_token_ids, target_mask, original_source, original_target)
          
        if self.step=="Deployment":
          retorno = (source_token_ids, source_mask, original_source)

        return retorno
    
    def encoder_plus(self,text,L):
        #padding - max_length:de acordo com o atributo max_length - True: maior sentença no batch
        #é preciso avaliar a performance disso. O True me parece melhor e o max_lenth me parece 
        # com maiores chances de funcionar
        return self.tokenizer.encode_plus(text,
                                          max_length = L,
                                          truncation=True,
                                          padding="max_length")