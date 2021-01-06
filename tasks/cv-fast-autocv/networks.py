import torch.nn as nn
import torch.nn.functional as F


class CustomModule(nn.Module):
    """Class that constructs the final layers of models"""
    def __init__(self, input_features, num_classes):
        super(CustomModule, self).__init__()
        self.linear1 = nn.Linear(in_features=input_features, out_features=256, bias=True)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.4)
        self.linear2 = nn.Linear(in_features=256, out_features=num_classes, bias=True)
        self.softmax = nn.LogSoftmax()

    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.dropout(out)
        out = self.linear2(out)
        out = self.softmax(out)
        
        return out
