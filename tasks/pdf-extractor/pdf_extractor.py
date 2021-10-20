import fitz
import os
import io
import sys
import pandas as pd
import re

from PIL import Image
from typing import List, Optional

class PDFExtractor():
    def __init__(self, filepath=None):
        if filepath:
            open(filepath)

    def _open_bytes(self, stream):
        try:
            self.pdf_file = fitz.open("pdf", stream)
            self.open = True
            print("OK")
            return True
        except:
            self.open = False
            return None
        
    def _open(self, filepath: str):
        try:
            self.pdf_file = fitz.open(filepath)
            self.open = True
            print("OK")
            return True
        except:
            self.open = False
            return None

    # read a pdf_file and return all text content a List of strings. each string is a page
    def extract_all_text(self) -> List[str]:
        if self.open:
            return [ page.get_text() for page in self.pdf_file ]
        else:
            return None

    # read a pdf_file and return a selected text between init_sep and final_sep over all pdf text
    def extract_related_text(self, init_sep: str="", final_sep: str="", input_text: str="") -> str:
        if self.open:
            if input_text == "":
                content = "\n".join([ page.get_text() for page in self.pdf_file ])
            else:
                content = input_text
            
            def init_cut(string:str, delimiter: str):
                splitted = re.split(delimiter, string, maxsplit=1, flags=re.I)
                if len(splitted) > 1:
                    return delimiter + splitted[-1]
                else: return "Delimiter not found."

            def final_cut(string:str ,delimiter: str):
                splitted = re.split(delimiter, string, maxsplit=1, flags=re.I)
                if len(splitted) > 1:
                    return splitted[0] + delimiter
                else: return "Delimiter not found."

            if init_sep != "":
                content = init_cut(content, init_sep)
            if final_sep != "":
                content = final_cut(content, final_sep)

            #print(content)
            return content
        

        else:
            return None

    # read a pdf_file and return the text content from a specific page
    def extract_page_text(self, page_id: int) -> str:
        if self.open:
            try:
                page_text = self.pdf_file[page_id].get_text()
                return page_text
            except:
                pass;
        else: return None;

    # read a pdf_file and return all figures inside the pdf_file as a List of figures
    def extract_all_figures(self):
        if self.open:
            figures = []
            for idx, page in enumerate(self.pdf_file):
                for img_ref in page.get_images():
                    img_obj = self.pdf_file.extract_image(img_ref[0])
                    ext = img_obj["ext"]
                    img_bytes = img_obj["image"]
                    img_stream = io.BytesIO(img_bytes)
                    img = Image.open(img_stream)
                    figures.append(img)
            return figures                  
        else: return None;

    # read a pdf_file and return all figures inside a specific page from the pdf_file
    def extract_page_figures(self, page_id: int):
        if self.open:
            figures = []
            try:
                for img_ref in self.pdf_file[page_id].get_images():
                    img_obj = self.pdf_file.extract_image(img_ref[0])
                    ext = img_obj["ext"]
                    img_bytes = img_obj["image"]
                    img_stream = io.BytesIO(img_bytes)
                    img = Image.open(img_stream)
                    figures.append(img)
            except:
                pass
            return figures
        else: return None;

    # read a pdf_file and return all rendered pages of the pdf_file as images
    def extract_all_as_image(self):
        if self.open:
            images = []
            for page in self.pdf_file:
                image_matrix = fitz.Matrix(fitz.Identity)

                # pdf image scale. 2 means 2x bigger (width, height) 
                #   than original pdf size
                image_matrix.preScale(2, 2)
                pix = page.getPixmap(alpha = False, matrix = image_matrix)

                img = Image.frombytes("RGB", [pix.width, pix.height],
                        pix.samples)

                images.append(img)
            return images
        else: return None;

    # read a pdf_file and return the rendered image from a specific page
    def extract_page_as_image(self, page_id: int):
        if self.open:
            try:
                page = self.pdf_file[page_id]
                image_matrix = fitz.Matrix(fitz.Identity)
                # pdf image scale. 2 means 2x bigger (width, height) 
                #   than original pdf size
                image_matrix.preScale(2, 2)
                pix = page.getPixmap(alpha = False, matrix = image_matrix)

                img = Image.frombytes("RGB", [pix.width, pix.height],
                        pix.samples)
                return img

            except:
                pass
        else: return None;

def read_file(datapath: str,
    extract: Optional[str]="text",
    text_filter_begin: Optional[str]="",
    text_filter_end: Optional[str]="",
    initial_page: Optional[int]=0,
    final_page: Optional[int]=-1
    ):

    pdf_extractor = PDFExtractor()

    # se nao conseguir abrir o arquivo, ja retorna a funcao
    if pdf_extractor._open(datapath) == None: 
        return None;

    if extract == "text":
        raw_text = pdf_extractor.extract_all_text()
        try:
            text = "\n".join(raw_text[initial_page:final_page] + [raw_text[final_page]])
        except:
            text = "\n".join(raw_text)

        if text_filter_begin != "" or text_filter_end != "":
            text = pdf_extractor.extract_related_text(text_filter_begin, text_filter_end, input_text=text)

        return text

    elif extract == "figures":
        figures = pdf_extractor.extract_all_figures()
        try:
            figures = figures[initial_page:final_page] + [figures[final_page]]
        except:
            pass
        return figures

    elif extract == "prints":
        images = pdf_extractor.extract_all_as_image()
        try:
            images = images[initial_page:final_page] + [images[final_page]]
        except:
            pass
        return images

    else:
        return None
    
def read_memory(stream,
    extract: Optional[str]="text",
    text_filter_begin: Optional[str]="",
    text_filter_end: Optional[str]="",
    initial_page: Optional[int]=0,
    final_page: Optional[int]=-1
    ):

    pdf_extractor = PDFExtractor()

    # se nao conseguir abrir o arquivo, ja retorna a funcao
    if pdf_extractor._open_bytes(stream) == None: 
        return None;

    if extract == "text":
        raw_text = pdf_extractor.extract_all_text()
        try:
            text = "\n".join(raw_text[initial_page:final_page] + [raw_text[final_page]])
        except:
            text = "\n".join(raw_text)

        if text_filter_begin != "" or text_filter_end != "":
            text = pdf_extractor.extract_related_text(text_filter_begin, text_filter_end, input_text=text)

        return text

    elif extract == "figures":
        figures = pdf_extractor.extract_all_figures()
        try:
            figures = figures[initial_page:final_page] + [figures[final_page]]
        except:
            pass
        return figures

    elif extract == "prints":
        images = pdf_extractor.extract_all_as_image()
        try:
            images = images[initial_page:final_page] + [images[final_page]]
        except:
            pass
        return images

    else:
        return None



def read_dir(datapath: str,
    extract: Optional[str]="text",
    text_filter_begin: Optional[str]="",
    text_filter_end: Optional[str]="",
    initial_page: Optional[int]=0,
    final_page: Optional[int]=-1
    ):

    filenames = []
    contents = []

    for idx, filename in enumerate(os.listdir(datapath)):
        print("extracting " + filename + "...", end="")
        content = read_file(datapath + filename, 
                extract,
                text_filter_begin,
                text_filter_end,
                initial_page,
                final_page)
        if content == None: continue;
        else:
            filenames.append(filename)
            contents.append(content)

    if extract == "text":
        df = pd.DataFrame({"filename": filenames, "text": contents})
        return df;

    elif extract == "figures" or extract == "prints":
        return contents



if __name__ == "__main__":
    pass;
    
