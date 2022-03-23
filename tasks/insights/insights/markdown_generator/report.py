import markdown
import markdown2
import shutil 

import plotly.express as px
import numpy as np
import pandas as pd

# begin-doc-include
import matplotlib
import pathlib
import uuid 
import plotly.io as pio

from pylatex import Document, Section, Figure, NoEscape, Command, Package, Subsection, StandAloneGraphic, Center, NewLine, Table, Label, Ref
from pylatex.utils import escape_latex

matplotlib.use('Agg')  # Not to use X server. For TravisCI.
import matplotlib.pyplot as plt  # noqa



class Report():
    def __init__(self, title):
        self.html = ''
        self.add_line(f'#{title}\n\n')
        # Clear figures folder
        self.path = pathlib.Path('./insights/markdown_generator/'+title.replace(' ', '')+'/figures')
        self.path.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(str(self.path))
        
    
    def create_figure(self, information):
        figure = information['figure']
        figure = self.process_plotly(figure) if information['package'] == 'plotly' else self.process_matplotlib(figure)
        figure_str = f'![{information["caption"]}]({figure})\n\n*{information["caption"]}*'
        self.add_line(figure_str)
        
    def create_table(self, information):
        df = information['table']
        markdown_table = df.to_markdown()
        self.html += markdown.markdown(markdown_table, extensions=['tables'])
        self.add_line(f'*{information["caption"]}*')
    
    def add_line(self, paragraph):
        self.html += markdown2.markdown(paragraph)
            
    def add_section(self, schema):
        title = schema['section_title']
        self.add_line(f'##{title}')
        self.add_information(schema['information'])
        
    def add_subsection(self, schema):
        title = schema['section_title']
        self.add_line(f'###{title}')
        self.add_information(schema['information'])
    
    
    def add_information(self, informations):
        for information in informations:                
            if information['type'] == 'text':
                self.add_line(information['info'])
                
            elif information['type'] == 'figure':
                self.create_figure(information)
                    
            elif information['type'] == 'table':
                self.create_table(information)
                    
            elif information['type'] == 'subsection':
                self.add_subsection(information['schema'])
        

    def get_path(self):
        name = str(uuid.uuid4()) + '.png'
        path = self.path / name
        path.parents[0].mkdir(parents=True, exist_ok=True)
        path = str(path)
        print(path)
        
        return path
    
    def process_table(self, table):
        processed_table = None
        return processed_table
    
    def process_plotly(self, figure):
        path = self.get_path()
        pio.write_image(figure, path)
        return path
    
    def process_matplotlib(self, figure):
        path = self.get_path()
        figure.save_fig(path)
        return path       
    
    def process(self):
        html = self.html
        with open('test.md', 'w') as f:
            f.write(html)

    
    
    
    
def main(fname, width, *args, **kwargs):
    geometry_options = {"right": "2cm", "left": "2cm"}
    doc = Document(fname, geometry_options=geometry_options)

    doc.append('Introduction.')

    with doc.create(Section('I am a section')):
        doc.append('Take a look at this beautiful plot:')

        with doc.create(Figure(position='htbp')) as plot:
            plot.add_plot(width=NoEscape(width), *args, **kwargs)
            plot.add_caption('I am a caption.')

        doc.append('Created using matplotlib.')

    doc.append('Conclusion.')

    doc.generate_pdf(clean_tex=False)


if __name__ == '__main__':
    fig_path='teste.jpeg'
    report = Report('Relatório AutoML CPQD')
    
    schema = {'section_title': 'Análise de Cluster', 'information': []}
        
    schema['information'].append(dict(
        type='text', 
        info='testando '*50))
    
    schema['information'].append(
        dict(
        type='subsection', 
        schema={'section_title': 'Análise de Cluster TESTANDOOOOOOOOOOOO', 'information': []})
        )
    
    schema['information'].append(dict(
        type='text', 
        info='testando '*50))
    
    schema['information'].append(
        dict(
        type='subsection', 
        schema={'section_title': 'Análise de Cluster A', 'information': []})
        )
    
    a = np.arange(10)
    
    figure = px.scatter(a, a)
    
    schema['information'].append(
        dict(
            type='figure',
            caption='testando o caption', 
            figure=figure,
            package='plotly'        
        )
    )
    
    a = np.ones([10, 10])
    df = pd.DataFrame(a)
    
    schema['information'].append(
        dict(
            type='table',
            caption='testando tabela',
            table=df
        )
    )
    
    print(schema)
    report.add_section(schema)
    
    report.process()