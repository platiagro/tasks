import os
import torch
from torchvision import datasets, transforms

import archive
from augmentations import *


class Augmentation(object):
    def __init__(self, policies):
        self.policies = policies

    def __call__(self, img):
        for _ in range(1):
            policy = random.choice(self.policies)
            for name, pr, level in policy:
                if random.random() > pr:
                    continue
                img = apply_augment(img, name, level)
        return img

class LoadData():
    """
    Class responsable for loading data,
    apply necessary transforms and 
    create data loader for train and test
    """
    def __init__(self, dataroot):
        self.dataroot = dataroot

    # Use imagenet data format
    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        'test': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    }

    def load_data_train(self, aug_police=None):
        """Load data for training and apply transforms to dataset"""
        if aug_police:
            augment_object = getattr(archive, aug_police)
            for x in ['train', 'val']:
                self.data_transforms[x].transforms.insert(0, Augmentation(augment_object()))

        image_datasets = {
            x: datasets.ImageFolder(
                os.path.join(self.dataroot, x),
                self.data_transforms[x]) for x in ['train', 'val']}
        dataloaders = {
            x: torch.utils.data.DataLoader(
                image_datasets[x], batch_size=4,
                shuffle=True, num_workers=4) for x in ['train', 'val']}
        dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
        class_names = image_datasets['train'].classes

        return dataloaders, dataset_sizes, class_names

    def load_data_test(self, aug_police=None):
        """Load data for testing"""
        image_datasets = {
            x: datasets.ImageFolder(
                os.path.join(self.dataroot, x),
                self.data_transforms[x]) for x in ['test']}
        dataloaders = {
            x: torch.utils.data.DataLoader(
                image_datasets[x], batch_size=4,
                shuffle=True, num_workers=4) for x in ['test']}
        dataset_sizes = {x: len(image_datasets[x]) for x in ['test']}
        class_names = image_datasets['test'].classes
        print(class_names, dataset_sizes)
        return dataloaders, dataset_sizes, class_names
