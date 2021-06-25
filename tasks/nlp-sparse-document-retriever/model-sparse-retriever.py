import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfRetriever:
    ''' Passage retriever based on TF-IDF.
        The responsability of persisting document vectors is not of this class.
        Save the class instance to disk instead.
    '''
    def __init__(self, binary=True, preproc=None):
        ''' preproc is a callable
        '''
        self.preproc = preproc
        self.vectorizer = TfidfVectorizer(binary=binary)
    
    def fit(self, contexts):
        ''' contexts is an iterable of strings
        '''
        if self.preproc:
            contexts = self.preproc.transform(contexts)
        self.contexts = contexts
        self.vectorizer.fit(contexts)
        self.context_vec = self.vectorizer.transform(contexts)
        #self.contexts = contexts

    def __call__(self, questions, top=100):
        ''' questions is a string or iterable of strings
        '''
        if isinstance(questions, str):
            questions = [questions]
        
        if self.preproc:
            questions = self.preproc.transform(questions)

        question_vec = self.vectorizer.transform(questions)
        pair_sim = np.dot(question_vec, self.context_vec.T).toarray()
        
        sim_contexts = []
        scores = []
        for i in range(len(questions)):
            similar_ids = np.argsort(pair_sim[i])[::-1][:top]
            sim_contexts.append(similar_ids)
            scores.append(pair_sim[i][similar_ids])
        
        return sim_contexts, scores