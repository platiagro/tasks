import numpy as np

from copy import deepcopy
from insights.utils.filtering import column_filter
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN



class DetOutliers(): 
    def __init__(self, df):
        filtered_df, _ = column_filter(df, target_data='numerical')
        self.df = df
        self.X = filtered_df.to_numpy()
        
        self.functions = {
            'DBscan': self.dbscan_outliers,
            'Isolation Forest': self.isolation_outliers,
        }
        
    def dbscan_outliers(self, eps=2): 
        db = DBSCAN(eps=eps, min_samples=10)
        pred = db.fit_predict(self.X)
        filtered_df = deepcopy(self.df.loc[pred != -1])
        y_pred = np.array([1 if y != -1 else -1 for y in pred])
        outliers_df = deepcopy(self.df.loc[pred == -1])
        return deepcopy(db), y_pred, filtered_df, outliers_df

    def isolation_outliers(self, contamination=0.05):
        clf = IsolationForest(contamination=contamination).fit(self.X)
        y_pred = clf.predict(self.X)
        filtered_df = deepcopy(self.df.loc[y_pred == 1])
        outliers_df = deepcopy(self.df.loc[y_pred == -1])
        return deepcopy(clf), y_pred, filtered_df, outliers_df