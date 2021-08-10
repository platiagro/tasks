import logging
import cv2 
import numpy as np
import pandas as pd
from torchvision import datasets, transforms
import torch
import random
from facenet_pytorch import MTCNN
from PIL import Image
from multiprocessing import cpu_count



class MTCNN_Model:


    def __init__(self, model_parameters, inference_parameters):
        
        #---------dataset_infos
        self.X = None
        self.input_images = None
        self.subfolders = None

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
        
    def predict(self, img_arr: np.ndarray):
        '''
        Parameters
        ----------
        img_arr : np.ndarray, list
            A array containing the data of a 3D image or a list of
            3D image arrays (as a batch)
        
        Returns
        -------
        Tuple
            First element represents a list of lists of bbox found in each 
            batch image. Shape: (N, B, 4), where N is the batch size and B
            is the associated bbox found in the image.
            
            Second element represents a list of a list of probabilities associated 
            with each batch image and each bbox. Shape: (N, B)
            
            If no bbox was found, first element is represented by None, and the second
            [None]
        '''

        # Convert to nd.array
        if isinstance(img_arr, list):
            img_arr = np.array(img_arr)

        # Adding batch dimension
        if len(img_arr.shape) == 3:
            img_arr = np.expand_dims(img_arr, 0)

        # Resize image to network input size
        original_image_shapes = []
        reshaped_images = []
        for img in img_arr:
            original_image_shapes.append(img.shape)
            reshaped_images.append(cv2.resize(img, (self.input_square_transformation_size, self.input_square_transformation_size)))
        
        # Convert to np.ndarray
        reshaped_images = np.array(reshaped_images)
        
        # Migth popup a warning when not fiding any bbox
        batch_bboxes, batch_probs = self.mtcnn.detect(reshaped_images, landmarks=False)

        for i, bboxes in enumerate(batch_bboxes):
            if bboxes is None: continue
            
            # Reshape bbox to match original image shape
            original_shape = original_image_shapes[i]
            batch_bboxes[i] = [self._bbox_to_original_shape(bbox, original_shape) for bbox in bboxes]

        return (batch_bboxes, batch_probs)
    
    def _post_process_results(self, batch_results, index_range):
        '''
        Parameters
        ----------
        batch_results : np.ndarray, list
            A array containing the data of each batch prediction
            
        index_range : np.ndarray, list
            Containing each image index in the batch
            
        Returns
        -------
        pd.DataFrame
            Returns a pd.DataFrame containing the batch results,
            for each image, with image_path, bbox and probability
        '''
        
        # Resulting arrays from batches results
        paths, bboxes, probs = [], [], []

        # Get batch image paths
        batch_img_paths = self.X[index_range]
        
        # Zip data for loop
        zipped_loop = zip(batch_results[0], batch_results[1], batch_img_paths)
        
        for bboxes_data, probs_data, image_path in zipped_loop:

            # Not found bbox
            if bboxes_data is None:
                paths.append(image_path)
                bboxes.append(None)
                probs.append(None)
                continue

            # Assure to be a numpy array
            bboxes_data = np.array(bboxes_data)
            
            for bbox_id in range(bboxes_data.shape[0]):
                paths.append(image_path)
                bboxes.append(bboxes_data[bbox_id])
                probs.append(probs_data[bbox_id])
            
        df = pd.DataFrame()
        df["image"] = paths
        df["coords(x_min,y_min,x_max,y_max)"] = bboxes
        df["probability"] = probs
        
        # Ordering column names
        df = df[["image","coords(x_min,y_min,x_max,y_max)","probability"]]
        
        return df
    
    def _bbox_to_original_shape(self, bbox, original_shape):
        '''
        Parameters
        ----------
        bbox : np.ndarray, list
            A array containing the bbox data (e.g. [x1, y1, x2, y2])
            
        original_shape : tuple
            Containing a original image tuple shape (e.g. (256, 256, *))

        Returns
        -------
        np.ndarray
            A array containing the bbox data (e.g. [x1', y1', x2', y2'])
        '''
        
        x1 = bbox[0] * original_shape[1]/self.input_square_transformation_size
        x2 = bbox[2] * original_shape[1]/self.input_square_transformation_size
        y1 = bbox[1] * original_shape[0]/self.input_square_transformation_size
        y2 = bbox[3] * original_shape[0]/self.input_square_transformation_size

        return np.array([x1, y1, x2, y2])

    def _build_batch(self, index_range):
        '''
        Build a batch of images to be used in prediction
        '''

        # Create a batch of images
        batch = []
        image_paths = self.X[index_range]
        for image_path in image_paths:
            # Read image
            v_cap = cv2.VideoCapture(image_path)
            success, frame = v_cap.read()

            # If image is not read correctly, skip it
            if not success: continue
            
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            batch.append(img)

        return np.array(batch)
    
    def _construct_result_dataframe(self):
        '''
        Build a dataframe that contains for each input image
        the respective predicted bbox and probabilities according
        to mtcnn pretreined model
        '''
        
        # Define the df_result format
        self.df_result = pd.DataFrame(columns=["image","coords(x_min,y_min,x_max,y_max)","probability"])
        
        # Perform batch prediction
        max_size = len(self.X)
        step     = min(max_size, self.inference_batch_size)
        for i in range(0, max_size, step):

            # Batch index range
            index_range = range(i, min(i+step, max_size))
            
            # Build a batch of images
            batch = self._build_batch(index_range)

            # Infer the batch
            batch_results = self.predict(batch)
            
            # Post process results from batch inference
            batch_df = self._post_process_results(batch_results, index_range)
            
            # Add results to final df
            self.df_result = pd.concat((self.df_result, batch_df))
        
        # Reseting indices
        self.df_result = self.df_result.reset_index(drop=True)
        
    def get_result_dataframe(self, X):
        '''
        Parameters
        ----------
        X : np.ndarray, list
            A array or list containing each image path
            
        Returns
        -------
        pd.DataFrame
            Returns a pd.DataFrame containing all the results of
            the inferences. The dataframe has the columns "image", 
            "coords(x_min,y_min,x_max,y_max)" and "probability".
        '''
        
        self.X = X
        self._construct_result_dataframe()
        
        return self.df_result