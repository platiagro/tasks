import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi


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
    
    def fit(self, contexts,doc_ids):
        ''' contexts is an iterable of strings
        '''
        if self.preproc:
            contexts = self.preproc.transform(contexts)
        self.contexts = contexts
        self.vectorizer.fit(contexts)
        self.context_vec = self.vectorizer.transform(contexts)
        self.doc_ids = doc_ids

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
            top_doc_ids = np.array([self.doc_ids[k] for k in similar_ids])
            sim_contexts.append(top_doc_ids)
            scores.append(pair_sim[i][similar_ids])
        
        sim_contexts = np.array(sim_contexts)
        scores = np.array(scores)
        
        return sim_contexts, scores

    
class W2VRetriever:
    ''' Passage retriever based on pre-trained W2V.
        The responsability of persisting document vectors is not of this class.
        Save the class instance to disk instead.
    '''
    def __init__(self, w2v_model, preproc=None):
        ''' w2v_model is a W2V model
            preproc is a callable
        '''
        self.preproc = preproc
        self.w2v = w2v_model
    
    def _phrase2vec(self, phrase):
        ''' s is a string
        '''
        dim = self.w2v.vector_size
        vecs = []
        for w in phrase:
            if w not in self.w2v:
                vecs.append(np.zeros(dim))
            else:
                vecs.append(self.w2v[w])
                
        vec = np.mean(vecs, axis=0)
        return vec
    
    def _transform(self, corpus):
        ''' corpus is an iterable of strings
        '''
        vecs = []
        for s in corpus:
            vec = self._phrase2vec(s)
            vecs.append(vec)
        return np.array(vecs)

    def fit(self, contexts,doc_ids):
        ''' contexts is an iterable of strings
        '''
        if self.preproc:
            contexts = self.preproc.transform(contexts)
        self.contexts = contexts
        self.context_vec = self._transform(contexts)
        self.doc_ids = doc_ids

    def __call__(self, questions, top=100):
        ''' questions is a string or iterable of strings
        '''
        if isinstance(questions, str):
            questions = [questions]
        
        if self.preproc:
            questions = self.preproc.transform(questions)
        
        question_vec = self._transform(questions)
        pair_sim = np.dot(question_vec, self.context_vec.T)
        
        sim_contexts = []
        scores = []
        
        for i in range(len(questions)):
            similar_ids = np.argsort(pair_sim[i])[::-1][:top]
            top_doc_ids = np.array([self.doc_ids[k] for k in similar_ids])
            sim_contexts.append(top_doc_ids)
            scores.append(pair_sim[i][similar_ids])

        
        sim_contexts = np.array(sim_contexts)
        scores = np.array(scores)
        
        return sim_contexts, scores

class BM25Retriever:
    ''' Passage retriever based on BM25.
        The responsability of persisting document vectors is not of this class.
        Save the class instance to disk instead.
    '''
    def __init__(self, preproc=None, **kwargs):
        ''' preproc is a callable
        '''
        self.preproc = preproc
        self.k1 = kwargs['k1']
        self.b = kwargs['b']
    
    def fit(self, contexts,doc_ids):
        ''' contexts is an iterable of strings
        '''
        if self.preproc:
            contexts = self.preproc.transform(contexts)
        self.contexts = contexts
        self.bm25 = BM25Okapi(self._tokenize(contexts),
                              k1=self.k1,
                              b=self.b)
        self.doc_ids = doc_ids
    
    def _tokenize(self, corpus):
        return [doc.split(' ') for doc in corpus]

    def __call__(self, questions, top=100):
        ''' questions is a string or iterable of strings
        '''
        if isinstance(questions, str):
            questions = [questions]
        
        if self.preproc:
            questions = self.preproc.transform(questions)
        
        scores = []
        tok_questions = self._tokenize(questions)
        for q in tok_questions:
            score = self.bm25.get_scores(q)
            scores.append(score)

        sim_contexts = []
        sim_scores = []
        for _score in scores:
            similar_ids = np.argsort(_score)[::-1][:top]
            top_doc_ids = np.array([self.doc_ids[k] for k in similar_ids])
            sim_contexts.append(top_doc_ids)
            sim_scores.append([_score[i] for i in similar_ids])
            
        sim_contexts = np.array(sim_contexts)
        sim_scores = np.array(sim_scores)
        
        return sim_contexts, sim_scores
