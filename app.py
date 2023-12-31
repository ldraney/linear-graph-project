import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("y = mx + b"),
        dcc.Input(id="m-value", type="number", value=1, step=0.1),
        dcc.Input(id="b-value", type="number", value=0, step=0.1),
        dcc.Graph(id="line-graph"),
    ]
)


# Define the callback to update the graph
@app.callback(
    Output("line-graph", "figure"),
    [Input("m-value", "value"), Input("b-value", "value")],
)
def update_graph(m, b):
    # Create an array of x values
    x_values = np.linspace(-10, 10, 100)

    # Calculate y values based on the linear equation
    y_values = m * x_values + b

    # Create a plotly graph object
    figure = {
        "data": [go.Scatter(x=x_values, y=y_values, mode="lines")],
        "layout": go.Layout(
            title="Linear Graph of y=mx+b",
            xaxis={"title": "x"},
            yaxis={"title": "y"},
        ),
    }
    return figure


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
