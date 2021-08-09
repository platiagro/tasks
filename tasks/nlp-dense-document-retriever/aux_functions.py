import pandas as pd
import numpy as np
from typing import Dict
from sklearn.preprocessing import MinMaxScaler

def build_result_dataframe(df_input:pd.DataFrame,sim_contexts_ids:np.ndarray,scores:np.ndarray,column_doc_id:str="doc_id",column_score:str="retriever_score"):
    
    scaler = MinMaxScaler()
    normalized_relevances = scaler.fit_transform(scores).ravel()
    df = pd.DataFrame({column_doc_id:sim_contexts_ids,column_score:normalized_relevances})
    df_result = pd.merge(df_input, df,on = [column_doc_id],how='inner')
    df_result = df_result.sort_values(by=[column_score], ascending=False).reset_index(drop=True)
    

    return df_result