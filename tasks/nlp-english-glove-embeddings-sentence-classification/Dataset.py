from torch.utils.data import Dataset
from numpy import genfromtxt
import torch

class ImdbDataset(Dataset):
    def __init__(self, X, X_words,target = None,step = "Experiment"):
        super(ImdbDataset, self).__init__()

        self.x = [torch.tensor(line).type(torch.LongTensor) for line in X ]
        self.words = X_words
        self.step = step
        if step == "Experiment":
            self.target = torch.tensor(target).type(torch.LongTensor) 


    def __len__(self):
        return len(self.x)
  
    def __getitem__(self, index):
        if self.step == "Experiment":
            return self.x[index], self.words[index], self.target[index]
        if self.step == "Deployment":
            return self.x[index], self.words[index]
