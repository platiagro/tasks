"""
A ideia dessas analises é que ela recebe uma entrada padrão, podendo ser utilizada em qualquer saída de detecção de outliers. 
A análise será alto nível, mas com opção de plotar gráficos. 
Padronizando as análises podemos ter uma lista de análises a se fazer, onde a entrada é o dataframe e a saída é a análise em texto e os plots, 
assim podemos linkar as análises igual uma rede neural sequencial, e os plots/textos ficam fáceis de serem encaminhados para a tela do usuário. 
""" 

import numpy as np

from insights.outliers.remove import DetOutliers
from insights.outliers.plot import plot
from insights.utils.filtering import column_filter

    
def outlier_analysis(df):
    outlier_determiner = DetOutliers(df)
    
    figures = []
    numerical_describer = []
    categorical_describer = []
    title = []
    
    text = ''
    
    for i, function_name in enumerate(outlier_determiner.functions):

        _, y_pred, filtered_df, outliers_df = outlier_determiner.functions[function_name]()
        
        _, cat_cols = column_filter(outliers_df, target_data='categorical')
        _, num_cols = column_filter(outliers_df, target_data='numerical')
        
       
        
        figure = plot(df, y_pred, dimensions=3, title=function_name)
        figures.append(figure)
        
        outliers_sum = np.sum(y_pred==-1)
        outliers_prop = outliers_sum/len(df)
        
        if outliers_sum > 0:
            text += f'Utilizando o método {function_name} foram detectados {outliers_sum} outliers neste dataset, correspondendo a uma proporção de {outliers_prop:.2%} do conjunto de amostras.\n'
            title.append(function_name)
            numerical_describer.append(outliers_df[num_cols].describe())
            categorical_describer.append(outliers_df[cat_cols].describe())
        elif outliers_sum == 0:
            text += f'Não foram detectados outliers utilizando o método {function_name}.\n'
                            
    return text, figures, filtered_df, title, numerical_describer, categorical_describer, outliers_df

