import os

import pandas as pd
from glob import glob
from pickle import dump, load
from pdf_reader import PDF_IO
from preprocess import Preprocess
from io_utils import IO_Utils

# Extract Paths
class FABC_Extractor:
    def __init__(self,reports_dir):

        self.paths = glob(f'{reports_dir}/**/*.pdf', recursive=True)
        self.pp = Preprocess()

    def _preproc_text(self,text):
        text = ' '.join(text.split())
        text = text.strip()
        return text
    def full_extract(self):
        res = {}
        _id = 0
        for fn in self.paths:
            pages = PDF_IO().read_pdf(fn)
            est = self.pp.get_structure(pages)
            cont = self.pp.get_strcuture_content(pages, est)

            for k, v in cont.items():
                report_name =  os.path.basename(fn)

                if 'Tabela' in k or 'Figura' in k or 'Anexo' in k:
                    sname = k
                elif k == '':
                    sname = '_raiz'
                elif '.' in k:
                    sname = f'Seção {k}'
                elif 'Anexos' in k:
                    sname = f'Anexos'
                else:
                    sname = f'Capítulo {k}'
                
                report_name = self._preproc_text(report_name)
                sname = self._preproc_text(sname)
                v = self._preproc_text(v)
                
                res[f'{_id}'] = {'report_name':report_name,
                            'section_name': sname,
                            'text': v}
                _id += 1

        return res
    
    def text_extract(self):
        text_list = []
        for fn in self.paths:
            pages = PDF_IO().read_pdf(fn)
            est = self.pp.get_structure(pages)
            cont = self.pp.get_strcuture_content(pages, est)
            for _, v in cont.items():
                v = self._preproc_text(v)
                text_list.append(v)

        return text_list