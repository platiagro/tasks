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
        
    def predict(self, 
                img_arr: np.ndarray):
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
        
        # Migth popup a warning when not fiding any bbox
        boxes, probs = self.mtcnn.detect(img_arr, landmarks=False)
        
        return (boxes, probs)
    
    def _post_process_batch(self, batch_results, batch_img_paths, batch_original_img_shapes):
        '''
        Parameters
        ----------
        batch_results : np.ndarray, list
            A array containing the data of each batch prediction
            
        batch_img_paths : np.ndarray, list
            Containing each image path for each instance of the
            batch_result
            
        batch_original_img_shapes : np.ndarray, list
            Containing each image original tuple shape (e.g. [(256, 256, *),...])

        Returns
        -------
        pd.DataFrame
            Returns a pd.DataFrame containing the batch results,
            for each image, with image_path, bbox and probability
        '''
        
        df = pd.DataFrame(columns=["Input_image","Bboxes(x1,y1,x2,y2)","Probabilities"])
        
        # Resulting arrays from batches results
        paths, bboxes, probs = [], [], []
        
        zipped_loop = zip(batch_results[0], batch_results[1], batch_img_paths, batch_original_img_shapes)
        
        for bboxes_data, probs_data, image_path, original_img_shape in zipped_loop:
            
            # Not found bbox
            if bboxes_data is None:
                paths.append(image_path)
                bboxes.append(None)
                probs.append(None)
                continue
            
            for bbox_id in range(bboxes_data.shape[0]):
                paths.append(image_path)
                
                # Restore the bbox to match original image shape
                restored_bbox = self._bbox_to_original_shape(
                    bboxes_data[bbox_id],
                    original_img_shape
                    )
                
                bboxes.append(restored_bbox)
                probs.append(probs_data[bbox_id])
            
        df = pd.DataFrame()
        df["Input_image"]         = paths
        df["Bboxes(x1,y1,x2,y2)"] = bboxes
        df["Probabilities"]       = probs
        
        # Ordering column names
        df = df[["Input_image","Bboxes(x1,y1,x2,y2)","Probabilities"]]
        
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
        
    
    def _construct_result_dataframe(self):
        '''
        Build a dataframe that contains for each input image
        the respective predicted bbox and probabilities according
        to mtcnn pretreined model
        '''
        
        # Define the df_result format
        self.df_result = pd.DataFrame(columns=["Input_image","Bboxes(x1,y1,x2,y2)","Probabilities"])
        
        # Perform batch prediction
        max_size = len(self.X)
        step     = min(max_size, self.inference_batch_size)
        for i in range(0, max_size, step):
            
            batch_imgs = []
            batch_original_img_shapes = []
            batch_img_paths = self.X[i:i+step]

            # Process each batch image
            for img_path in batch_img_paths:
                
                # Read image
                v_cap = cv2.VideoCapture(img_path)
                success, frame = v_cap.read()
                
                # Preprocess image
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                batch_original_img_shapes.append(img.shape) # Save original shape for refactor bbox
                img = cv2.resize(img, (self.input_square_transformation_size,self.input_square_transformation_size))
                batch_imgs.append(img)

            # Infer the batch
            batch_results = self.predict(np.array(batch_imgs))
            
            # Post process results from batch inference
            batch_df = self._post_process_batch(batch_results, batch_img_paths, batch_original_img_shapes)
            
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
            the inferences. The dataframe has the columns "Input_image", 
            "Bboxes(x1,y1,x2,y2)" and "Probabilities".
        '''
        
        self.X = X
        self._construct_result_dataframe()
        
        return self.df_result