import nav
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from nav import navbar
from footer import footer


content = html.Div([
    dbc.Jumbotron([
        html.H1("About Us")
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Button(
                "Creators",
                id="creators-button",
                size = 'lg',
                className="mr-1",
                color="primary",
            )],
            width = {'offset':  5}
        )],
    ),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Collapse(
                    dbc.CardGroup([
                        dbc.Card([
                            dbc.CardBody([
                                html.H3(["Aastha Jha"]),
                                html.P(["UC Berkeley Class of 2020"]),
                                html.P(["Accenture Consulting"]),
                                html.P(["Virgo"])
                            ]),
                            ],
                        color = "primary",
                        outline = True
                        ),
                        dbc.Card([
                            dbc.CardBody([
                                html.H3(["Devina Sen"]),
                                html.P(["UC Berkeley Class of 2020"]),
                                html.P(["Not Accenture"]),
                                html.P(["Virgo"])
                            ]),
                        ],
                        color = 'primary',
                        outline = True
                        ),
                        dbc.Card([
                            dbc.CardBody([
                                html.H3(["Varsha Sundar"]),
                                html.P(["UC Berkeley Class of 2020"]),
                                html.P(["Accenture Digital"]),
                                html.P(["Scorpio"])
                            ]),
                        ],
                        color = 'primary',
                        outline = True
                        )
                    ]),
                    id="collapse-1",
            )
        ], width = 9)
    ], justify = "center"),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Button(
                "Algorithm",
                id="algorithm-button",
                size = 'lg',
                className="mr-1",
                color="primary",
            )
        ], width = {'offset': 5})
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Collapse(
                dbc.Card([
                    dbc.CardBody([
                        html.P("This machine learning model utilizes decision tree classification and performs logistic regression on "
                        "predominantly categorical user submitted data to determine the zodiac sign and preferred "
                        "qualities of a user's ideal match respectively. With more data and frequent testing, we aim to "
                        "redefine astrological pairings for the modern day match seeker and help them "
                        "recognize the Perfect Signs. ")
                    ])
                ], color = "secondary", inverse = True
                ),
                id = "collapse-2"
            )
        ], width = 9)
    ], justify = "center")
])



def about():
    layout = html.Div([
        navbar(),
        html.Br(),
        content,
        html.Br(),
        footer()
    ])
    return layout
