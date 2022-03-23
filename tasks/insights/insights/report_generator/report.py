#!/usr/bin/python
"""
This example shows matplotlib functionality.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

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
        
        geometry_options = {"right": "2cm", "left": "2cm"}
        self.doc = Document(title, geometry_options=geometry_options)
        self.doc.packages.append(Package('babel', options=['portuguese']))
        self.doc.packages.append(Package('placeins'))
        self.doc.packages.append(Package('booktabs'))
        self.doc.preamble.append(Command('title', title))
        self.doc.preamble.append(Command('date', NoEscape(r'\today')))
        self.doc.append(NoEscape(r'\maketitle'))
        self.doc.append(NoEscape(r'\clearpage'))
        self.doc.append(NoEscape(r'\tableofcontents'))
        self.doc.append(NoEscape(r'\listoffigures'))
        self.doc.append(NoEscape(r'\listoftables'))
        self.doc.append(NoEscape(r'\clearpage'))
    
    
    def create_figure(self, information):
        figure = information['figure']
        figure = self.process_plotly(figure) if information['package'] == 'plotly' else self.process_matplotlib(figure)
        with self.doc.create(Figure(position=None)) as plot:
            width = information['width'] if 'width' in information else r'0.5\textwidth'
            plot.add_image(figure, width=NoEscape(width))
            plot.add_caption(information['caption'])
            if 'label' in information:
                plot.append(Label(NoEscape(information['label'])))
            
    
    def create_table(self, information):
        df = information['table']
        with self.doc.create(Table(position='htbp')) as table:
            table.add_caption(information['caption'])
            table.append(Command('centering'))
            alignment = None
            float_fmt = information['float_fmt'] if 'float_fmt' in information else None
            table.append(NoEscape(df.to_latex(escape=True, column_format='c'*(len(df.columns) + 1), float_format=float_fmt)))
            if 'label' in information:
                table.append(Label(NoEscape(information['label'])))
        
    def add_section(self, schema):
        self.doc.append(NoEscape(r'\clearpage'))
        with self.doc.create(Section(schema['section_title'])):
            for information in schema['information']:
                if information['type'] == 'text':
                    self.doc.append(information['info'])
                    self.doc.append(NewLine())
                    
                elif information['type'] == 'figure':
                    self.create_figure(information)
                        
                elif information['type'] == 'table':
                    self.create_table(information)
                        
                elif information['type'] == 'subsection':
                    self.add_subsection(information['schema'])
            
        self.doc.append(NoEscape(r'\FloatBarrier'))   

    def add_subsection(self, schema):
        with self.doc.create(Subsection(schema['section_title'])):

            for information in schema['information']:
                if information['type'] == 'text':
                    self.doc.append(information['info'])
                    self.doc.append(NewLine())
                    
                elif information['type'] == 'figure':
                    self.create_figure(information)
                
                elif information['type'] == 'table':
                    self.create_table(information)

    def get_path(self):
        name = str(uuid.uuid4()) + '.png'
        path = pathlib.Path('./insights/report_generator/latex_figures') / name
        path.parents[0].mkdir(parents=True, exist_ok=True)
        path = str(path)
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
        self.doc.generate_pdf(clean_tex=False)
    
    
    
    
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
    report.add_section(
        section_title='Teste', 
        text='testando '*50, 
        figure=fig_path, 
        figure_caption='testando o teste')
    report.process()