"""
A ideia dessas analises é que ela recebe uma entrada padrão, podendo ser utilizada em qualquer saída de detecção de clusters. 
A análise será alto nível, mas com opção de plotar gráficos. 
Padronizando as análises podemos ter uma lista de análises a se fazer, onde a entrada é o dataframe e a saída é a análise em texto e os plots, 
assim podemos linkar as análises igual uma rede neural sequencial, e os plots/textos ficam fáceis de serem encaminhados para a tela do usuário. 
""" 

import numpy as np
import pandas as pd
import plotly.express as px

from tabulate import tabulate

from insights.clustering.permutation import ClusterPermutator
from insights.clustering.plot import Plotter
from insights.utils.filtering import column_filter

from pylatex import NoEscape

def cluster_analysis(df, target_variable=None, dimensions=2, categorical=False):
    clusterer = ClusterPermutator(df, dimensions=dimensions, categorical=categorical)
    plotter = Plotter(target_variable=target_variable, dimensions=dimensions)
    
    analysis = {}
    high_score = 0
    
    _, categorical_columns = column_filter(df, target_data='categorical')
    counts_columns = categorical_columns + ['cluster_group']
    
    scores_dict = {}
    labels_dict = {}
            
    texts = []
    tables = []
    for function_name, info in zip(clusterer.functions, clusterer.information):        
        title = f'{function_name}'
                
        scores, df_ohe = clusterer.functions[function_name]()
        
        cluster_df = scores[0]['labelled_df']
            
        figure = plotter.plot(df_ohe, scores, title=title)
        cf_figure, cfs = plotter.plot_conf(df, scores, title)
        figure += cf_figure
        
        group_statistics = []
        n_grupos = scores[0]['n']

        
        scores_dict[function_name] = {" - ".join(score['labels']): score['score'] for score in scores}    

        text = f'A melhor separação de grupos ocorreu nas features: {list(scores[0]["labels"])} com uma quantidade de {n_grupos} grupos. ' + clusterer.information[info]
        
        texts.append(text)
        
        tables.append(cfs[0])
            
        cluster_score = scores[0]['score']
        
        if cluster_score > high_score:
            score_dict = {'score': cluster_score, 'cluster_df': cluster_df}
            high_score = cluster_score
    

    
    texts.append('Na tabela abaixo podemos observar a comparação de todos os métodos de clustering testados. O método com o maior score será considerado o melhor método, sendo este utilizado nas próximas análises.')
    tables.append(pd.DataFrame.from_dict(scores_dict))
          
    numerical_group, categorical_group = cluster_pivot(score_dict['cluster_df'], df, categorical_columns) 
    
        
    return texts, tables, numerical_group, categorical_group


def numerical_insights(numerical_group): 
    title = 'Insights - Variáveis Numéricas'
    schema = {'section_title': title, 'information': []}
    
    
    numerical_pivot = pd.DataFrame([
        numerical_group[key]['mean diff'] for key in numerical_group
    ], index=numerical_group.keys())
    numerical_pivot.columns = numerical_pivot.columns.astype(str)
    
    numerical_pivot_std = pd.DataFrame([
        numerical_group[key]['std diff'] for key in numerical_group
    ], index=numerical_group.keys())
    numerical_pivot_std.columns = numerical_pivot_std.columns.astype(str)
    

    
    texts = []
    texts.append('Insights obtidos das variáveis numéricas estão disponíveis nas tabelas a seguir, onde são apresentadas as diferenças das médias e variâncias entre a população geral e cada um dos grupos. A idéia é facilitar a observação de tendências distintas em cada um dos grupos, em relação a população geral. A tabela abaixo é relacionada com a diferença de médias entre os grupos e a população geral.')

    tables = []
    
    tables.append(numerical_pivot)
    
    texts.append('Abaixo podemos observar a tabela de variância entre os grupos e a população geral. Esta tabela de variância é importante de um ponto de vista de análise da variação das features dentro de cada um dos grupos. A ideia é que a variância dentro de um grupo específico seja menor em relação a população em geral.')
    
    tables.append(numerical_pivot_std)
    
    texts.append('Figuras também são aliadas importantes na visualização de dados. Nas figuras abaixo estão presentes duas figuras que representam a variação de média e variância de cada grupo em relação a população geral. Dados variando para a cor azul significam que a variação é negativa, enquanto dados variando para cores vermelhas significam que a variação é positiva.\n')
        
    figures = []
    
    figures.append(px.imshow(numerical_pivot, title=title + ' - Médias', ))
    
    figures.append(px.imshow(numerical_pivot_std, title=title + ' - Variâncias', ))
    
        
    pivot_matrix = numerical_pivot.to_numpy()
    max_idx = np.unravel_index(np.argmax(pivot_matrix), pivot_matrix.shape)
    max_value = np.max(pivot_matrix)
    min_idx = np.unravel_index(np.argmin(pivot_matrix), pivot_matrix.shape)
    min_value = np.min(pivot_matrix)
    
    texts.append(f'A maior diferença populacional positiva foi detectada na feature {numerical_pivot.index[max_idx[0]]} e no grupo {numerical_pivot.columns[max_idx[1]]}, com valor de {max_value:.2f}. A maior variação negativa foi na feature {numerical_pivot.index[min_idx[0]]} e no grupo {numerical_pivot.columns[min_idx[1]]}, com o valor registrado de {min_value:.2f}\n')
    return texts, figures, tables

