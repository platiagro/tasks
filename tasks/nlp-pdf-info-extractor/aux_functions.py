import os
from extract import FABC_Extractor
import pandas as pd

def get_reports_as_dataframe(reports_dir):
    fabc_extractor = FABC_Extractor(reports_dir=reports_dir)
    report_contents = fabc_extractor.full_extract()
    doc_id_list = []
    report_name_list = []
    section_name_list = []
    text_list = []
    for doc_id, values in report_contents.items():
        doc_id_list.append(doc_id)
        report_name_list.append(values["report_name"])
        section_name_list.append(values["section_name"])
        text_list.append(values["text"])

    data = {'doc_id':doc_id_list,
           'report_name':report_name_list,
           'section_name':section_name_list,
           'text':text_list}

    df = pd.DataFrame(data)
    
    return df