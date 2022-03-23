import plotly.express as px

from insights.clustering.utils import confusion_matrix


class Plotter():
    def __init__(self, dimensions=3, target_variable=None): 
        
        possible_dimensions = [
            2, 
            3
        ]
        
        if dimensions not in possible_dimensions: 
            raise ValueError(f'Dimensions {dimensions} not valid')
        
        self.dimensions = dimensions
        self.plot_function = px.scatter_3d if self.dimensions  == 3 else px.scatter
        self.target_variable = target_variable
        
    def plot(self, df_cluster, samples, title): 
        figures = []
        for sample in samples:
            if self.dimensions == 3: 
                self.config = {
                    'x': sample['labels'][0],
                    'y': sample['labels'][1],
                    'z': sample['labels'][2],
                    'color': [str(sample) for sample in sample['y_pred']],
                }
                size=3
                
            elif self.dimensions == 2: 
                self.config = {
                    'x': sample['labels'][0],
                    'y': sample['labels'][1],
                    'color': [str(sample) for sample in sample['y_pred']],
                }
                size=6
            
            fig = self.plot_function(df_cluster, **self.config)
            
            fig.update_traces(marker=dict(size=size))
            
            fig.update_layout(
                coloraxis_colorbar=dict(yanchor="top", y=1, x=0,
                                                ticks="outside"),
                title_text=title,
                title_x=0.5,
            )
            figures.append(fig)
        return figures
    
    def plot_conf(self, df, samples, title):
        if self.target_variable is None:
            raise ValueError('Target Variable is not set.')
        
        figures = []
        confusion_matrixes = []
        for sample in samples:
            y_true = df[self.target_variable]
            cf = confusion_matrix(y_true, sample['y_pred'])
            fig = px.imshow(cf, title=title + ": [" + " x ".join(sample['labels']) + "]")
            fig.update_layout(
                coloraxis_colorbar=dict(yanchor="top", y=1, x=0,
                                                ticks="outside"),
                title_text=title,
                title_x=0.5,
            )
            figures.append(fig)
            confusion_matrixes.append(cf)
        
        return figures, confusion_matrixes