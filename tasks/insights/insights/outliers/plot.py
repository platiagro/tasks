import plotly.express as px

def plot(df, y_pred, dimensions=3, title=None):  
    if dimensions == 3: 
        config = {
            'x': df.columns[0],
            'y': df.columns[1],
            'z': df.columns[2],
            'color': [str(sample) for sample in y_pred],
        }
        plot_function = px.scatter_3d
        size=3
                
    elif dimensions == 2: 
        config = {
            'x': df.columns[0],
            'y': df.columns[1],
            'color': [str(sample) for sample in y_pred],
        }
        plot_function = px.scatter
        size=6
    
    fig = plot_function(df, **config)
    fig.update_traces(marker=dict(size=size))
    
    if dimensions == 3:
        fig.update_layout(
            height=800,
            width=1000,
            coloraxis_colorbar=dict(yanchor="top", y=1, x=0,
                                            ticks="outside"),
            scene= dict(
                aspectratio= dict(
                            x= 0.85,
                            y= 0.85,
                            z= 1.3
                            )),
            title_text=title,
            title_x=0.5,
            showlegend=False
        )
    else:
        fig.update_layout(
            coloraxis_colorbar=dict(yanchor="top", y=1, x=0,
                                            ticks="outside"),
            title_text=title,
            title_x=0.5,
            showlegend=False
        )
        
    return fig
    