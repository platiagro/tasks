import os
import torch
import torchvision
import torch.nn as nn


class TrainedModels():

    def get_model(self, model_arch):
        switcher = {
            'resnet18': torchvision.models.resnet18(pretrained=True),
            'resnet50': torchvision.models.resnet50(pretrained=True),
            'vgg16': torchvision.models.vgg16(pretrained=True)
        }

        model = switcher.get(model_arch, lambda: 'Invalid model')
        return model

class Checkpoint():
    
    def __init__(self, dataset_id, multi_gpu, checkpoint_path=None):
        self.dataset_id = dataset_id
        self.multi_gpu = multi_gpu
        self.path = checkpoint_path
        self.trained_models = TrainedModels()

    def save_checkpoint(self, model_arch, aug_police, model):
        checkpoint = {
            'name': model_arch,
            'epochs': model.epochs,
        }

        if model.phase == 'val':
            checkpoint['best_acc'] = model.best_acc

        if model_arch in ['vgg16']:
            if self.multi_gpu:
                checkpoint['classifier'] = model.module.classifier
                checkpoint['state_dict'] = model.module.state_dict()
            else:
                checkpoint['classifier'] = model.classifier
                checkpoint['state_dict'] = model.state_dict()

        elif model_arch in ['resnet18', 'resnet50']:

            if self.multi_gpu:
                checkpoint['fc'] = model.module.fc
                checkpoint['state_dict'] = model.module.state_dict()
            else:
                checkpoint['fc'] = model.fc
                checkpoint['state_dict'] = model.state_dict()

        checkpoint['optimizer'] = model.optimizer
        checkpoint['optimizer_state_dict'] = model.optimizer.state_dict()
        model_name = "{0}_{1}_{2}".format(self.dataset_id, model_arch, aug_police)
        torch.save(checkpoint, os.path.join(self.path, model_name))

    def load_checkpoint(self, model_arch, checkpoint_path):

        checkpoint = torch.load(checkpoint_path)
        if model_arch in ['vgg16']:
            model = self.trained_models.get_model(model_arch)

            for param in model.parameters():
                param.requires_grad = False
            model.classifier = checkpoint['classifier']

        elif model_arch in ['resnet18', 'resnet50']:
            model = self.trained_models.get_model(model_arch)

            for param in model.parameters():
                param.requires_grad = False
            model.fc = checkpoint['fc']

        model.load_state_dict(checkpoint['state_dict'])
        
        total_params = sum(p.numel() for p in model.parameters())
        print(f'{total_params:,} total parameters.')
        total_trainable_params = sum(
            p.numel() for p in model.parameters() if p.requires_grad)
        print(f'{total_trainable_params:,} total gradient parameters.')

        if self.multi_gpu:
            model = nn.DataParallel(model)

        if torch.cuda.is_available():
            model = model.to('cuda')

        model.epochs = checkpoint['epochs']
        model.best_acc = checkpoint['best_acc']
        model.optimizer = checkpoint['optimizer']
        model.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        return model
