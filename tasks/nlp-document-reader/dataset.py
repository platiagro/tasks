import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, df, tokenizer, max_length,stage='Experiment'):
        self.stage = stage
        self.tokenizer = tokenizer
        self.df = df
        self.max_length = max_length
        self.verify_args()


    def verify_args(self):
        possible_stages = ['Experiment','Deployment']
        if self.stage not in possible_stages:
            raise ValueError(f"{self.stage} should be on of {possible_stages}")

    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        row = self.df.iloc[idx]

        #Encoder
        encoder_plus = self.encoder_plus(row['question'],row['context'])
        token_ids = encoder_plus['input_ids'].squeeze()
        attention_mask = encoder_plus['attention_mask'].squeeze()
        token_type_ids = encoder_plus['token_type_ids'].squeeze()
  
        #tranformacao para tensor

        if self.stage == 'Experiment':

            start_positions = torch.tensor(row['answer_start']).type(torch.long)
            end_positions = torch.tensor(row['answer_end']).type(torch.long)

            retorno =  token_ids, attention_mask, token_type_ids, start_positions, end_positions
        else:
            retorno = token_ids, attention_mask, token_type_ids
        
        return retorno
    #already truncate and paded
    def encoder_plus(self,question,context):
        return self.tokenizer.encode_plus(text=question,
                                          text_pair=context,
                                          max_length = self.max_length,
                                          padding='max_length',
                                          return_tensors='pt',
                                          truncation ='only_second'
                                          )