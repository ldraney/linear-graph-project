# ... (other necessary imports) ...
from dash import Dash, html, dcc, Input, Output, State
import plotly.graph_objs as go

app = Dash(__name__)

server = app.server

app.layout = html.Div(
    [
        html.H1("Policy Sales Visualization Tool"),
        dcc.Markdown(
            """
        **Adjust the sliders to see how outreach, conversion efficiency, and existing policies impact policy sales.**
        - **X (New Households)**: Represents the number of new households agents engage with.
        - **M (Conversion Efficiency)**: Represents the ratio of new life policies per new household.
        - **B1 (Previous Customer Households)**: Life policies sold to previous customer households without current life policies.
        - **B2 (Additional Coverage and Renewals)**: Additional life policies sold to customers who already have at least one life policy.
    """
        ),
        html.Div(
            [
                html.P("New Households (X):"),
                dcc.Slider(
                    id="x-slider",
                    min=0,
                    max=825,
                    value=50,
                    step=1,
                    marks={i: str(i) for i in range(0, 851, 75)},
                ),
                dcc.Input(id="x-input", type="number", value=50, min=0, max=825),
            ]
        ),
        html.Div(
            [
                html.P("Conversion Efficiency (M):"),
                dcc.Slider(
                    id="m-slider",
                    min=0,
                    max=1,
                    value=0.5,
                    step=0.01,
                    marks={i / 10: str(i / 10) for i in range(0, 11)},
                ),
                dcc.Input(
                    id="m-input", type="number", value=0.5, min=0, max=1, step=0.01
                ),
            ]
        ),
        html.Div(
            [
                html.P("Previous Customer Households (B1):"),
                dcc.Slider(
                    id="b1-slider",
                    min=0,
                    max=350,
                    value=10,
                    step=1,
                    marks={i: str(i) for i in range(0, 351, 35)},
                ),
                dcc.Input(id="b1-input", type="number", value=100, min=0, max=351),
            ]
        ),
        html.Div(
            [
                html.P("Additional Coverage and Renewals (B2):"),
                dcc.Slider(
                    id="b2-slider",
                    min=0,
                    max=350,
                    value=5,
                    step=1,
                    marks={i: str(i) for i in range(0, 351, 35)},
                ),
                dcc.Input(id="b2-input", type="number", value=100, min=0, max=351),
            ]
        ),
        dcc.Graph(id="policy-graph"),
        # ... (additional elements and styling) ...
    ],
    style={"backgroundColor": "#F9F9F9", "padding": "10px", "fontSize": "18px"},
)


# Callbacks to sync sliders and input boxes
@app.callback(
    Output("x-slider", "value"),
    [Input("x-input", "value")],
    [State("x-slider", "value")],
)
def update_x_slider(input_val, slider_val):
    # When input box is used, update the slider
    return input_val if input_val is not None else slider_val


# Callback for 'Conversion Efficiency (M)' slider and input box
@app.callback(
    Output("m-slider", "value"),
    [Input("m-input", "value")],
    [State("m-slider", "value")],
)
def update_m_slider(input_val, slider_val):
    return input_val if input_val is not None else slider_val


# Callback for 'Previous Customer Households (B1)' slider and input box
@app.callback(
    Output("b1-slider", "value"),
    [Input("b1-input", "value")],
    [State("b1-slider", "value")],
)
def update_b1_slider(input_val, slider_val):
    return input_val if input_val is not None else slider_val


# Callback for 'Additional Coverage and Renewals (B2)' slider and input box
@app.callback(
    Output("b2-slider", "value"),
    [Input("b2-input", "value")],
    [State("b2-slider", "value")],
)
def update_b2_slider(input_val, slider_val):
    return input_val if input_val is not None else slider_val


# Callback to update the input box when the 'X' slider changes
@app.callback(
    Output("x-input", "value"),
    [Input("x-slider", "value")],
)
def update_x_input(slider_val):
    return slider_val


# Callback to update the input box when the 'M' slider changes
@app.callback(
    Output("m-input", "value"),
    [Input("m-slider", "value")],
)
def update_m_input(slider_val):
    return slider_val


# Callback to update the input box when the 'B1' slider changes
@app.callback(
    Output("b1-input", "value"),
    [Input("b1-slider", "value")],
)
def update_b1_input(slider_val):
    return slider_val


# Callback to update the input box when the 'B2' slider changes
@app.callback(
    Output("b2-input", "value"),
    [Input("b2-slider", "value")],
)
def update_b2_input(slider_val):
    return slider_val


# Callback to update graph based on slider or input values
@app.callback(
    Output("policy-graph", "figure"),
    [
        Input("x-slider", "value"),
        Input("m-slider", "value"),
        Input("b1-slider", "value"),
        Input("b2-slider", "value"),
        # Add inputs as dependencies too
        Input("x-input", "value"),
        Input("m-input", "value"),
        Input("b1-input", "value"),
        Input("b2-input", "value"),
    ],
)
def update_graph(
    x_value, m_value, b1_value, b2_value, x_input, m_input, b1_input, b2_input
):
    # Use the most recent values from either the slider or input box
    x_value = x_input if x_input is not None else x_slider
    m_value = m_input if m_input is not None else m_slider
    b1_value = b1_input if b1_input is not None else b1_slider
    b2_value = b2_input if b2_input is not None else b2_slider

    total_b = b1_value + b2_value  # Calculate total B as the sum of B1 and B2
    y_values = [m_value * x + total_b for x in range(x_value + 1)]
    figure = go.Figure(
        data=go.Scatter(
            x=list(range(x_value + 1)),
            y=y_values,
            mode="lines",
            line=dict(width=10, color="blue"),
        )
    )
    figure.update_layout(
        title="Impact of Outreach, Efficiency, and Existing Policies on Policy Sales",
        xaxis_title="New Households (X)",
        yaxis_title="Life Policies Sold (Y)",
    )
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run(debug=True, host='0.0.0.0', port='8050')
