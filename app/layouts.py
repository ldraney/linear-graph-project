from dash import html, dcc

layout = html.Div([
    html.H1("Life Insurance Policies Visualization"),
    html.P("Use the sliders to adjust the model parameters."),
    
    dcc.Slider(
        id='slope-slider',
        min=0, max=1, step=0.01, value=0.1,
        marks={i: str(i) for i in range(0, 11)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    
    dcc.Slider(
        id='intercept-slider',
        min=0, max=100, step=1, value=0,
        marks={i: str(i) for i in range(0, 101, 10)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    
    dcc.Graph(id='linear-plot')
    
    html.H2('Understanding the Impact of Your Efforts'),
    html.P('This interactive tool illustrates how different engagement strategies can '
           'impact policy sales. Adjust the sliders to see how increasing outreach (X) '
           'and improving conversion efficiency (M) can lead to more life policies sold (Y).'),
    
    # ... ( add more of your layout here) ...
])

