# app.py
import dash
from dash import html, dcc
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

def linear_model(x, m, b):
    return m * x + b

app.layout = html.Div([
    html.H1("Linear Model Visualization"),

    html.Div([
        html.Label("Ratio of New Life Policies per New Households (M):"),
        dcc.Slider(
            id='slope-slider',
            min=0, max=1, step=0.01, value=0.1,
            marks={i: str(i) for i in np.arange(0, 1.1, 0.1)},
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ]),

    # We will add more components here later
])

app.layout = html.Div([
    html.H1("Linear Model Visualization"),
    # We'll add components here in the next steps
])

if __name__ == '__main__':
    app.run_server(debug=True)
