import pandas as pd
from typing import Dict

def build_df_result(df_input:pd.DataFrame,gen_questions_dict:Dict,column_doc_id:str="doc_id",column_question:str="questions"):
    questions_list = [v["questions"] for k,v in gen_questions_dict.items()]
    doc_id_list = list(map(int, gen_questions_dict.keys()))
    df_question_gen = pd.DataFrame({column_doc_id: doc_id_list,column_question: questions_list})
    df_result = pd.merge(df_input, df_question_gen,on = [column_doc_id])
    return df_result