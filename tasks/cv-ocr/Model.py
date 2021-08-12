import joblib
import nltk
import pandas as pd
import numpy as np
import base64
import cv2
import logging
from ocr import Class_Pytesseract_OCR


class Model:
    
    def __init__(self):
        self.loaded = False
    
    def load(self):
        artifacts = joblib.load("/tmp/data/ocr.joblib")
        self.hyperparams = artifacts["hyperparams"]
        self.model_parameters = artifacts["model_parameters"]
        self.return_formats = artifacts["return_formats"]
        
        self.model = Class_Pytesseract_OCR(self.hyperparams, self.model_parameters, self.return_formats)
        # Health check validation
        random_img = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
        _, _ = self.model.predict(random_img, "Deployment")
        
        
        
        self.loaded = True 

        
    def class_names(self):
        if self.return_formats['bbox_return'] == "image":
            return ['image', 'text']
        return ['x_min', 'y_min', 'x_max', 'y_max', 'text']
    
    def format_result(self, boxes, text):
        words = text.split(' ')
        try:
            words.remove('')
        except: None
        res = []
        for i, box in enumerate(boxes):
            box = list(map(float, box))
            res.append(
                np.array(box + [words[i]])
            )
        """
        for i in range(len(boxes)):
            
            bbox = list(map(float, boxes[i]))
            bbox.extend([text[i]])
            bbox = np.array(bbox)
            res.append(bbox)
        """

        
        return res
    
    def predict(self, X, feature_names, meta=None):
        # First time load model
        if not self.loaded:
            self.load()
            
        # Check if data is a bytes
        if isinstance(X, bytes):
            im_bytes = X # Get image bytes
        
        # If not, should be a list or ndarray
        else:
            # Garantee is a ndarray
            X = np.array(X)
            
            # Seek for extra dimension
            if len(X.shape) == 2:
                im_bytes = X[0,0] # Get image bytes
            
            else:
                im_bytes = X[0] # Get image bytes
        
        # Preprocess img bytes to img_arr
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        frame = np.array(img).astype(np.uint8)
        
        bboxes_or_image, text = self.model.predict(frame, "Deployment", self.return_formats)
        
        if self.return_formats['bbox_return'] == "np_array":
            result = self.format_result(bboxes_or_image, text)
        else:
            im_arr = np.frombuffer(bboxes_or_image, dtype=np.uint8)
            img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            frame_with_text = np.array(img).astype(np.uint8)
            result = frame_with_text
        
        ### DEBUG ###
        logging.error('--- DBG ---')
        logging.error('result: %s', result)
        logging.error('type: %s', type(result))
        logging.error('--- DBG ---')
        #############
        
        return np.array(result)
