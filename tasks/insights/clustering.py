import glob


import pandas as pd
import numpy as np

from insights.analysis.outliers_analysis import outlier_analysis
from insights.analysis.cluster_analysis import cluster_analysis
from insights.preprocessing.preprocess import df_to_float, num_2_cat
from insights.utils.filtering import column_filter

from insights.markdown_generator.report import Report

datasets = glob.glob('data/*.csv')

target_variables = {
    'data/HousingData.csv': 'MEDV',
    'data/winequality-red.csv': 'quality',
    'data/winequality-white.csv': 'quality',
    'data/titanic.csv': 'Survived',
    'data/Mall_Customers.csv': 'Spending Score (1-100)',
    'data/Iris.csv': 'variety'
}

drop_columns = {
    'data/HousingData.csv': [],
    'data/winequality-red.csv': [],
    'data/winequality-white.csv': [],
    'data/titanic.csv': ['PassengerId', 'Name', 'Ticket', 'Cabin'],
    'data/Mall_Customers.csv': ['CustomerID'],
    'data/Iris.csv': []
}

for i, dataset in enumerate(datasets):
    target = target_variables[dataset]
    
    df = pd.read_csv(dataset)
    
    df = df.drop(drop_columns[dataset], axis=1)
    
    df = df_to_float(df)
    
    df = df.dropna(how='any')
    
    _, numerical_columns = column_filter(df, target_data='numerical')
    if target in numerical_columns:
        df = num_2_cat(df, target)
    
    report = Report('CPQD AutoML Algorithm: '+str(i))

    # Outlier determination
    schema, filtered_df, outliers_df = outlier_analysis(df)

    report.add_section(schema)

    df = filtered_df

    schema = cluster_analysis(df, target_variable = target, dimensions=2, categorical=False, outliers=outliers_df)

    report.add_section(schema)

    report.process()



