import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import re

class time_feature_eng():
  def __init__(self, file_path, resample=None):

    """
      Description.
    """

    # Reading file
    self.dataset = self.read_file(file_path)

    # Drop null cols
    self.dataset.dropna(axis=1, inplace=True)

    # Drop null rows
    self.dataset.dropna(axis=0, inplace=True)

    # Chaging , to .
    self.dataset.replace(',', '.', regex=True, inplace=True)

    # drop columns that just has one unique value
    for column in self.dataset.columns:
      if self.dataset[column].nunique() <= 1:
        self.dataset.drop(column, axis=1, inplace=True)

    # Columns
    self.columns = self.dataset.columns

    # DateTime cols
    # Check if there is datatime columns, if not, dont execute anything
    self.datatime_cols = self.get_datatime_column()
    # If None, exit object
    if self.datatime_cols == None:
      print("No Datatime column found.")
      return None # Exit
    print("Datatime cols: ", self.datatime_cols)

    # Features in the dataset excluding datatime
    # Use set to subtract (not implemented)
    self.features = [feature for feature in self.columns if feature not in self.datatime_cols]
    print("Features: ", self.features)

    # Categorical features
    self.categorical, self.numerical = self.categorical_numeric_features()
    print("Features categoricas: ", self.categorical)
    print("Features numericas: ", self.numerical)

    # Create a list of datasets
    self.list_dataset = self.create_datetime_col()

    # Will change the period of the datetime features
    # And also will groupby datetime and another feature
    self.resample_choose(resample=resample)

    # New features
    self.new_features = self.new_features_func()

    # Dict
    tmp_dict = {}
    for i, date_col in enumerate(self.datatime_cols):
      tmp_dict[date_col] = self.grouped_tmp[i]
    
    self.grouped_tmp = tmp_dict

  def read_file(self, file_path):

    """
      Read dataset.
    """

    type_file = file_path.split('.')[-1]

    if type_file == 'csv':
      dataset = pd.read_csv(file_path)
    elif type_file == 'xlsx':
      dataset = pd.read_excel(file_path)

    return dataset

  def get_datatime_column(self, ):

    """
      This method will search for any datetime column in the dataset, and return a list of
      columns that has the datetime data.
      Input: None.
      Output: list of datetime cols.
    """

    # list if datatime columns
    datatime_col = []

    # Check if there is any column with pandas datatime type
    for type_, column in zip(self.dataset.dtypes, self.columns):

      if pd.api.types.is_datetime64_ns_dtype(type_):
        datatime_col.append(column)

      elif isinstance(type_, (datetime.datetime, pd.Timestamp, datetime.datetime)):
        datatime_col.append(column)

    # Checking if there is datatime column with regex
    for column in (self.columns):
      
      text = self.dataset[column][0]

      # Ignore numeric type
      if isinstance(text, (str)):
        x = re.match(r'\d{2}/\d{2}/\d{4}', text)
        y = re.match(r'\d{4}-\d{2}-\d{2}', text)

        if x:
          datatime_col.append(column)

        if y:
          datatime_col.append(column)


    # Raise error in case of empty list
    # May change this line
    if not datatime_col:
      #raise NameError('This dataset has no datatime column.')
      return None

    return datatime_col

  def categorical_numeric_features(self, ):

    """
      Identify if the feature is categorical or numerical.
    """

    categorical_ = []
    numerical_ = []

    for feature in self.features:

      dif = (self.dataset[feature].shape[0] - self.dataset[feature].nunique())/self.dataset[feature].shape[0]

      if dif >= 0.95:
        categorical_.append(feature)
      else:
        numerical_.append(feature)

    return categorical_, numerical_

  def create_datetime_col(self, ):

    """
      Apply pd.to_datetime to every date column, and store each in a new dataset.
    """

    # List of datasets
    list_dataset = []

    # Create datetime columns
    # Transforms to datetime if the columns' value is string type
    for i, date_col in enumerate(self.datatime_cols):

      dataset_copy = self.dataset.copy()
      dataset_copy['time_'+str(i)] = pd.to_datetime(dataset_copy[date_col]) # string to datetime

      dataset_copy.drop([col for col in self.datatime_cols if col not in date_col], axis = 1, inplace=True)

      # Append dataset in the list for each datatime
      list_dataset.append(dataset_copy)

    return list_dataset

  def resample_choose(self, resample):

    if resample == 'week':
      self.grouped_dataset, self.grouped_tmp = self.resample_each_dataset(resample='W')
    elif resample == 'month':
      self.grouped_dataset, self.grouped_tmp  = self.resample_each_dataset(resample='M')
    elif resample == 'year':
      self.grouped_dataset, self.grouped_tmp  = self.resample_each_dataset(resample='Y')
    elif resample == 'trimestre':
      self.grouped_dataset, self.grouped_tmp  = self.resample_each_dataset(resample='Q')
    else:
      self.grouped_dataset, self.grouped_tmp  = self.resample_each_dataset(resample='D')

  def resample_each_dataset(self, resample):

    """
      Method to resample each dataset by day (D), week (W), month (M) or year (Y).
      Will also create new columns: year, month name and year-day.
      Input: resample.
      Output: list of dataset grouped by some frequency.
    """

    # list for every datetime cols
    grouped_dataset = []
    grouped_tmp = []

    # resampling for every dataset
    for idx, dataset in enumerate(self.list_dataset):

      # List for every catgorical cols
      sub_list = []
      tmp_list = []

      for column in self.numerical:
        dataset[column] = pd.to_numeric(dataset[column], errors='coerce').fillna(0, downcast='infer')

      for col_cat in self.categorical:

        # Copy of daatset
        df = dataset.copy()

        # New index with new period
        df.index = pd.DatetimeIndex(df['time_'+str(idx)]).to_period(resample)

        # Concat new column SQR
        df = pd.concat([df, df[self.numerical].pow(2).rename(columns=lambda x: 'SQR_' + x )], axis=1)

        # Groupby
        agg_functions = ['min', 'max', 'count', 'sum']
        agg_df = df.groupby([df.index, col_cat]).agg({col : agg_functions for col in self.numerical + ['SQR_' + col for col in self.numerical]})

        # fill missing [self.datatime_cols, self.categorical] values
        agg_df = agg_df.reindex(
          pd.MultiIndex.from_product([agg_df.index.levels[0],
                                      agg_df.index.levels[1]],
                                      names=['time_'+str(idx),
                                             col_cat])
        )
        agg_df = agg_df.reset_index().sort_values([col_cat, 'time_'+str(idx)],ignore_index=True)

        # Append new dataset for every categorical feature
        sub_list.append(agg_df)
        tmp_list.append(df)

      # Append for every datetime feature
      grouped_dataset.append(sub_list)
      grouped_tmp.append(tmp_list)

    return grouped_dataset, grouped_tmp

  def mean_average_(self, df, group_col, k=3):

    agg_cols = [(col, f) for col in self.numerical for f in ['count', 'sum']]
    res_df = df.groupby(group_col)[agg_cols].rolling(k, min_periods=1).sum()

    for col in self.numerical:
      
      res_df[f'MEAN_{group_col}_{col}_{k}'] = res_df[(col, 'sum')] / res_df[(col, 'count')]
    
    res_df = res_df.drop(agg_cols, axis=1)
    res_df.columns = res_df.columns.droplevel(1)
    return res_df

  def mean_average_extrema(self, df, group_col, extrema='min', k=3):

    agg_cols = [(col, extrema) for col in self.numerical]
    if extrema == 'min':
        res_df = df.groupby(group_col)[agg_cols].rolling(k, min_periods=1).min().shift(1)
    else:
        res_df = df.groupby(group_col)[agg_cols].rolling(k, min_periods=1).max().shift(1)
    
    res_df.columns = res_df.columns.droplevel(1)

    for col in self.numerical:
      res_df = res_df.rename(columns={col: f'{extrema.upper()}_{group_col}_{col}_{k}' for col in col}) 

    return res_df

  def mean_average_std(self, df, group_col, k=3):

    agg_cols = [(col, f) for col in self.numerical + ['SQR_' + col for col in self.numerical] for f in ['count', 'sum']]
    res_df = df.groupby(group_col)[agg_cols].rolling(k, min_periods=1).sum().shift(1)
    
    for col in self.numerical:
        new_name = f'STD_{group_col}_{col}_{k}'
        res_df[new_name] = res_df[('SQR_' + col, 'sum')] - (np.power(res_df[(col, 'sum')], 2) / res_df[(col, 'count')])
        res_df[new_name] = np.sqrt(res_df[new_name]) / (res_df[(col, 'count')] - 1)
        
    res_df = res_df.drop(agg_cols, axis=1)
    res_df.columns = res_df.columns.droplevel(1) 
    return res_df

  def new_features_func(self, ):

    new_features = pd.DataFrame([])

    for i, sub_list in enumerate(self.grouped_dataset):

      for j, dataset in enumerate(sub_list):

        df = pd.DataFrame([])

        df = pd.concat([
        pd.concat([self.mean_average_(dataset, self.categorical[j], k) for k in [3, 6, 9]], axis=1), # olhar isso aqui
        pd.concat([self.mean_average_std(dataset, self.categorical[j], k) for k in [3, 6, 9]], axis=1),
        pd.concat([self.mean_average_extrema(dataset, self.categorical[j], 'min', k) for k in [3, 6, 9]], axis=1),
        pd.concat([self.mean_average_extrema(dataset, self.categorical[j], 'max', k) for k in [3, 6, 9]], axis=1)
        ], axis=1)
        

        df['time_'+str(i)] = dataset['time_'+str(i)].to_list()
        df[self.categorical[j]] = dataset[self.categorical[j]].to_list()

        #remove unnecessary column
        self.grouped_tmp[i][j].drop(['SQR_' + col for col in self.numerical], axis=1, inplace=True)

        #merge the generated features with the original data
        self.grouped_tmp[i][j].set_index(pd.Index(self.grouped_tmp[i][j][self.categorical[j]]), append=True, inplace=True)
        df.set_index(['time_'+str(i), self.categorical[j]], inplace=True)
        self.grouped_tmp[i][j] = pd.merge(self.grouped_tmp[i][j], df, left_index=True, right_index=True)

        #reset index and sort values
        self.grouped_tmp[i][j].set_index(pd.RangeIndex(start=0, stop=self.grouped_tmp[i][j].shape[0], step=1), inplace=True)

        #new_features = pd.concat([new_features, df],axis=1)

    #return new_features

  def mean_plot(self, date_col):

    lis_ = [col + '_x' for col in self.numerical] + [col + '_y' for col in self.numerical] + [col for col in self.datatime_cols] + ['time_'+str(idx) for idx,_ in enumerate(self.datatime_cols)]
    columns = set(self.grouped_tmp[date_col][0]) - set(self.features) - set(lis_)

    for col in columns:
      fig = px.line(self.grouped_tmp[date_col][0], x='time_0', y=col,
                    markers=True,
                    title = f'{col} x {date_col}')
      fig.show()

  def std_plot(self, date_col):

    for col_num in self.numerical:
      for col_cat in self.categorical:
        for num in [3, 6, 9]:
          y = f'STD_{col_cat}_{col_num}_' + str(num)

          fig = px.line(self.grouped_tmp[date_col][0], x='time_0', y=y,
                    markers=True,
                    title = f'{y} x {date_col}')
          fig.show()

  def cat_plot(self, date_col):

    for col_cat in self.categorical:

      count = self.grouped_tmp[date_col][0][col_cat].value_counts(normalize=True) * 100

      fig = px.bar(count, title = f'Contagem da variavel {col_cat}')
      fig.show()

  def date_plot(self, ):

    for idx, col in enumerate(self.datatime_cols):

      day_week = [date.day_name() for date in self.grouped_tmp[col][0]['time_'+str(idx)]]
      day_week = pd.Series(day_week, name='Dia da semana')
      count = day_week.value_counts(normalize=True) * 100

      fig = px.bar(count, title = f'Contagem da variavel')
      fig.show()

      month = [date.month_name() for date in self.grouped_tmp[col][0]['time_'+str(idx)]]
      month = pd.Series(month, name='Mês')
      count = month.value_counts(normalize=True) * 100

      fig = px.bar(count, title = f'Contagem da variavel')
      fig.show()