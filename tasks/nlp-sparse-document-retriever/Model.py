import joblib
import pandas as pd
import numpy as np
import json


class Model:
    
    def __init__(self):
        
        artifacts = joblib.load("/tmp/data/sparse_retriever.joblib")
        self.model = artifacts["model"]
        self.report_contexts = artifacts["report_contexts"]
    
    def build_result_dataframe(self, sim_contexts_ids,scores):
        sim_contexts = [self.report_contexts[i] for i in sim_contexts_ids[0]]
        df = pd.DataFrame({'doc_id':sim_contexts_ids[0],'score':scores[0],'sim_contexts':sim_contexts})
        df = df.sort_values(by=['score'], ascending=False).reset_index(drop=True)
        return df

    def predict(self, X, feature_names, meta=None):

        question = X.copy()[0]
        sim_contexts_ids,scores = self.model(question)
        df = self.build_result_dataframe(sim_contexts_ids,scores)
        df['question'] = [question]*len(scores[0])
        #teste = json.dumps({'question':[question]*len(scores[0]),'df':df.to_numpy()})
        #*** TypeError: Object of type ndarray is not JSON serializable
        return df.to_numpy() 
