from dash.dependencies import Input, Output
from . import models  # This will import your linear model function
from .. import app  # Import the Dash app instance


@app.callback(
    Output("linear-plot", "figure"),
    [Input("slope-slider", "value"), Input("intercept-slider", "value")],
)
def update_graph(slope, intercept):
    x_values = models.get_x_values()  # Get X values from the models.py
    y_values = models.calculate_y(x_values, slope, intercept)  # Calculate Y values
    return models.create_figure(x_values, y_values)  # Create and return the figure
