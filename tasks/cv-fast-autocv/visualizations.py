import torch
import numpy as np
import matplotlib.pyplot as plt


class ImageVisualization():
    # interactive mode
    plt.ion()

    def __init__(self, device, dataloaders, path):
        self.device = device
        self.dataloaders = dataloaders
        self.path = path

    def imshow(self, inp, title=None):
        inp = inp.numpy().transpose((1, 2, 0))
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        inp = std * inp + mean
        inp = np.clip(inp, 0, 1)

        plt.imshow(inp)
        if title is not None:
            plt.title(title)

        out_path = self.path + str(title) + '.png'
        plt.savefig(out_path)

    def visualize_model(self, model, class_names, num_images=6):
        was_training = model.training
        model.eval()
        images_so_far = 0
        fig = plt.figure()

        with torch.no_grad():
            for i, (inputs, labels) in enumerate(self.dataloaders['val']):
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)

                for j in range(inputs.size()[0]):
                    images_so_far += 1
                    ax = plt.subplot(num_images//2, 2, images_so_far)
                    ax.axis('off')
                    ax.set_title('predicted: {}'.format(class_names[preds[j]]))
                    self.imshow(inputs.cpu().data[j])

                    if images_so_far == num_images:
                        model.train(mode=was_training)
                        return
            model.train(mode=was_training)

    def visualize_results(self, history, out_name):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,6))
        fig.suptitle("Loss and Acc of model: {0}".format(out_name), fontsize=14)

        # Loss graph
        for curve in ['train_epoch_loss', 'val_epoch_loss']:
            ax1.plot(history[curve], label=curve)
        ax1.legend()
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Loss')
        ax1.set_title('Training and Validation Losses')
        # Acc graph
        for curve in ['train_epoch_acc', 'val_epoch_acc']:
            ax2.plot(history[curve], label=curve)
        ax2.legend()
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Acc')
        ax2.set_title('Training and Validation Acc')

        out = self.path + out_name + '_loss_acc' + '.png'
        plt.savefig(out, bbox_inches='tight')
