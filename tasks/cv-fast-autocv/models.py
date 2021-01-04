import os
import torch

import time
import copy

import numpy as np
from PIL import Image

from checkpoint import Checkpoint


class ModelInfos():
    def model_info(self, models_path):
        files = os.listdir(models_path)
        for fl in files:
            model = torch.load(models_path+fl)
            print('File Name:', fl)
            print('Best Acc:', '{0:.2f}'.format(model['best_acc'].cpu().numpy()))
            print('Epochs:', model['epochs'])
            print()


class Model():
    """Class responsable for models train and inference phases"""

    def __init__(self, model_arch, device, checkpoint=None):
        self.model_arch = model_arch
        self.checkpoint = checkpoint
        self.device = device

    def process_image(self, image_path):
        """Prepare single image for inference"""
        image = Image.open(image_path)
        img = image.resize((256, 256))

        # Center crop
        width = 256
        height = 256
        new_width = 224
        new_height = 224

        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        img = img.crop((left, top, right, bottom))

        # Convert to numpy, transpose color dimension and normalize
        img = np.array(img).transpose((2, 0, 1)) / 256

        # Standardization
        means = np.array([0.485, 0.456, 0.406]).reshape((3, 1, 1))
        stds = np.array([0.229, 0.224, 0.225]).reshape((3, 1, 1))
        img = img - means
        img = img / stds
        img_tensor = torch.Tensor(img)

        return img_tensor

    def train_model(
            self, model, police, dataloaders,
            dataset_sizes, criterion,
            optimizer, scheduler, num_epochs=25):
        """Train a model using data augmented with some set of polices"""
        since = time.time()
        model = model.to(self.device)
        best_model_wts = copy.deepcopy(model.state_dict())
        best_acc = 0.0
        print("\n######\nModel architecture: {0}\nPolice: {1}".format(self.model_arch, police))
        try:
            print('Epochs trained:', model.epochs)
            num_epochs = num_epochs - model.epochs
            history = model.history
        except:
            print('Start to training a model.')
            model.epochs = 0
            history = {}

        epoch = 1
        for epoch in range(1, num_epochs+1):
            model.epochs = model.epochs+1
            print('Epoch {}/{}\n'.format(epoch, num_epochs))

            # Each epoch has a training and validation phase
            for phase in ['train', 'val']:
                if phase == 'train':
                    model.train()  # Set model to training mode
                else:
                    model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0
                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    inputs = inputs.to(self.device)
                    labels = labels.to(self.device)

                    # zero the parameter gradients
                    optimizer.zero_grad()
                    # forward
                    # track history if only in train
                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()

                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)
                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]
                if not phase + '_epoch_loss' in history:
                    history[phase + '_epoch_loss'] = []
                    history[phase + '_epoch_acc'] = []

                history[phase + '_epoch_loss'] += [epoch_loss]
                acc = epoch_acc.cpu().numpy().tolist()
                history[phase + '_epoch_acc'] += [acc]
                print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))
                # deep copy the model
                if phase == 'val' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())
                    
                    model.best_acc = best_acc               
                    model.optimizer = optimizer
                    model.phase = phase
                    self.checkpoint.save_checkpoint(self.model_arch, police, model)
        print()
        model.history = history
        time_elapsed = time.time() - since
        print('Training completed in {:.0f}m {:.0f}s'.format(
            time_elapsed // 60, time_elapsed % 60))
        print('Best val Acc: {:.4f}'.format(model.best_acc))
        # load best model weights
        model.load_state_dict(best_model_wts)
        return model, float(model.best_acc)


    def predict_single_img(self, multi_gpu, model_path,
                           image_path, topk):
        """Run inference for a single image"""
        checkpoint = Checkpoint(self.model_arch, multi_gpu)
        model = checkpoint.load_checkpoint(self.model_arch, model_path)

        real_class = image_path.split('/')[-2]

        # Convert to pytorch tensor
        img_tensor = self.process_image(image_path)
        img_tensor = img_tensor.view(1, 3, 224, 224).to(self.device)

        with torch.no_grad():
            model.eval()
            out = model(img_tensor)
            ps = torch.exp(out)

            topk, topclass = ps.topk(topk, dim=1)
            topk_index = topclass.cpu().numpy()[0]
            topk_prob = topk.cpu().numpy()[0]

            return topk_index, topk_prob, real_class
    
    def predict_batch(self, multi_gpu, model_path,
                      dataloaders, dataset_sizes):
        """Run inference for test set of images"""
        checkpoint = Checkpoint(self.model_arch, multi_gpu)
        model = checkpoint.load_checkpoint(self.model_arch, model_path)
        model.eval()

        phase = 'test'
        running_corrects = 0
        running_wrongs = 0
        # Iterate over data.
        for inputs, labels in dataloaders[phase]:
            inputs = inputs.to(self.device)
            labels = labels.to(self.device)

            with torch.no_grad():
                outs = model(inputs)
                _, preds = torch.max(outs, 1)

            # statistics
            running_corrects += torch.sum(preds == labels.data)
            running_wrongs += torch.sum(preds != labels.data)
            acc = running_corrects.double() / dataset_sizes[phase]
        return int(running_corrects), int(running_wrongs), float(acc)
