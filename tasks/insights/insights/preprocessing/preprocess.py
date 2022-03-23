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
        df[column] = pd.cut(df[column], 5).astype(str)
    return df