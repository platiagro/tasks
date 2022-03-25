import itertools
import random 
import copy 

import pandas as pd

from sklearn import metrics

from insights.clustering.optimal_clustering import OptimalCluster
from insights.utils.filtering import column_filter

class ClusterPermutator():
    def __init__(self, df, categorical=False, target_variable=None, dimensions=2): 
        self.functions = {
            f'Feature Permutation {dimensions} dim.': self.permutate,
            'Multidimensional': self.multidim_cluster,
        }
        
        self.information = {
            f'Feature Permutation Clustering em {dimensions} dimensões': f'A análise multidimensional em {dimensions} dimensões fornece insights de quais features são mais importantes e que distinguem grupos entre si. Esta análise é realizada realizando a permutação das features do dataset.',
            'Multidimensional Clustering': 'A análise multidimensional de clusters é semelhante a análise bi-dimensional ou tri-dimensional, mas sua principal diferença é que utiliza todas as features disponíveis no dataset.',
        }
        
        self.df = df
        _, categorical_columns = column_filter(df, target_data='categorical')
        _, self.num_cols = column_filter(df, target_data='numerical')
        self.df_ohe = pd.get_dummies(df, columns=categorical_columns)
        
        self.clusterer = OptimalCluster()
        self.categorical = categorical
        
        self.categorical_columns = list(set(self.df_ohe) - set(self.num_cols)) if \
            self.categorical else ['']
        
        self.targets_columns = list(itertools.combinations(self.num_cols, dimensions-1)) if \
            self.categorical else list(itertools.combinations(self.num_cols, dimensions))
        
        
        self.total_targets = []
        for categorical in self.categorical_columns:
            for target_column in self.targets_columns:
                combined = list(target_column)
                if self.categorical:
                    combined.append(categorical)
                self.total_targets.append(combined)
        self.total_targets = random.sample(self.total_targets, min(len(self.total_targets), 4))
        
    def permutate(self):
        score_list = []
        for target_column in self.total_targets:
            target_column = list(target_column)
            X = self.df_ohe[target_column].to_numpy()
            # Calcula os clusters e os scores, salva em um dicionário
            n, km, y_pred = self.clusterer.get_opt_cluster(X)
            score = metrics.silhouette_score(X, km.labels_, metric='euclidean')
            labelled_df = self.df
            labelled_df['cluster_group'] = [str(x) for x in y_pred]
            score_list.append(
                {'score': score, 'X': X, 'y_pred': y_pred, 'labels': target_column, 'n': n, 'labelled_df': copy.deepcopy(labelled_df)}
                )
        # Ordena a lista: 
        score_list = sorted(score_list, key=lambda x: -x['score'])
        return score_list[0:3], self.df_ohe

    def multidim_cluster(self):
        # Análise multidimensional (Sem plot de gráficos, utilizando todas as features)
        target_column = list(self.df_ohe.columns) if self.categorical else self.num_cols
        X = self.df_ohe[target_column].to_numpy()
        # Calcula os clusters e os scores, salva em um dicionário
        n, km, y_pred = self.clusterer.get_opt_cluster(X)
        score = metrics.silhouette_score(X, km.labels_, metric='euclidean')
        labelled_df = self.df
        labelled_df['cluster_group'] = [str(x) for x in y_pred]
        score_list = [{'score': score, 'X': X, 'y_pred': y_pred, 'labels': target_column, 'n': n, 'labelled_df': labelled_df}]
        return score_list, self.df_ohe