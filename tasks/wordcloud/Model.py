from wordcloud import WordCloud
import pandas as pd
import numpy as np
import joblib
import io
from io import StringIO

class Model:
    def __init__(self):
        self.loaded = False

    def load(self):
        # utilize esta função para carregar e inicializar modelos
        artifacts = joblib.load("/tmp/data/wordcloud.joblib")
        self.wordcloud_parameters = artifacts["wordcloud_parameters"]

        background_color = self.wordcloud_parameters["background_color"]
        max_words = self.wordcloud_parameters["max_words"]
        stopwords = self.wordcloud_parameters["stopwords"]
        max_font_size = self.wordcloud_parameters["max_font_size"]
        width = self.wordcloud_parameters["width"]
        height = self.wordcloud_parameters["height"]

        self.wc = WordCloud(background_color = background_color,
            max_words = max_words,
            stopwords = stopwords,
            max_font_size = max_font_size,
            width = width,
            height = height)

        self.loaded = True
        print("Loaded model")

    def predict(self, X, feature_names, meta=None):
        if not self.loaded:
            self.load()
        
        input_data = X
        images = []
        
        if isinstance(X, bytes):
            string = str(X, 'utf-8')
            data = StringIO(string)
            try:
                input_data = pd.read_csv(data)
            except OSError:
                input_data = string

        elif isinstance(X, dict):
            input_data = X['strData']
            
        if type(input_data) == str:
            self.wc.generate(input_data)
            images.append(self.wc.to_image())
        
        elif type(input_data) == pd.DataFrame:
            print('cuuuuuuuuuuu')
            print(input_data["text"])
            print('cuuuu')
            for text in input_data["text"]:
                self.wc.generate(text)
                images.append(self.wc.to_image())

        result = []
        for img in images:
            buff = io.BytesIO()
            img.save(buff, format="JPEG")
            result.append(buff.getvalue().decode("latin1"))
             
        # a função predict recebe um parâmetro X (numpy array, str ou bytes)
        # e deve retornar o resultado da tarefa (numpy array, list, str ou bytes)
        return result
