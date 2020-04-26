import dash_bootstrap_components as dbc


def navbar():
    nav = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Find Your Match", href="/")),
            dbc.NavItem(dbc.NavLink("How It Works", href="/about")),
            dbc.NavItem(dbc.NavLink("Contribute", href="/survey")),
            dbc.NavItem(dbc.NavLink("Trends", href="/trends"))
        ],
        brand="Compatible",
        color="primary",
        dark=True,
        fluid = True
    )
    return nav
