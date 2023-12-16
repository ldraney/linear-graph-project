# app.py
import dash
from dash import html, dcc, Input, Output
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

# Linear model function
def linear_model(x, m, b):
    return m * x + b

app.layout = html.Div([
    html.H1("Linear Model Visualization"),

    dcc.Slider(
        id='slope-slider',
        min=0,
        max=1,
        step=0.01,
        value=0.1,
        marks={i: f'{i}' for i in np.arange(0, 1.1, 0.1)},
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    html.Div(id='slope-value'),

    # Additional sliders for B, X range, Y range will go here

    dcc.Graph(id='linear-plot')
])

@app.callback(
    Output('slope-value', 'children'),
    Output('linear-plot', 'figure'),
    Input('slope-slider', 'value'),
    # Additional inputs for other sliders will go here
)
def update_graph(slope):
    x = np.linspace(0, 1000, 500)
    y = linear_model(x, slope, 0)  # B and other parameters to be dynamic

    return f'Slope: {slope}', {
        'data': [go.Scatter(x=x, y=y, mode='lines')],
        'layout': go.Layout(title='Linear Model', xaxis={'title': 'X'}, yaxis={'title': 'Y'})
    }

if __name__ == '__main__':
    app.run_server(debug=True)

