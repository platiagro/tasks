import PyPDF4
import matplotlib.pyplot as plt
from os import popen, makedirs
from os.path import isdir, basename
from time import sleep


class PDF_IO:
    
    def read_pdf(self, path: str):
        """
        Read PDF file with PyPDF4 library.
        Args:
            path (str): file path.
        Returns:
            (str): text found inside PDF file.
        """

        # Open file
        pdfFileObj = open(path, 'rb') 
        pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

        # Read pages
        pages = [pdfReader.getPage(i).extractText() for i in range(pdfReader.numPages)]

        # Close file
        pdfFileObj.close()

        return pages


    def _read_spaced_pdf(self, path: str):
        """
        Read PDF file with pdftotext command.
        Args:
            path (str): file path.
        Returns:
            (str): text found inside PDF file with approximate spacing.
        """
        tmp_dir = '/tmp/pdf2text'
        if not isdir(tmp_dir):
            makedirs(tmp_dir)
        
        tmp_path = basename(path)[:-3] + 'txt'
        tmp_path = f'{tmp_dir}/{tmp_path}'
        
        popen(f'pdftotext -r 144 -layout "{path}" "{tmp_path}"')
        
        tries = 0
        max_tries = 3
        while tries < max_tries:
            try:
                with open(tmp_path, 'r') as f:
                    _txt = f.read()
                break
            except FileNotFoundError as e:
                if tries == max_tries:
                    raise e
                tries += 1
                sleep(1)
            
        return _txt