def categorical_insights(categorical_group):
    schema = {'section_title': 'Insights - Variáveis Categóricas', 'information': []}
    
    maximum = {}
    minimun = {}
    
    for key in categorical_group:
        
        pop_dif = categorical_group[key].iloc[3].to_numpy()
        max_val = np.max(pop_dif)
        argmax = np.argmax(pop_dif)
        min_val = np.min(pop_dif)
        argmin = np.argmin(pop_dif)
        
        biggest = categorical_group[key].iloc[:, argmax]
        biggest.loc['grupo'] = argmax
        
        lowest = categorical_group[key].iloc[:, argmin]
        lowest.loc['grupo'] = argmin

        maximum[key] = biggest
        minimun[key] = lowest
    
    text = 'É possível observar nas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. '
    
    tables = []
    tables.append(
        pd.DataFrame.from_dict(maximum)
    )
    
    tables.append(
        pd.DataFrame.from_dict(minimun)
    )

        
    return text, tables

def cluster_pivot(cluster_df, df, categorical_columns):
    
    numerical_grouping = {}
    
    mean = cluster_df.groupby(['cluster_group']).mean()   
    std = cluster_df.groupby(['cluster_group']).std()
    
    for column in mean.columns:
        column_mean = df[column].to_numpy().mean()
        column_diff = pd.Series(mean[column] - column_mean, name='mean diff')
        column_std = df[column].to_numpy().std()
        column_std_diff = pd.Series(std[column] - column_std, name='std diff')
        
        column_df = mean[[column]]
        column_df = column_df.rename(columns={column: 'mean'})
        column_df['mean diff'] = column_diff
        
        column_df['std'] = std[column]
        column_df['std diff'] =  column_std_diff
                
        numerical_grouping[column] = column_df
        
    categorical_grouping = {}
    
    for column in categorical_columns:
        pivot = pd.crosstab(cluster_df['cluster_group'], df[column])
        pivot_max = pd.Series(pivot.idxmax(axis=1), name=f'maior ocorrencia')
        pivot_count = pd.Series(pivot.max(axis=1), name=f'contagem')
        pivot_pop = pd.Series(pivot_count / np.sum(pivot.to_numpy(), axis=1), name=f'proporção')
        column_pop = df[column].value_counts() / len(df)
        
        diff = {i: pop - column_pop[max_value] for i, (max_value, pop) in enumerate(zip(pivot_max, pivot_pop))}
        diff = pd.Series(diff, name=f'diferença da população')
        
        pivot_normalized = pd.crosstab(cluster_df['cluster_group'], df[column], normalize='columns')
        pivot_max_normalized = pd.Series(pivot_normalized.idxmax(axis=1), name=f'maior ocorrencia normalizada')
        pivot_freq = pd.Series(pivot_normalized.max(axis=1), name=f'frequencia')
        
        dataframe = pd.DataFrame([
            pivot_max, 
            pivot_count, 
            pivot_pop, 
            diff,  
            ], columns=pivot.index)
        categorical_grouping[column] = dataframe
    return numerical_grouping, categorical_grouping