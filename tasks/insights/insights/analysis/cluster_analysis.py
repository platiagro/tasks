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

def cluster_analysis(df, target_variable=None, dimensions=2, categorical=False, outliers=None):
    clusterer = ClusterPermutator(df, dimensions=dimensions, categorical=categorical)
    plotter = Plotter(target_variable=target_variable, dimensions=dimensions)
    
    analysis = {}
    high_score = 0
    
    _, categorical_columns = column_filter(df, target_data='categorical')
    counts_columns = categorical_columns + ['cluster_group']
    
    schema = {'section_title': 'Análise de Cluster', 'information': []}

    schema['information'].append(
        {
            'type': 'text',
            'info': f'O clustering ou análise de agrupamento de dados é o conjunto de técnicas de prospecção de dados (data mining) que visa fazer agrupamentos automáticos de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema e, dependendo, do algoritmo. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). O procedimento de agrupamento (clustering) também pode ser aplicado a bases de texto utilizando algoritmos de prospeção de texto (text mining), onde o algoritmo procura agrupar textos que falem sobre o mesmo assunto e separar textos de conteúdo diferentes. '
        }
    )
    scores_dict = {}
    labels_dict = {}
    
    for function_name, info in zip(clusterer.functions, clusterer.information):        
        title = f'{function_name}'
        subschema = {'section_title': title, 'information': []}
        
                
        scores, df_ohe = clusterer.functions[function_name]()
        
        cluster_df = scores[0]['labelled_df']
        if outliers is not None:
            cluster_df = cluster_df.append(outliers)
        
        figure = plotter.plot(df_ohe, scores, title=title)
        cf_figure, cfs = plotter.plot_conf(df, scores, title)
        figure += cf_figure
        
        group_statistics = []
        n_grupos = len(cluster_df['cluster_group'].unique())
        text = ''
        
        scores_dict[function_name] = {" - ".join(score['labels']): score['score'] for score in scores}    
        
        subschema['information'].append(
            {
                'type': 'text',
                'info': f'A melhor separação de grupos ocorreu nas features: {list(scores[0]["labels"])} com uma quantidade de {n_grupos} grupos. ' + clusterer.information[info]
            }
        )
        
        subschema['information'].append(
            {
                'type': 'text',
                'info': NoEscape(r'A matriz de separação abaixo mostra a distribuição populacional normalizada dentro de cada grupo de cluster. Note que valores maiores significam que há maior presença daquela população dentro daquele grupo. Este tipo de tabela também pode ser chamado de matriz de confusão, do inglês Confusion Matrix.')
            }
        )

        subschema['information'].append(
            {
                'type': 'table', 
                'caption': 'Matriz de separação do melhor agrupamento',
                'label': r'tab:matsep',
                'table': cfs[0],
                'float_fmt': "%.2f"
            }
        )
        
        schema['information'].append(
        {
            'type': 'subsection',
            'schema': subschema
            }
        )
            
        cluster_score = scores[0]['score']
        
        if cluster_score > high_score:
            score_dict = {'score': cluster_score, 'cluster_df': cluster_df}
            high_score = cluster_score
    

    
    subschema = {'section_title': 'Comparação dos Métodos', 'information': []}
    
    subschema['information'].append(
        {
            'type': 'text',
            'info': NoEscape(r'Na tabela abaixo podemos observar a comparação de todos os métodos de clustering testados. O método com o maior score será considerado o melhor método, sendo este utilizado nas próximas análises.')
        }
    )
    
    subschema['information'].append(
        {
            'type': 'table',
            'caption': 'Análise de score do agrupamento.',
            'table': pd.DataFrame.from_dict(scores_dict),
            'label': r'tab:clustertypes',
            'float_fmt': "%.2f"
        }
    )
    
    schema['information'].append(
        {
            'type': 'subsection',
            'schema': subschema
        }
    )
    
    numerical_group, categorical_group = cluster_pivot(score_dict['cluster_df'], df, categorical_columns) 
    
    subschema = numerical_insights(numerical_group)
    
    schema['information'].append(
        {
            'type': 'subsection',
            'schema': subschema
        }
    )
        
    subschema = categorical_insights(categorical_group)
    
    schema['information'].append(
        {
            'type': 'subsection',
            'schema': subschema
        }
    )

    schema['information'].append(
        {
            'type': 'subsection',
            'schema': group_analysis(numerical_group, categorical_group)
        }
    )
    
    return schema


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
    
    fig_mean = px.imshow(numerical_pivot, title=title + ' - Médias', )
    
    fig_std = px.imshow(numerical_pivot_std, title=title + ' - Variâncias', )
    
    schema['information'].append(
        {
            'type': 'text',
            'info': NoEscape(r'Insights obtidos das variáveis numéricas estão disponíveis nas tabelas de médias e variâncias abaixo, onde são apresentadas as diferenças das médias e variâncias entre a população geral e cada um dos grupos. A idéia é facilitar a observação de tendências distintas em cada um dos grupos, em relação a população geral. A tabela de variância é importante de um ponto de vista de análise da variação das features dentro de cada um dos grupos. A ideia é que a variância dentro de um grupo específico seja menor em relação a população em geral.',)
        }
    )
    
    schema['information'].append(
        {
            'type': 'text',
            'info': NoEscape(r'Figuras também são aliadas importantes na visualização de dados. Nas figuras de médias e variâncias abaixo estão presentes duas figuras que representam a variação de média e variância de cada grupo em relação a população geral. Dados variando para a cor azul significam que a variação é negativa, enquanto dados variando para cores vermelhas significam que a variação é positiva.')
        }
    )
        
    schema['information'].append(
        {
            'type': 'table',
            'caption': 'Diferença de Média entre População - Grupos',
            'table': numerical_pivot,
            'label': r'tab:media',
            'float_fmt': "%.2f"
        }
    )
    
    schema['information'].append(
        {
            'type': 'table',
            'caption': 'Diferença de Variância entre População - Grupos',
            'table': numerical_pivot_std,
            'label': r'tab:var',
            'float_fmt': "%.2f"
        }
    )
        
    schema['information'].append(
        {
            'type': 'figure',
            'caption': 'Diferença de Média entre População - Grupos',
            'figure': fig_mean,
            'label': r'fig:media',
            'package': 'plotly',
            'width': r'0.5\textwidth'
        }
    )
    
    schema['information'].append(
        {
            'type': 'figure',
            'caption': 'Diferença de Variância entre População - Grupos',
            'figure': fig_std,
            'label': r'fig:var',
            'package': 'plotly',
            'width': r'0.5\textwidth'
        }
    )
        
    pivot_matrix = numerical_pivot.to_numpy()
    max_idx = np.unravel_index(np.argmax(pivot_matrix), pivot_matrix.shape)
    max_value = np.max(pivot_matrix)
    min_idx = np.unravel_index(np.argmin(pivot_matrix), pivot_matrix.shape)
    min_value = np.min(pivot_matrix)
    
    schema['information'].append(
        {
            'type': 'text',
            'info': f'A maior diferença populacional positiva foi detectada na feature {numerical_pivot.index[max_idx[0]]} e no grupo {numerical_pivot.columns[max_idx[1]]}, com valor de {max_value:.2f}. A maior variação negativa foi na feature {numerical_pivot.index[min_idx[0]]} e no grupo {numerical_pivot.columns[min_idx[1]]}, com o valor registrado de {min_value:.2f}\n'
        }
    ) 
    
    # pivot_matrix = numerical_pivot_std.to_numpy()
    # max_idx = np.unravel_index(np.argmax(pivot_matrix), pivot_matrix.shape)
    # max_value = np.max(pivot_matrix)
    # min_idx = np.unravel_index(np.argmin(pivot_matrix), pivot_matrix.shape)
    # min_value = np.min(pivot_matrix)


    # text += f'Variância: \n \t Aumento: {numerical_pivot_std.index[max_idx[0]]} no grupo {numerical_pivot_std.columns[max_idx[1]]} - {max_value:.2f}\n \t Diminuição:  {numerical_pivot_std.index[min_idx[0]]} no grupo {numerical_pivot_std.columns[min_idx[1]]} - {min_value:.2f}\n'
    
    return schema

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
    
    schema['information'].append(
        {
            'type': 'text',
            'info': NoEscape(r'É possível observar nas tabelas em ambas tabelas abaixo alguns dados notáveis extraídos dos grupos da base de dados. Estas tabelas de diferenças máximas e mínimas visam demonstrar as diferenças de distribuição entre a população e os grupos. A linha Contagem mostra a contagem daquela classe dentro do grupo, A linha Proporção mostra a proporção da classe em relação a população do grupo, A linha Diferença da População mostra a diferença de proporção daquela população no grupo em relação a população geral. ')
        }
    )
    schema['information'].append(
        {
            'type': 'table', 
            'caption': 'Diferença Máxima de População entre Grupos e Dataset',
            'label': r'tab:notavelmax',
            'table': pd.DataFrame.from_dict(maximum)
        }
    )
    
    schema['information'].append(
        {
            'type': 'table', 
            'caption': 'Diferença Mínima de População entre Grupos e Dataset',
            'label': r'tab:notavelmin',
            'table': pd.DataFrame.from_dict(minimun)
        }
    )
        
    return schema

