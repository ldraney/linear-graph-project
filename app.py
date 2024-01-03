# ... (other necessary imports) ...
from dash import Dash, html, dcc, Input, Output
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
            ]
        ),
        dcc.Graph(id="policy-graph"),
        # ... (additional elements and styling) ...
    ],
    style={"backgroundColor": "#F9F9F9", "padding": "10px", "fontSize": "18px"},
)


# Define callback to update graph
@app.callback(
    Output("policy-graph", "figure"),
    [
        Input("x-slider", "value"),
        Input("m-slider", "value"),
        Input("b1-slider", "value"),
        Input("b2-slider", "value"),
    ],
)
def update_graph(x_value, m_value, b1_value, b2_value):
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
