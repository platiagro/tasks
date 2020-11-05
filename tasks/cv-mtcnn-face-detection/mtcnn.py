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
        boxes = []
        probs = []

        for i in range(0,len(self.X),self.inference_batch_size):
          img_reference = []
          batch = self.X[i:i+self.inference_batch_size]
          for row in batch:
            v_cap = cv2.VideoCapture(row[0])
            success, frame = v_cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (self.input_square_transformation_size,self.input_square_transformation_size))
            img_reference.append(Image.fromarray(img))

          batch_result = self.predict(img_reference,step)

          if self.keep_all:
            for b,p in zip(batch_result[0],batch_result[1]):
              boxes.append(b)
              probs.append(p)
              
          else:
            for b,p in zip(batch_result[0],batch_result[1]):
              max_prob_position = np.argmax(p)
              boxes.append(b[max_prob_position])
              probs.append(np.max(p))

        self.df_result = pd.DataFrame({'Input_image':self.input_images,'Subfolder': self.subfolders ,'Bboxes(x1,y1,x2,y2)':boxes,'Proababilities':probs})


    def get_result_dataframe(self,X,step = 'Experiment'):

        self.X = X
        self.input_images = X[:,0]
        self.subfolders = X[:,1]
        self._construct_result_dataframe(step)
        return self.df_result