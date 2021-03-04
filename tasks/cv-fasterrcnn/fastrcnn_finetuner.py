import functools
import traceback
import psutil
from multiprocessing import cpu_count

import pandas as pd
import numpy as np
import cv2

import torch
from torch.utils.data import DataLoader
import pytorch_lightning as pl
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator

import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

import metric
from averager import Averager


class FastRCNNFinetuner(pl.LightningModule):


    def __init__(self, 
                 hyperparams,
                 model_parameters,
                 dataset_infos,
                 extra_infos):

        super(FastRCNNFinetuner, self).__init__()

        #---------- hyperparams
        self.learning_rate = hyperparams['learning_rate']
        self.momentum = hyperparams['momentum']
        self.weight_decay = hyperparams['weight_decay']
        self.detection_threshold = hyperparams['detection_threshold']
        self.train_batch_size = hyperparams['train_batch_size']
        self.valid_batch_size = hyperparams['valid_batch_size']
        self.test_batch_size = hyperparams['test_batch_size']
        
        #---------- model_parameters
        self.num_classes = model_parameters['num_classes'] # 1 class (wheat) + background
        self.coord_format = model_parameters['coord_format'] # coco ou pascal_voc
        self.Averager = Averager
        self.loss_hist  = self.Averager()

        #---------- dataset_infos
        self.all_data = dataset_infos['all_data']
        self.DIR_TRAIN = dataset_infos['DIR_TRAIN']
        self.DIR_TEST = dataset_infos['DIR_TEST']
        self.CustomDataset = dataset_infos['CustomDataset']
        
        #---------- extra_infos
        self.overfit = extra_infos['overfit']
        
         #---------- other_infos
        self.predict_proba  =  torch.nn.Softmax(dim=1)
        self.step = 'Experiment'

        #---------- Dados para gráfico de Acurácia e Loss
        self.df_performance_train_batch = pd.DataFrame(columns=['train_batch_loss'])
        self.df_performance_train_epoch = pd.DataFrame(columns=['train_epoch_loss'])
        self.df_performance_valid_batch = pd.DataFrame(columns=['valid_batch_loss','valid_batch_iou'])
        self.df_performance_valid_epoch = pd.DataFrame(columns=['valid_epoch_loss','valid_epoch_iou'])
        self.df_performance_test_batch = pd.DataFrame(columns=['test_batch_iou'])
        self.df_performance_test_epoch = pd.DataFrame(columns=['test_epoch_iou'])


        #---------- Carregamento datasets
        if self.overfit:
            self.train_dataset = self.CustomDataset(self.all_data[0], self.DIR_TRAIN, self.get_train_transform())
            self.valid_dataset = self.CustomDataset(self.all_data[0], self.DIR_TRAIN, self.get_train_transform())
            self.test_dataset =  self.CustomDataset(self.all_data[0], self.DIR_TRAIN, self.get_train_transform())
        else:
            self.train_dataset = self.CustomDataset(self.all_data[0], self.DIR_TRAIN, self.get_train_transform())
            self.valid_dataset = self.CustomDataset(self.all_data[1], self.DIR_TRAIN, self.get_valid_transform())
            self.test_dataset =  self.CustomDataset(self.all_data[2], self.DIR_TRAIN, self.get_valid_transform())


        #---------- Resultados
        self.df_valid = pd.DataFrame(columns=['IMAGE_ID','PREDICTION_STRING','PRECISION_IOU'])
        self.df_test = pd.DataFrame(columns=['IMAGE_ID','PREDICTION_STRING','PRECISION_IOU'])
        self.result_valid = []
        self.result_test = []

        #---------- Preditor Fast-RCNN
        # load a model; pre-trained on COCO
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

        # get number of input features for the classifier
        in_features = self.model.roi_heads.box_predictor.cls_score.in_features

        # replace the pre-trained head with a new one
        self.model.roi_heads.box_predictor = FastRCNNPredictor(in_features, self.num_classes)


    def predict(self, df, image_dir):

        self.step = "Deployment"
        inference_dataset = self.CustomDataset(df, image_dir, self.get_test_transform(),step = self.step)
        dataloader = DataLoader(inference_dataset, batch_size=self.test_batch_size,shuffle=False, num_workers=cpu_count(),collate_fn=self.my_collate)    
        for batch in dataloader:
            self.test_step(batch, None)
        return self.df_test


    def forward(self, images, image_ids, targets = None, info_requested='loss'):
        
        if info_requested == 'loss':
          self.model.train()
          images = list(image for image in images)
          targets = [{k: v for k, v in t.items()} for t in targets]
          loss_dict = self.model(images, targets)
          losses = sum(loss for loss in loss_dict.values())
          loss_value = losses.item()
          self.loss_hist.send(loss_value)
          retorno = losses

        if info_requested == 'predictions':
          self.model.eval()
          results = []
          images = list(image for image in images)
          outputs = self.model(images)

          for i, image in enumerate(images):

              boxes = outputs[i]['boxes'].data.cpu().numpy()
              scores = outputs[i]['scores'].data.cpu().numpy()

              # Sort highest confidence -> lowest confidence
              boxes_sorted_idx = np.argsort(scores)[::-1]
              boxes = boxes[boxes_sorted_idx]
                            
              #eliminate boxes with scores under detection_threshold
              # if you enter model in pascal_voc it will output in pascal_voc
              boxes = boxes[scores >= self.detection_threshold].astype(np.int32)
              boxes_prediction_string = boxes.copy()
              scores = scores[scores >= self.detection_threshold]
              image_id = image_ids[i]
              
              #Converting from Pascal Voc to  COCO-> Only for prediction String
              boxes_prediction_string[:, 2] = boxes_prediction_string[:, 2] - boxes_prediction_string[:, 0]
              boxes_prediction_string[:, 3] = boxes_prediction_string[:, 3] - boxes_prediction_string[:, 1]
              
              result = {
                  'image_id': image_id,
                  'boxes':boxes,
                  'scores':scores,
                  'PredictionString': self.format_prediction_string(boxes_prediction_string, scores)
              }

              results.append(result)
          retorno = results

        return retorno
        
    def training_step(self, batch, batch_nb):

        # batch
        images, image_ids,targets  = batch
         
        # loss
        loss = self.forward(images, image_ids,targets,'loss')
        
        # What to log
        tensorboard_logs = {'loss': loss}

        self.df_performance_train_batch = self.df_performance_train_batch.append(pd.Series([loss.item()], index=self.df_performance_train_batch.columns ), ignore_index=True)

        return {'loss': loss, 'train_loss_batch': loss,'log': tensorboard_logs}
     
    
    def training_epoch_end(self, outputs):

        if not outputs: return {}
        
        temp_avg_loss_batch = [x['train_loss_batch'] for x in outputs]
  
        avg_train_loss = torch.stack(temp_avg_loss_batch).mean()

        self.df_performance_train_epoch = self.df_performance_train_epoch.append(pd.Series([avg_train_loss.item()], index=self.df_performance_train_epoch.columns ), ignore_index=True)

        tensorboard_logs = {'avg_train_loss': avg_train_loss}

        return {'log': tensorboard_logs}
 

    def validation_step(self, batch, batch_nb):

        # batch
        images, image_ids,targets  = batch
         
        # loss
        loss = self.forward(images, image_ids,targets,'loss')

        # Inference
        outputs = self.forward(images, image_ids,targets,'predictions')

        #constructing dataframe
        ious = np.zeros(len(targets))
        for iter in zip(enumerate(outputs),targets):
            i = iter[0][0]
            output = iter[0][1]
            target = iter[1]
            gts_boxes = target['boxes'].data.cpu().numpy().astype(np.int32)
            pred_boxes = output['boxes']
            image = images[i].permute(1,2,0).cpu().numpy()
            image_id = output['image_id']
            prediction_string = output['PredictionString']
            image_precision =  calculate_image_precision(gts_boxes, pred_boxes,(self.detection_threshold,),'pascal_voc')
            ious[i] = image_precision 
            self.df_valid = self.df_valid.append(pd.Series([image_id,prediction_string,image_precision], index=self.df_valid.columns), ignore_index=True)
            self.result_valid.append({'image_id':image_id,'image':image,'gts_boxes':gts_boxes, 'pred_boxes':pred_boxes})
        #mean batch dataframe
        mean_batch_ious = np.mean(ious)
        self.df_performance_valid_batch = self.df_performance_valid_batch.append(pd.Series([loss.item(),mean_batch_ious], index=self.df_performance_valid_batch.columns ), ignore_index=True)

        return {'valid_iou_batch': mean_batch_ious, 'valid_loss_batch': loss}


    def validation_epoch_end(self, outputs):

        if not outputs: return {}

        temp_avg_loss_batch = [x['valid_loss_batch'] for x in outputs]
        temp_avg_iou_batch = [x['valid_iou_batch'] for x in outputs]

        avg_valid_loss = torch.stack(temp_avg_loss_batch).mean()
        avg_valid_iou = np.mean(temp_avg_iou_batch)

        self.df_performance_valid_epoch = self.df_performance_valid_epoch.append(pd.Series([avg_valid_loss.item(),avg_valid_iou], index=self.df_performance_valid_epoch.columns ), ignore_index=True)

        tensorboard_logs = {'avg_valid_iou': avg_valid_iou,'avg_valid_loss': avg_valid_loss}

        return {'avg_valid_iou': avg_valid_iou, 'log': tensorboard_logs}


    def test_step(self, batch, batch_nb):

        to_return = None
        
        # batch
        if self.step == "Experiment":
            # batch
            images, image_ids,targets  = batch
            
            # Inference
            outputs = self.forward(images, image_ids,targets,'predictions')

            #constructing dataframe
            ious = np.zeros(len(targets))
            for iter in zip(enumerate(outputs),targets):
                i = iter[0][0]
                output = iter[0][1]
                target = iter[1]
                gts_boxes = target['boxes'].data.cpu().numpy().astype(np.int32)
                pred_boxes = output['boxes'].astype(np.int32)
                image = images[i].permute(1,2,0).cpu().numpy()
                image_id = output['image_id']
                prediction_string = output['PredictionString']
                image_precision =  calculate_image_precision(gts_boxes, pred_boxes,(self.detection_threshold,),'pascal_voc')
                ious[i] = image_precision 
                self.df_test = self.df_test.append(pd.Series([image_id,prediction_string,image_precision], index=self.df_test.columns), ignore_index=True)
                self.result_test.append({'image_id':image_id,'image':image,'gts_boxes':gts_boxes, 'pred_boxes':pred_boxes})

            #mean batch dataframe
            mean_batch_ious = np.mean(ious)
            self.df_performance_test_batch = self.df_performance_test_batch.append(pd.Series([mean_batch_ious], index=self.df_performance_test_batch.columns), ignore_index=True)

            to_return = {'test_iou_batch': mean_batch_ious}
                
        if self.step == "Deployment":
            # batch
            images, image_ids  = batch

            # Inference
            outputs = self.forward(images, image_ids, 'predictions')
            not_apply_list = ['N/A'] * len(outputs)

            #constructing dataframe
            for iter in zip(enumerate(outputs),not_apply_list):
                i = iter[0][0]
                output = iter[0][1]
                na = iter[1]
                pred_boxes = output['boxes'].astype(np.int32)
                image = images[i].permute(1,2,0).cpu().numpy()
                image_id = output['image_id']
                prediction_string = output['PredictionString']
                self.df_test = self.df_test.append(pd.Series([image_id,prediction_string,na], index=self.df_test.columns), ignore_index=True)
                self.result_test.append({'image_id':image_id,'image':image,'pred_boxes':pred_boxes})
            
        return to_return


    def test_epoch_end(self, outputs):

        if not outputs: return {}

        if self.step == "Experiment":
          avg_test_iou = np.mean([x['test_iou_batch'] for x in outputs])
          tensorboard_logs = {'avg_test_iou': avg_test_iou}
          retorno = {'avg_test_iou': avg_test_iou, 'log': tensorboard_logs}

        if self.step == "Deployment":
          retorno = None

        return retorno


    def configure_optimizers(self):

        params = [p for p in self.parameters() if p.requires_grad]
        return torch.optim.SGD( params,
                               lr=self.learning_rate,
                               momentum=self.momentum,
                               weight_decay=self.weight_decay)
    

    def my_collate(self,batch):
        return tuple(zip(*batch))


    def gpu_mem_restore(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                type, val, tb = sys.exc_info()
                traceback.clear_frames(tb)
                raise type(val).with_traceback(tb) from None
        return wrapper
    

    # Albumentations
    def get_train_transform(self):
        return A.Compose([
            A.Flip(0.5),
            ToTensorV2(p=1.0)
        ], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels']})


    def get_valid_transform(self):
        return A.Compose([
            ToTensorV2(p=1.0)
        ], bbox_params={'format': 'pascal_voc', 'label_fields': ['labels']})


    def get_test_transform(self):
        return A.Compose([
            # A.Resize(512, 512),
            ToTensorV2(p=1.0)
        ])
    

    def format_prediction_string(self, boxes, scores):
      pred_strings = []
      for j in zip(scores, boxes):
          pred_strings.append("{0:.4f} {1} {2} {3} {4}".format(j[0], j[1][0], j[1][1], j[1][2], j[1][3]))

      return " ".join(pred_strings)


    @gpu_mem_restore
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.train_batch_size, shuffle=False,num_workers=cpu_count(), collate_fn=self.my_collate)

    @gpu_mem_restore
    def val_dataloader(self):
        return DataLoader(self.valid_dataset, batch_size=self.valid_batch_size,shuffle=False, num_workers=cpu_count(),collate_fn=self.my_collate)    

    @gpu_mem_restore
    def test_dataloader(self):
        return DataLoader(self.valid_dataset, batch_size=self.test_batch_size,shuffle=False, num_workers=cpu_count(),collate_fn=self.my_collate)