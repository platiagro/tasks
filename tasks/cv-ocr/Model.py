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
        artifacts = joblib.load("/tmp/data/ocr.joblib")
        self.hyperparams = artifacts["hyperparams"]
        self.model_parameters = artifacts["model_parameters"]
        self.return_formats = artifacts["return_formats"]
        
        self.model = Class_Pytesseract_OCR(self.hyperparams, self.model_parameters, self.return_formats)

        
    def class_names(self):
        
        return ['x_min', 'y_min', 'x_max', 'y_max', 'text']
    
    def format_result(self, boxes, text):
        
        res = []
        
        for i in range(len(boxes)):
            
            bbox = list(map(float, boxes[i]))
            bbox.extend([text[i]])
            bbox = np.array(bbox)
            res.append(bbox)
        
        return res
    
    def predict(self, X, feature_names, meta=None):
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
        
        if self.return_formats == "np_array":
            result = self.format_result(bboxes_or_image, text)
        else:
            result = [text, np.array(bboxes_or_image)]
            
        ### DEBUG ###
        logging.error('--- DBG ---')
        logging.error('result: %s', result)
        logging.error('type: %s', type(result))
        logging.error('--- DBG ---')
        #############
        
        return np.array(result)
