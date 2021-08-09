import os
import pandas as pd
from vident.io_utils import IO_Utils
import faiss

from vident.document_retriever.sparse_similarity.similarity import TfidfVectorizer

from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt

#import faiss
import numpy as np


class FaissKMeans:
    def __init__(self, n_clusters=8, n_init=10, max_iter=300):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.kmeans = None
        self.cluster_centers_ = None
        self.inertia_ = None

    def fit(self, X, y):
        self.kmeans = faiss.Kmeans(d=X.shape[1],
                                   k=self.n_clusters,
                                   niter=self.max_iter,
                                   nredo=self.n_init)
        self.kmeans.train(X.astype(np.float32))
        self.cluster_centers_ = self.kmeans.centroids
        self.inertia_ = self.kmeans.obj[-1]

    def predict(self, X):
        return self.kmeans.index.search(X.astype(np.float32), 1)[1]


if __name__ == '__main__':
    root_dir = os.path.join(os.path.abspath(os.getcwd()).replace('= ',''))
    data_dir = os.path.join(root_dir,"data")
    qgenerator_dir = os.path.join(data_dir,'qgenerator')
    context_questions_map_path = os.path.join(qgenerator_dir,'context_questions_map.json')
    
    io_utils = IO_Utils()
    context_questions_map = io_utils.read_json(filepath=context_questions_map_path)
    # import pdb;pdb.set_trace()
    example_context = context_questions_map['9']['context']
    # '4.6 Análise Estatística: Os dados obtidos foram submetidos ao estudo da homogeneidade da variância (para estabilizar ou reduzir a variabilidade existente) através do método Box-Cox contido no PROC TRANSREG do Sistema SAS. Como para valores nulos a família de transformações de Box-Cox fica restrita, utilizou-se a variável somada a uma constante (+1.0). fitotoxicidade aos 6 e 18 DAAreinfestação de trapoeraba aos 41 DAAfoi sugerida a transformação dos dados com valor de lambda (+0.0), (-3.0) e (+0.0), respectivamente. Após a transformação dos dados as variáveis fitotoxicidade aos 18 DAAreinfestação de trapoeraba aos 41 DAAnão apresentaram distribuição normal, portanto para estabilizar a variabilidade dos tratamentos foi utilizada a estatística não paramétrica, através do Teste de Friedman. Os dados, então, foram submetidos a análise de variância, sendo a comparação das médias quando significativas realizadas pelo teste LSD ao nível de 5 % de probabilidade. Para a análise dos dados foi utilizado o software SAS.'
    example_questions = context_questions_map['9']['questions']
    # ['Quando foi utilizado o método Box-Cox?',
    #  'Qual foi o critério utilizado para analisar os dados para a análise de variância?',
    #   'Qual foi a frequência do teste paramétrica?',
    #    'Em que nível a análise estatística é realizada?', 
    #    'Qual foi o valor de lambda usado para estabilizar a variabilidade dos tratamentos?', 
    #    'Quantos dados foram submetidos a análise de variância?', 
    #    'Qual foi a função de equação usada para estabilizar a variabilidade dos tratamentos?', 
    #    'O que foi adicionado para estabilizar a variabilidade dos tratamentos?',
    #     'Quantos tratamentos foram submetidos ao estudo da homogeneidade da variância?',
    #      'Qual foi a análise de variância?']
    
    print('example_questions:\n',example_questions)
    
    vectorizer = TfidfVectorizer()
    vectorizer.fit(example_questions)
    vec = vectorizer.transform(example_questions)
    X = vec.toarray()


    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    y_kmeans  = kmeans.predict(X)

    print(kmeans.cluster_centers_)

    print(kmeans.labels_)

    #plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()