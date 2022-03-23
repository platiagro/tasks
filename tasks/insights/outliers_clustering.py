import pandas as pd
import numpy as np

from insights.analysis.outliers_analysis import outlier_analysis
from insights.analysis.cluster_analysis import cluster_analysis

from insights.markdown_generator.report import Report

from insights.time_feature_creation.time_features import time_feature_eng


# parameters
dataset = "amostra.xlsx" #@param {type:"string"}
group_col = "" #@param {type:"string",label:"coluna para o agrupamento"}
target = "" # pode ter ou não


def decimal_converter(value):
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return value
    
# numerical_cols = [
#     'Tempo de Dispensa (dias)', 
#     'Tempo de Entrega',
# ]
# features = [
#     'Area de atuacao [Funcionario]',
#     'Descricao do afastamento',
# ]

# converter_dict = {col: decimal_converter for col in numerical_cols}

# df = pd.read_excel(dataset, index_col=None, header=0, converters=converter_dict)
# df_num = df[numerical_cols]

# df = df_num.join(df[features]).dropna(how='any')
df = pd.read_csv('Iris.csv')

report = Report('CPQD AutoML Algorithm')

# Outlier determination
schema, filtered_df, outliers_df = outlier_analysis(df)

report.add_section(schema)

df = filtered_df

# schema = cluster_analysis(df, target_variable = 'Area de atusacao [Funcionario]', dimensions=2, categorical=False, outliers=outliers_df)
schema = cluster_analysis(df, target_variable = 'variety', dimensions=2, categorical=False, outliers=outliers_df)

report.add_section(schema)

report.process()



