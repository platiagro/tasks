import joblib
import nltk
import pandas as pd
import numpy as np
import base64
import cv2
import logging
import io
from pdf_extractor import PDFExtractor, read_memory, read_file

class Model:
    def __init__(self):
        self.loaded = False;

    def load(self):
        artifacts = joblib.load("/tmp/data/pdf_extractor.joblib")
        self.extractor_parameters = artifacts["extractor_parameters"]
        
        if self.extractor_parameters["initial_page"] != None: 
            self.extractor_parameters["initial_page"] -= 1;

        if self.extractor_parameters["final_page"] != None: 
            self.extractor_parameters["final_page"] -= 1;
        
        self.loaded = True
        print("Loaded model")

    def predict(self, X, feature_names, meta=None):
        if not self.loaded:
            self.load()
        
        if isinstance(X, bytes):
            result = read_memory(X,
                                extract = self.extractor_parameters["extract"],
                                text_filter_begin = self.extractor_parameters["text_filter_begin"],
                                text_filter_end = self.extractor_parameters["text_filter_end"],
                                initial_page = self.extractor_parameters["initial_page"],
                                final_page = self.extractor_parameters["initial_page"])
        else:
            return ""
                                        
        if self.extractor_parameters["extract"] == "text":
            #return np.array([1,2]);
            return result
    
        elif self.extractor_parameters["extract"] == "figures":
            result_bytes = []
            if len(result) > 0:
                for img in result:
                    buff = io.BytesIO()
                    img.save(buff, format="JPEG")
                    result_bytes.append(buff.getvalue().decode("latin1"))

                return result_bytes;
            else:
                return result
    
        elif self.extractor_parameters["extract"] == "prints":
            result_bytes = []
            if len(result) > 0:
                for img in result:
                    buff = io.BytesIO()
                    img.save(buff, format="JPEG")
                    result_bytes.append(buff.getvalue().decode("latin1"))

                return result_bytes;
            else:
                return result
