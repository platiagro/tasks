import pandas as pd

def build_df_result(gen_questions_dict,column_context="context",column_question="questions"):
    context_list = [v["context"] for k,v in gen_questions_dict.items()]
    questions_list = [v["questions"] for k,v in gen_questions_dict.items()]
    df_result = pd.DataFrame({column_context: context_list,column_question: questions_list})
    return df_result