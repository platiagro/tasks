import pandas as pd
from typing import Union
def build_result_dataframe(df_input:pd.DataFrame,
                           df_result:pd.DataFrame,
                           ntops_overall:int,
                           reader_score_weight:float,
                           retriever_reader_pipeline:bool = True,
                           remove_no_answer_found:bool = True,
                           column_doc_id:str="doc_id",
                           column_retriever_score:Union[str,None]="retriever_score",
                           column_reader_score:str="reader_score"):
    
    
    df_result_copy = df_result.copy()
    del df_result_copy['context']
    df_result_copy = pd.merge(df,df_result_copy,on = [column_doc_id],how='inner')
    df_result_copy = df_result_copy.rename(columns={"answer_prob": column_reader_score})
    
    if remove_no_answer_found:
        df_result_copy.loc[df_result_copy['answer'] == '[Not Found]', column_reader_score] = 0
        
    if retriever_reader_pipeline:
        retriever_score_weight = 1.0 - reader_score_weight
        retriever_score_weighted = retriever_score_weight*df_result_copy[column_retriever_score]
        reader_score_weighted = reader_score_weight*df_result_copy[column_reader_score]
        overall_score = [ret + rea for ret,rea in zip(retriever_score_weighted,reader_score_weighted)]
        df_result_copy.insert(df_result_copy.shape[1],'overall_score',overall_score)
    
    else:
        df_result_copy = df_result_copy.rename(columns={column_reader_score: 'overall_score'})
           
        
    df_result_copy = df_result_copy.sort_values(by='overall_score', ascending=False).reset_index(drop=True)
    df_result_copy = df_result_copy[:ntops_overall]
        
    return df_result_copy