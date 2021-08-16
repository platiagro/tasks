import joblib
import pandas as pd
import numpy as np
import json
from aux_functions import build_result_dataframe


class Model:
    
    def __init__(self):
        self.loaded = False
    
    def load(self):
        
        artifacts = joblib.load("/tmp/data/sparse_retriever.joblib")
        self.model = artifacts["model"]
        self.top = artifacts["top"]
        self.question = artifacts["question"]
        self.columns = artifacts["columns"]
        self.column_context = artifacts["column_context"]
        self.column_doc_id = artifacts["column_doc_id"]
        self.column_score = artifacts["column_score"]
        self.loaded = True

    def predict(self, X, feature_names, meta=None):
        
        if not self.loaded:
            self.load()
            
        if not feature_names:
            feature_names = self.columns
            
        
        df = pd.DataFrame(X,columns = feature_names)
        report_contexts = df[self.column_context].to_numpy()
        doc_ids = df[self.column_doc_id].to_numpy()
        self.model.fit(contexts=report_contexts, doc_ids=doc_ids)
        sim_contexts_ids, scores = self.model(questions=self.question, top=self.top)

            
        df_result = build_result_dataframe(df_input=df,
                            sim_contexts_ids=sim_contexts_ids[0],
                            scores=scores[0],
                            column_doc_id = self.column_doc_id,
                            column_score = self.column_score)
        
        return df_result.to_numpy() 
