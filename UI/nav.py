#navigation

import dash_bootstrap_components as dbc

#Creating navigation bar for each webpage
#Method from dash_bootstrap_components documentation
def navbar():
    nav = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Find Your Match", href="/")),
            dbc.NavItem(dbc.NavLink("How It Works", href="/about")),
            dbc.NavItem(dbc.NavLink("Contribute", href="/survey")),
            dbc.NavItem(dbc.NavLink("Trends", href="/trends"))
        ],
        brand="Perfect Signs",
        color="primary",
        dark=True,
        fluid = True
    )
    return nav
