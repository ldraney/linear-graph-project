# app.py
import dash
from dash import html, dcc
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output  # Import Input and Output

app = dash.Dash(__name__)

def linear_model(x, m, b):
    return m * x + b

@app.callback(
    Output('linear-plot', 'figure'),
    [Input('slope-slider', 'value'),
     Input('intercept-slider', 'value')]
)
def update_graph(slope, intercept):
    x = np.linspace(0, 1000, 500)
    y = linear_model(x, slope, intercept)
    return {
        'data': [go.Scatter(x=x, y=y, mode='lines')],
        'layout': go.Layout(title='Linear Model', xaxis={'title': 'X'}, yaxis={'title': 'Y'})
    }

app.layout = html.Div([
    html.H1("Linear Model Visualization"),

    # Slope (M) Slider
    html.Div([
        html.Label("Ratio of New Life Policies per New Households (M):"),
        dcc.Slider(
            id='slope-slider',
            min=0, max=1, step=0.01, value=0.1,
            marks={i: str(i) for i in np.arange(0, 1.1, 0.1)},
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ]),

    # Y-Intercept (B) Slider
    html.Div([
        html.Label("Y-Intercept (Life Policies Sold to Existing Households and Policy Owners) (B):"),
        dcc.Slider(
            id='intercept-slider',
            min=0, max=100, step=1, value=0,
            marks={i: str(i) for i in range(0, 101, 10)},
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ]),

    # Placeholder for Graph
    dcc.Graph(id='linear-plot')
])

if __name__ == '__main__':
    app.run_server(debug=True)