def cluster_pivot(cluster_df, df, categorical_columns):
    
    numerical_grouping = {}
    
    mean = cluster_df.groupby(['cluster_group']).mean()   
    std = cluster_df.groupby(['cluster_group']).std()
     
    for column in mean.columns:
        column_mean = df[column].to_numpy().mean()
        column_diff = pd.Series(mean[column] - column_mean, name='mean diff')
        column_std = df[column].to_numpy().std()
        column_std_diff = pd.Series((mean[column] - column_mean)/column_std, name='std diff')
        
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
        diff = {index: pop - column_pop[max_value] for max_value, pop, index in zip(pivot_max, pivot_pop, pivot.index)}
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

def group_analysis(numerical_grouping, categorical_grouping):
    group_info = {}
    for group in numerical_grouping:
        for index, row in numerical_grouping[group].iterrows():
            if row['std diff'] > 0.5:
                if index in group_info:
                    group_info[index] += ['Média maior que a população: '+group]
                else:
                    group_info[index] = ['Média maior que a população: '+group]
            if row['std diff'] < -0.5:
                if index in group_info:
                    group_info[index] += ['Média menor que a população: '+group]
                else:
                    group_info[index] = ['Média menor que a população: '+group]
    
    for group in categorical_grouping:
        df = categorical_grouping[group]
        for column in df.columns:
            if df[column].loc['diferença da população'] > 0.1:
                if column in group_info:
                    group_info[column] += [f'Presença maior de população na feature {group}: '+df[column].loc['maior ocorrencia']]
                else:
                    group_info[column] = [f'Presença maior de população na feature {group}: '+df[column].loc['maior ocorrencia']]
    
    group_info = {k: group_info[k] for k in sorted(group_info)}
                 
    schema = {'section_title': 'Insights - Resumo Clustering', 'information': []}
    
    schema['information'] = [
        {'type': 'text',
        'info': 'Os seguintes insights resumidos foram obtidos a partir dos métodos de agrupamento apresentados:'
        },
        *[{'type': 'text', 'info': 'Grupo '+str(key)+': '+', '.join(group_info[key])} for key in group_info]
    ]
    return schema