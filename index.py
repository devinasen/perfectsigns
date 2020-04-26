import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from trends import trends, graph
from product import product, result

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/trends':
        return trends()
    return product()

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

if __name__ == '__main__':
    app.run_server(debug = True)
