import os
from extract import FABC_Extractor
import pandas as pd

def get_reports_as_dataframe(reports_dir,columns_dict):
    fabc_extractor = FABC_Extractor(reports_dir=reports_dir)
    report_contents = fabc_extractor.full_extract()
    data = {'doc_id':[],
           'report_name':[],
           'section_name':[],
           'context':[]}
    
    for doc_id, values in report_contents.items():
        data['doc_id'].append(doc_id)
        data['report_name'].append(values["report_name"])
        data['section_name'].append(values["section_name"])
        data['context'].append(values["text"])
        
    for column_name,is_present in columns_dict.items():
        if not is_present:
            data.pop(column_name)
    
    df = pd.DataFrame(data)
    
    return df