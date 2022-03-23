import numpy as np

from copy import deepcopy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

class OptimalCluster():
    
    def __init__(self):
        self.n_clusters_possibilities = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.weights = {
            'size_std': 0.3,
            'mean_difference': 0.1, 
            'n_bellow_average': 0.5, 
            'n_outliers': 0.5, 
            'id': 1,
        } 
          
    def get_opt_cluster(self, X):
        
        n_cluster_stats = {}
        processed_list = []
        for n_cluster in self.n_clusters_possibilities: 
            clusterer = KMeans(n_clusters=n_cluster).fit(X)
            cluster_labels = clusterer.predict(X)
            
            # Calculate the average silhouette score
            silhouette_avg = silhouette_score(X, cluster_labels)
            
            # Get the silhouette value for each sample
            sample_silhouette_values = silhouette_samples(X, cluster_labels)
            
            # Initialize the important stats for determining the best number of clusters
            i_cluster_stats = {'mean': [], 'std': [], 'mean_diff': [], 'n_under': [], 'n_outliers': [], 'size': []}
            
            for i in range(n_cluster):
                # Calculate the silhouette values for each group
                ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
                mean = ith_cluster_silhouette_values.mean()
                std = ith_cluster_silhouette_values.std()
                diff = ith_cluster_silhouette_values - silhouette_avg
                
                # Important metrics to classify the best number of clusters, for each group
                i_cluster_stats['mean'].append(mean)
                i_cluster_stats['std'].append(std)
                i_cluster_stats['mean_diff'].append(np.power(diff, 2).mean())
                i_cluster_stats['n_under'].append(np.sum(diff < 0)/len(diff))
                i_cluster_stats['n_outliers'].append(np.sum(ith_cluster_silhouette_values < 0))
                i_cluster_stats['size'].append(len(ith_cluster_silhouette_values))
            
            # Processing the data for the batch, now considering all the groups of a determined n of clusters. 
            processed_data = {}
            processed_data['mean_difference'] = np.sum(np.power(i_cluster_stats['mean_diff'], 2))
            processed_data['n_bellow_average'] = np.mean(i_cluster_stats['n_under'])
            processed_data['n_outliers'] = np.sum(i_cluster_stats['n_outliers'])
            processed_data['size_std'] = np.std(i_cluster_stats['size'])
            processed_data['id'] = n_cluster
            processed_list.append(processed_data)
            
            # Saving a copy of the trained model and its output
            n_cluster_stats[n_cluster] = {'clusterer': deepcopy(clusterer), 'y_pred': deepcopy(cluster_labels)}
            

        # Using a cost function to determine the best cluster number, the idea is to minimize J
        J = {}
        for processed in processed_list:
            j = np.sum([self.weights[key]*processed[key] for key in self.weights])
            J[processed['id']] = j
        # Sorting J
        J = {k: v for k, v in sorted(J.items(), key=lambda item: item[1])}
        
        # Getting the lowest value
        n_clusters = int(list(J.keys())[0])
        # Returning the number of clusters, the optimal cluster model and the predictions of the model
        return n_clusters, n_cluster_stats[n_clusters]['clusterer'], n_cluster_stats[n_clusters]['y_pred']