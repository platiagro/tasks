def column_filter(df, target_data='numerical'):
    possible_targets = [
        'numerical', 
        'categorical', 
    ]
    
    if target_data not in possible_targets: 
        raise ValueError(f'Target data {target_data} not within the possible inputs {" ".join(possible_targets)}')
    else:
        cols = list(df.columns)
        num_cols = list(df._get_numeric_data().columns)
        categorical_columns = list(set(cols) - set(num_cols))
        filtered_df = df[num_cols] if target_data == 'numerical' else df[categorical_columns]
        columns = num_cols if  target_data == 'numerical' else categorical_columns
             
        return filtered_df, columns