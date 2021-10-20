import joblib
import nltk
import pandas as pd
import numpy as np
import base64
import cv2
import logging
from pdf_extractor import PDFExtractor, read_memory

class Model:
    def __init__(self):
        self.loaded = False;

    def load(self):
        artifacts = joblib.load("/tmp/data/pdf_extractor.joblib")
        self.extractor_parameters = artifacts["extractor_parameters"]
        
        self.loaded = True
        print("Loaded model")

    def predict(self, X, feature_names, meta=None):
        if not self.loaded:
            self.load()
        
        # check if data is bytes
        if isinstance(X, bytes):
            result = read_memory(X,
                                extract = self.extractor_parameters["extract"],
                                text_filter_begin = self.extractor_parameters["text_filter_begin"],
                                text_filter_end = self.extractor_parameters["text_filter_end"],
                                initial_page = self.extractor_parameters["initial_page"],
                                final_page = self.extractor_parameters["initial_page"])
                                        
        if self.extractor_parameters["extract"] == "text":
            return result
    
        elif self.extractor_parameters["extract"] == "figures":
            for img in result:
                img = np.array(img)
            return np.stack(result, axis=0)
    
        elif self.extractor_parameters["extract"] == "prints":
            for img in result:
                img = np.array(img)
            return np.stack(result, axis=0)
