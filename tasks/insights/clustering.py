import glob


import pandas as pd
import numpy as np

from insights.analysis.outliers_analysis import outlier_analysis
from insights.analysis.cluster_analysis import cluster_analysis
from insights.preprocessing.preprocess import df_to_float, num_2_cat, df_nan_process
from insights.utils.filtering import column_filter

from insights.markdown_generator.report import Report

datasets = [
    'data/avocado.csv',
    'data/IBM-HR.csv',
    'data/insurance.csv',
    'data/creditcard.csv',
    # 'data/HousingData.csv',
    # 'data/winequality-red.csv',
    # 'data/winequality-white.csv',
    # 'data/titanic.csv',
    # 'data/Mall_Customers.csv',
    # 'data/Iris.csv',
    # 'data/cdc_zika.csv',
    # 'data/HousePrices.csv'
    ]

target_variables = {
    'data/avocado.csv': 'AveragePrice',
    'data/IBM-HR.csv': 'PerformanceRating',
    'data/insurance.csv': 'charges',
    'data/creditcard.csv': 'Class',
    'data/HousingData.csv': 'MEDV',
    'data/winequality-red.csv': 'quality',
    'data/winequality-white.csv': 'quality',
    'data/titanic.csv': 'Survived',
    'data/Mall_Customers.csv': 'Spending Score (1-100)',
    'data/Iris.csv': 'variety',
    'data/cdc_zika.csv': 'value',
    'data/HousePrices.csv': 'SalePrice'
}

drop_columns = {
    'data/avocado.csv': ['Date'],
    'data/IBM-HR.csv': [],
    'data/insurance.csv': [],
    'data/creditcard.csv': ['Time'],
    'data/HousingData.csv': [],
    'data/winequality-red.csv': [],
    'data/winequality-white.csv': [],
    'data/titanic.csv': ['PassengerId', 'Name', 'Ticket', 'Cabin'],
    'data/Mall_Customers.csv': ['CustomerID'],
    'data/Iris.csv': [],
    'data/cdc_zika.csv': ['report_date', 'time_period', 'time_period_type', 'unit'],
    'data/HousePrices.csv': ['Id', 'MiscFeature', 'MiscVal', 'SaleType', 'SaleCondition'],
}

for i, dataset in enumerate(datasets):
    report = Report('CPQD AutoML Algorithm - '+str(i))
    
    target = target_variables[dataset]
    
    df = pd.read_csv(dataset).iloc[:5000]
        
    df = df.drop(drop_columns[dataset], axis=1)
        
    df = df_to_float(df)
    
    df = df_nan_process(df)
        
    # Outlier determination
    schema, filtered_df, outliers_df = outlier_analysis(df)
            
    report.add_section(schema)

    schema = cluster_analysis(df, target_variable = target, dimensions=2, categorical=False, outliers=outliers_df)

    report.add_section(schema)

    report.process()



