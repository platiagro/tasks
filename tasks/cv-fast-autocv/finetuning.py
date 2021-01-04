from checkpoint import TrainedModels
from networks import CustomModule


class FineTuning():
  
    def __init__(self, model_archs, num_classes):
        self.model_archs = model_archs
        self.num_classes = num_classes
        self.trained_models = TrainedModels()

    def fine_tuning(self, model_arch):

        if model_arch in ['resnet18', 'resnet50']:
            model_conv = self.trained_models.get_model(model_arch)

            for param in model_conv.parameters():
                param.requires_grad = False

            num_ftrs = model_conv.fc.in_features
            net_out = CustomModule(num_ftrs, self.num_classes)
            model_conv.fc = net_out

        if model_arch in ['vgg16']:
            model_conv = self.trained_models.get_model(model_arch)
            for param in model_conv.parameters():
                param.requires_grad = False

            num_ftrs = model_conv.classifier[0].in_features
            net_out = CustomModule(num_ftrs, self.num_classes)
            model_conv.classifier = net_out
        return model_conv
