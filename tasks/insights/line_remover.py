import pandas as pd 

df = pd.read_csv('data/creditcard.csv').iloc[:170_000]

df.to_csv('data/creditcard.csv')