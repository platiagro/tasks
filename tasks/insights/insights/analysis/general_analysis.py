import pandas as pd 
from insights.utils.filtering import column_filter
from insights.preprocessing.preprocess import df_to_float, num_2_cat, df_nan_process

def general_analysis(df, target=None):
    schema = {'section_title': 'Análise Geral', 'information': []}

    schema['information'].append(
        {
            'type': 'text',
            'info': f'Uma análise geral pode gerar insighs interessantes, no ponto de vista de dados gerais do banco fornecido. Nas tabelas a seguir serão apresentados dados como média, frequencia, maior valor, etc.'
        }
    )
    
    
    
    schema['information'].append(
        {
            'type': 'table',
            'table': df.describe(),
            'caption': 'Tabela de descrição geral dos dados fornecidos.'
        }
    )
    
    if target is not None:
        _, categorical_columns = column_filter(df, target_data='categorical')
        _, numerical_columns = column_filter(df, target_data='numerical')
        
        if target in numerical_columns:
            df[target + ' categorizado'] = num_2_cat(df, target)
            target += ' categorizado'
            
        schema['information'].append(
        {
            'type': 'text',
            'info': f'A análise por agrupamento pode trazer insights interessantes por considerar uma variável alvo como um ponto em comum dos dados. Assim possibilitando a comparação de quais features mais caracterizam cada um dos grupos alvo.'
        }
        )
        columns = list(set(numerical_columns) | set([target]))
        grouped_mean = df[columns].groupby([target]).mean()
        grouped_mean = grouped_mean.sort_values(by=target)
        
        schema['information'].append(
        {
            'type': 'table',
            'table': grouped_mean,
            'caption': 'Tabela de agrupamento geral dos dados numéricos, por média.'
        }
        )
        
        columns = list(set(categorical_columns) | set([target]))
        grouped_mode = df[columns].groupby([target]).count()/len(df)
        grouped_mode = grouped_mode.sort_values(by=target)
        
        schema['information'].append(
        {
            'type': 'table',
            'table': grouped_mode,
            'caption': 'Tabela de agrupamento geral dos dados categóricos, por moda.'
        }
        )
    
    
    return schema