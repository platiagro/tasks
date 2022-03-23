import numpy as np
import pandas as pd


def confusion_matrix(y_true, y_pred):
    y_true = [str(y) for y in y_true]
    
    # Organizing labels and predictions      
    labels = [str(y) for y in list(set(y_true))]
    indexes = [str(y) for y in list(set(y_pred))]
    
    # Generating a dictionary for mapping label to prediction
    label_dict = {label: i for i, label in enumerate(labels)}
    
    # Matrix where rows are the true labels and columns are the predictions
    conf_mat = np.zeros([len(label_dict), len(indexes)])
    
    # Adding each prediction to the correct spot in the matrix
    for predicted, label in zip(y_pred, y_true):
        conf_mat[label_dict[label], predicted] += 1
    
    # Normalizing the matrix
    labels_sum = np.sum(conf_mat, axis=1).reshape(len(labels), 1)
    conf_mat = conf_mat/labels_sum
    
    # Returning it as a pd dataframe for ease of plotting
    df_cm = pd.DataFrame(conf_mat, columns=indexes, index=labels)
    return df_cm