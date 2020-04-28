import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate


jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.P(
                    "Have any feedback for us? Let us know by contacting devinasen@berkeley.edu.",
                    className="lead",
                ),
                html.P("A Varshinaastha Creation.")
            ],
            fluid=True,
        )
    ],
    fluid=True,
)


def footer():
  layout = html.Div([
      html.Br(),
      jumbotron,
      html.Br()
    ])
  return layout
