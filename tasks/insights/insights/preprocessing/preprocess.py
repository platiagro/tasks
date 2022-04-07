import pandas as pd 

def to_float(x):
    if type(x) == str:
        try:
            x = x.replace(',', '.')
            return float(x)
        except ValueError:
            return x
    else:
        return x
        

def df_to_float(df):
    for column in df.columns:
        df[column] = df[column].apply(lambda x: to_float(x))
    return df

def num_2_cat(df, column):
    if df[column].nunique() > 5:
        series = pd.cut(df[column], 5)
    else:
        series = df[column]
    return series

def df_nan_process(df):
    for column in df.columns:
        n_nans = df[column].isna().sum()
        p_nans = n_nans / len(df[column])
        if p_nans > 0.6:
            # Column is categorical or numerical, change nans accordingly
            df_n_nans = df[column].dropna(how='any')
            if df_n_nans.dtype == float:
                df[column] = df[column].fillna(0.0)
            if df_n_nans.dtype == int:
                df[column] = df[column].fillna(0)
            else:
                df[column] = df[column].fillna('-')
    df = df.dropna(how='any')
    return df