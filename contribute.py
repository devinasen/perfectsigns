import nav
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from nav import navbar
from footer import footer


header = html.Div([
  dbc.Row([
    dbc.Col([
        dbc.Card(
            dbc.CardBody([
              html.H1('Help train our algorithm!', className = "card-title"),
              html.P("Whether you're happily in love or gladly single, we want to hear your story!", className="card-text"),
              html.P("Fill out this 5 minute survey about your current or past relationships, then head over to our Trends page and see how you compare to the rest of our responders.", className="card-text"),
              dbc.Button("Survey", id = 'survey_link', size="lg", color = 'primary', className="mr-1",
                  external_link = True, href = "https://drive.google.com/open?id=1gz70dyN4AX6n8BMfkiLoM5tFzztpDLQlPNNCvFcAtdY")
                  ]),
            color = "secondary",
            inverse = True
        ),],
        width = {'size': 8, 'offset': 2}
    ),
  ]),
])




def contribute():
  layout = html.Div([
    navbar(),
    html.Br(),
    html.Br(),
    html.Br(),
    header,
    html.Br(),
    footer(),
  ])
  return layout
