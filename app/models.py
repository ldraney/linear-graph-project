# linear-plot-app/models.py

import numpy as np
import plotly.graph_objs as go

def get_x_values():
    return np.linspace(0, 1000, 500)  # Replace with dynamic range if needed

def calculate_y(x, m, b):
    return m * x + b  # The linear model equation

def create_figure(x, y):
    return {
        'data': [go.Scatter(x=x, y=y, mode='lines')],
        'layout': go.Layout(title='Linear Model', xaxis={'title': 'X'}, yaxis={'title': 'Y'})
    }

