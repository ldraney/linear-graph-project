# linear-plot-app/app.py

import dash
from dash import html
from linear_plot_app import callbacks  # This will import your callback functions
from linear_plot_app import layouts  # This will import your app layout

app = dash.Dash(__name__)

app.layout = layouts.layout  # Set the layout of the app

# Include the server variable for deployment purposes
# Please see https://dash.plotly.com/deployment
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)

