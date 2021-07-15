import os
import json
import pandas as pd
from typing import List
from pickle import load as read_pickle
from pickle import dump as dump_pickle

class IO_Utils(object):
    """ 
    Class with utilities for reading and writing
    """
    def __init__(self):
        pass

    def read_json(self,json_file_path:str):
        with open(json_file_path) as f:
            json_result = json.load(f)
        return json_result
    
    def save_json(self,destination_path:str,d,ensure_ascii=False,command='a'):
        with open(destination_path, command) as fp:
            json.dump(d, fp, ensure_ascii=ensure_ascii)

    def read_pickle(self,filepath:str):
        with open(filepath, 'rb') as f:
            content = read_pickle(f)
        return content

    def save_pickle(self,filepath:str,info):
        """
        Save info in a picke file
        """
        with open(filepath, 'wb') as f:
            dump_pickle(info, f)
    
    def create_folder_structure(self,folder:str):
        """ Create the comple folder structure if it does not exists """
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    def read_line_spaced_txt_file(self,filepath:str):
        with open(filepath, 'r') as infile:
            data = infile.read().splitlines()
        return data
    
    def save_line_spaced_txt_file(self,filepath:str,text_list:List[str]):
        with open(filepath, "w") as output:
            for row in text_list:
                output.write(str(row) + '\n')
    
    def save_df_to_csv(self,filepath:str,df:pd.DataFrame,zipped=False):
        if filepath.split(".")[-1] != "csv":
            raise ValueError(f"{filepath} tem de ter a extensão .csv")

        filepath = filepath.split(".csv")[0]+".csv.gz" if zipped else filepath
        compression =  'gzip' if zipped else 'infer' 
        df.to_csv(filepath, compression=compression)


    def read_csv_to_df(self,filepath:str):
        if ".csv" not in filepath and ".csv.gz" not in filepath:
            raise ValueError(f"{filepath} tem de ter a extensão .csv ou csv.gz")
        df = pd.read_csv(filepath)
        return df