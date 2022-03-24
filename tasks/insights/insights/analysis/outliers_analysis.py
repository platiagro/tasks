"""
A ideia dessas analises é que ela recebe uma entrada padrão, podendo ser utilizada em qualquer saída de detecção de outliers. 
A análise será alto nível, mas com opção de plotar gráficos. 
Padronizando as análises podemos ter uma lista de análises a se fazer, onde a entrada é o dataframe e a saída é a análise em texto e os plots, 
assim podemos linkar as análises igual uma rede neural sequencial, e os plots/textos ficam fáceis de serem encaminhados para a tela do usuário. 
""" 

import numpy as np
import pandas as pd

from insights.outliers.remove import DetOutliers
from insights.outliers.plot import plot
from insights.utils.filtering import column_filter
from insights.analysis.cluster_analysis import cluster_pivot


from pylatex import Ref, NoEscape, Command

def generate_ref_literal(label, i):
    label = r'{'+r'{label}'.format(label=label) + r'{i}'.format(i=i) + r'}'
    return label
    
def outlier_analysis(df):
    outlier_determiner = DetOutliers(df)
    
    analisys = {}
    
    schema = {'section_title': 'Análise de Outliers', 'information': []}
    
            
    schema['information'].append(
        {
            'type': 'text',
            'info': f'Os outliers são dados que se diferenciam drasticamente de todos os outros. Em outras palavras, um outlier é um valor que foge da normalidade e que pode (e provavelmente irá) causar anomalias nos resultados obtidos por meio de algoritmos e sistemas de análise. Entender os outliers é fundamental em uma análise de dados por pelo menos dois aspectos: os outliers podem viesar negativamente todo o resultado de uma análise; o comportamento dos outliers pode ser justamente o que está sendo procurado.'
        }
    )
        
    for i, function_name in enumerate(outlier_determiner.functions):
        subschema = {'section_title': function_name, 'information': []}
        

        _, y_pred, filtered_df, outliers_df = outlier_determiner.functions[function_name]()
        
        _, cat_cols = column_filter(outliers_df, target_data='categorical')
        _, num_cols = column_filter(outliers_df, target_data='numerical')
        
        
        if len(num_cols) > 0:
            numerical_describer = outliers_df[num_cols].describe()
        else:
            numerical_describer = pd.DataFrame([0])
        if len(cat_cols) > 0:
            categorical_describer = outliers_df[cat_cols].describe()
        else:
            categorical_describer = pd.DataFrame([0])
            
        figure = plot(df, y_pred, dimensions=2, title=None)
        
        
        outliers_sum = np.sum(y_pred==-1)
        outliers_prop = outliers_sum/len(df)

        subschema['information'].append(
            {
                'type': 'text', 
                'info': 'Isolation Forests é um modelo de detecção de anomalias que faz uso de um conjunto de dados onde o alvo, neste caso a anomalia da fraude, do modelo contém poucas amostras entre tantos dados normais. A ideia do modelo é construir Árvores para isolar essas anomalias. Em outras palavras, a floresta de Isolamento é um conjunto de Árvores de Isolamento. Método parecido com a da nossa querida Random Forest.'
            }
        )
        
        if outliers_sum > 0:
            text = f'Utilizando o método {function_name} foram detectados {outliers_sum} outliers neste dataset, correspondendo a uma proporção de {outliers_prop:.2%} do conjunto de amostras.'
                            
            subschema['information'].append(
                {
                    'type': 'text',
                    'info': text
                }
            )

            label1 = generate_ref_literal(r'tab:numerical', i)
            label2 = generate_ref_literal(r'tab:categorical', i)
            label3 = generate_ref_literal(r'fig:outliers', i)
            
            text = NoEscape(fr'A orbservação do outliers pode ser feita nas tabelas abaixo, onde serão mostradas as tabelas de descrição dos outliers, tando de todas as features categóricas quanto de todas as features numéricas. Também é mostrado, na figura abaixo, a distribuição dos outliers em relação ao restante da população do dataset.')

            subschema['information'].append(
                {
                    'type': 'text',
                    'info': text
                }
            )
        
            subschema['information'].append(
                {
                    'type': 'table', 
                    'caption': 'Descrição Features Numéricas dos Outliers: ' + function_name,
                    'table': numerical_describer,
                    'label': r'tab:numerical{i}'.format(i=i),
                    'float_fmt': "%.2f"
                }
            ) 
            
            subschema['information'].append(
                {
                    'type': 'table', 
                    'caption': 'Descrição Features Categóricas dos Outliers: ' + function_name,
                    'label': r'tab:categorical{i}'.format(i=i),
                    'table': categorical_describer
                }
            ) 
            
            subschema['information'].append(
                {
                    'type': 'figure', 
                    'package': 'plotly',
                    'caption': 'Visualização dos outliers: ' + function_name,
                    'label': r'fig:outliers{i}'.format(i=i),
                    'figure': figure
                }
            )
                    
        schema['information'].append(
            {
                'type': 'subsection', 
                'schema': subschema
            }
        ) 
        
    outliers_df['cluster_group'] = 'outlier'
    return schema, filtered_df, outliers_df

