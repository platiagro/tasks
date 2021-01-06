import cv2 
import numpy as np
import pandas as pd
from torchvision import datasets, transforms
import torch
import random
from facenet_pytorch import MTCNN
from PIL import Image
from multiprocessing import cpu_count
import zipfile

class MTCNN_Model:
    def __init__(self, general_parameters,model_parameters,inference_parameters):
        
        #---------dataset_infos
        self.X = None
        self.input_images = None
        self.subfolders = None

        #--------general_parameters
        self.root_folder_name = general_parameters['root_folder_name']
        

        #---------model_parameters
        self.image_size = model_parameters['image_size']
        self.margin = model_parameters['margin']
        self.min_face_size = model_parameters['min_face_size']
        self.thresholds = model_parameters['thresholds']
        self.factor = model_parameters['factor']
        self.keep_all = model_parameters['keep_all']
        self.device = 'cuda:0' if (model_parameters['device']=="cuda" and torch.cuda.is_available()) else 'cpu'
        self.seed = model_parameters['seed']
        self.post_process = False
  
        #---------Inference_parameters
        self.inference_batch_size = inference_parameters['inference_batch_size']
        self.input_square_transformation_size = inference_parameters['input_square_transformation_size']

        #------- Other
        self.num_workers = cpu_count()

        #------- MTCNN
        self.mtcnn = MTCNN(image_size=self.image_size, 
                           margin=self.margin, 
                           min_face_size=self.min_face_size,
                           thresholds=self.thresholds, 
                           factor=self.factor, 
                           post_process=self.post_process,
                           keep_all=self.keep_all,
                           device=self.device)

        #------- Reproducibility
        random.seed(self.seed)
        np.random.seed(self.seed)
        torch.random.manual_seed(self.seed)
        torch.cuda.manual_seed(self.seed)
        
        #------- Results
        self.df_result  = None


    def predict(self,img_reference,step):
        if step == "Experiment":
            image_array = img_reference
        if step == "Deployment":
            img = img_reference
            image_array = Image.fromarray(img)

        boxes, probs = self.mtcnn.detect(image_array, landmarks=False)
        
        return (boxes, probs)

    def _construct_result_dataframe(self,step):
        
        self.df_result = pd.DataFrame(columns=["Input_image","Bboxes(x1,y1,x2,y2)","Probabilities"])

        boxes_list = []
        probs_list = []

        for i in range(0,len(self.X),self.inference_batch_size):
          img_reference = []
          batch_images = self.X[i:i+self.inference_batch_size]

          #Process each batch image
          for row in batch_images:
            v_cap = cv2.VideoCapture(row[0])
            success, frame = v_cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (self.input_square_transformation_size,self.input_square_transformation_size))
            img_reference.append(Image.fromarray(img))

          #Infer the batch
          batch_result = self.predict(img_reference,step)

          #Expand dims when batch ==1
          if batch_result[0].ndim==2 and batch_result[1].ndim==1:
            faces_boxes = np.expand_dims(batch_result[0],axis=0)
            probabilities = np.expand_dims(batch_result[1],axis=0)
            batch_result = [faces_boxes,probabilities]      

          #Organize batch 
          boxes_batch = []
          probs_batch = []
          images_batch = []
          for i in range(batch_result[0].shape[0]):
            image_path = batch_images[i][0]
            result_bboxes = batch_result[0][i,:,:]
            result_probs = batch_result[1][i,:]
            if self.keep_all:
              for b,p in zip(result_bboxes,result_probs):
                boxes_batch.append(b)
                probs_batch.append(p)
                images_batch.append(image_path)
                
            else:
              max_prob_position = np.argmax(result_probs)
              boxes_batch.append(result_bboxes[max_prob_position])
              probs_batch.append(result_probs[max_prob_position])
              images_batch.append(image_path)

          #Constructing Dataframe
          for boxes_image,probs_image,image_path in zip(boxes_batch,probs_batch,images_batch):
            self.df_result = self.df_result.append(
                        pd.Series(
                            [
                              image_path,
                              boxes_image,
                              probs_image
                            ],
                            index=self.df_result.columns,
                        ),
                        ignore_index=True,
                    )
          

    def get_result_dataframe(self,X,step = 'Experiment'):

        self.X = X
        self.image_paths = X[:,0]
        self._construct_result_dataframe(step)
        return self.df_result