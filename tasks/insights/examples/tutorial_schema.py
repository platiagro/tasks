"""
Schema é um sistema bem parecido com json que vai ter a capacidade de gerar o relatório. 
A ideia é que schemas representem seções ou subseções de texto do relatório. 
Hoje é possível adicionar figuras plotly, matplotlib, dataframes pandas e textos planos
A única dificuldade hoje é escrever referências, bem complicado para falar a verdade. 
Mas de resto é simples e prático.
"""

# Importamos a classe Report
from insights.report_generator.report import Report

import plotly.express as px
import numpy as np
import pandas as pd

# Definimos ele com um título
report = Report('Exemplo Schema')

# A partir de agora podemos usar os schemas.
# O schema base está abaixo, adicionamos informações neles na lista information
# A ideia é que ele vai adicionar seguindo a ordem da lista e as informações contidas ali.abs(x)
schema = {'section_title': 'Análise de Cluster', 'information': []}

# Normalmente eu faço assim para adicionar um texto
schema['information'].append(
    {
        'type': 'text',
        'info': 'Um texto de exemplo'
    }
)

# Para uma figura plotly
x = np.arange(1, 10)
y = np.arange(1, 10)

figure = px.scatter(x, y)
schema['information'].append(
    {
        'type': 'figure',
        'caption': 'um teste',
        'figure': figure,
        'package': 'plotly'
    }
)

# Para um dataframe pandas
x = np.arange(1, 10)
y = np.arange(1, 10)
pd_dict = {'x': x, 'y': y}

df = pd.DataFrame.from_dict(pd_dict)

schema['information'].append(
    {
        'type': 'table',
        'caption': 'um teste',
        'table': df,
    }
)

# Podemos também adicionar subseções
# A ideia é que ela segue o mesmo padrão do schema superior, mas é adicionada como informação no schema principal que ela pertence
subschema = {'section_title': 'Teste de Subseção', 'information': []}

subschema['information'].append(
    {
        'type': 'text',
        'info': 'A subseção sendo testada'
    }
    )

# Finalizando a subseção adiciono ela na seção principal
schema['information'].append(
    {
        'type': 'subsection',
        'schema': subschema,
    }
)

# Depois que finalizo a seção posso adicionar ela como seção no documento
report.add_section(schema)

# Fecho e salvo o documento
report.process()
