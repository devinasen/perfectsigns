'''This is our control center from which we process all user input and call other pages.
The application is run from this file. Many callback methods are adapted from dash_bootstrap_components documentation.
App structure from https://towardsdatascience.com/create-a-multipage-dash-application-eceac464de91.'''

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from trends import trends, graph
from product import product, result
from contribute import contribute
from about import about


#initializing
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

#Which page to display
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/trends':
        return trends()
    if pathname == "/survey":
        return contribute()
    if pathname == "/about":
        return about()
    return product()

#takes in survey input and returns output from result method in product.py
@app.callback([Output('result', 'children'),
    Output('error', 'children')],

    [Input('user-survey', 'n_clicks')],

    [State('name', 'value'),
    State('q1', 'value'),
    State('q2', 'value'),
    State('q3', 'value'),
    State('q4', 'value'),
    State('q5', 'value'),
    State('q6', 'value'),
    State('q7', 'value'),
    State('q8', 'value'),
    State('q9', 'value'),
    ]
)
def update_result(click, n, q1, q2, q3, q4, q5, q6, q7, q8, q9):
    if click is None:
        raise PreventUpdate

    if (q1 or q2 or q3 or q4 or q5 or q6 or q7) is None:
        return dash.no_update, 'Whoops! Seems like you missed a question'

    if n is None:
        n = 'there'

    return result(n, q1, q2, q3, q4, q5, q6, q7, q8, q9)

#takes user input of graphbuilder section and returns graph using method in trends.py
@app.callback(
    Output('graph_output', 'figure'), [
    Input('zodiac-1', 'value'),
    Input('zodiac-2', 'value'),
    Input('x', 'value'),
    Input('y', 'value'),
    Input('size', 'value'),
    Input('color', 'value')
    ]
)
def update_graph(z1, z2, z3, z4, z5, z6):
    if (z1 is None or z2 is None or z3 is None or z4 is None or z5 is None or z6 is None):
        raise PreventUpdate
    return graph(z1, z2, z3, z4, z5, z6)

#opens and closes creator cards in about.py
@app.callback(
    Output("collapse-1", "is_open"),
    [Input("creators-button", "n_clicks")],
    [State("collapse-1", "is_open")],
)
def toggle_collapse1(n, is_open):
    if n:
        return not is_open
    return is_open

#opens and closes algorthim explanation card in about.py
@app.callback(
    Output("collapse-2", "is_open"),
    [Input("algorithm-button", "n_clicks")],
    [State("collapse-2", "is_open")],
)
def toggle_collapse2(n, is_open):
    if n:
        return not is_open
    return is_open

#run the app - Whoooooo!
if __name__ == '__main__':
    app.run_server(debug = True)
