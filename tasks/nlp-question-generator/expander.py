import os
import pandas as pd

from io_utils import IO_Utils
from typing import List

class DocExpander:
    def __init__(self):
        '''
        Expand documents with the questions gerated from them. 
        Documents and questions and questins between them are separated by the special token [SEP]
        '''
        pass
    
    def expand_nosql(self,context_questions_map,context_key='context',questions_key = 'questions',apply_filter=False,apply_low_case=False):
        """
        Retorna os contextos expandidos no formato noSQL com o id do contexto, tendo como valores
        os contextos, contextos expandidos e perguntas.
        """

        context_questions_map_internal = context_questions_map.copy()

        if apply_low_case:
            context_questions_map = self.lower_case_dict(context_questions_map)

        if apply_filter:
            context_questions_map_internal = self.filter_post_content(content=context_questions_map_internal,
                                                            section_names_to_keep=['Capítulo 6', 'Capitulo 6'],
                                                            min_context_length_in_tokens=20)
        
        for k,v in context_questions_map_internal.items():
            context = v[context_key]
            questions = v[questions_key]
            expanded_context = context + ' ' + ' '.join(questions)
            expanded_context = expanded_context.strip()
            context_questions_map_internal[k]['expanded_context'] = expanded_context
        
        return context_questions_map_internal

    # TODO: Desenvolver técnica SQL
    def expand_sql(self,df,context_column_name='context',questions_column_name = 'questions'):
        """
        Retorna os contextos expandidos no formato de uma nova coluna no dataframe
        """
        
        df_copy = df.copy()
        expanded_context_list = []
        for index, row in df_copy.iterrows():
            questions = row[questions_column_name]
            context = row[context_column_name]
            expanded_context = context + ' ' + ' '.join(questions)
            expanded_context = expanded_context.strip()
            expanded_context_list.append(expanded_context)
        
        df_copy.insert(df.shape[1], "expanded_context", expanded_context_list)
        
        return df_copy