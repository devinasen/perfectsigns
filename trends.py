import sklearn
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go
from nav import navbar
from footer import footer

df = pd.read_csv('Data Collection Survey (Responses).csv')
og_df = df.copy()

og_df.rename(columns={'Your Zodiac': 'Zodiac',
                   "Your Ex/Partner's Zodiac": "Partner's Zodiac",
                   "Age Range": "Respondent's Age",
                   "Ex/Partner's Age Range": "Partner's Age",
                   "Your Gender?": "Respondent Gender",
                   "Your ex/partner's Gender?": "Partner's Gender",
                   "On a scale from 1-10, how happy were/are you in your relationship?": "Happiness",
                   "On a scale from 1-10, how compatible did/do you feel you both are?": "Compatibility",
                   "Income": "Income",
                   "Are you and your ex/partner the same ethnicity?": "Ethnicity",
                   "Your highest level of education? (Or in progress)": "Respondent's Education",
                   "Your ex/partner's highest level of education? (Or in progress)": "Partner's Education",
                   "Did/do you and your partner generally hold the same political views?": "Political Views",
                   "Did/do you and your partner hold the same religious views?":"Religion",
                   "Preferences (select for you and your ex/partner if yes) [Smoke?]": "Smoking",
                   "Preferences (select for you and your ex/partner if yes) [Drink?]": "Drinking",
                   "Preferences (select for you and your ex/partner if yes) [Drug use?]": "Drug Use",
                   "Preferences (select for you and your ex/partner if yes) [Premarital sex?]": "Premarital Sex",
                   "Preferences (select for you and your ex/partner if yes) [Want to have kids?]": "Wants Kids",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Calm]": "calm",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Rational]": "rational",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Emotional ]": "emotional",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Stubborn]": "stubborn",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Adventurous]": "adventurous",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Creative]": "creative",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Analytical]": "analytical",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Introvert]": "introvert",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Extrovert]": "extrovert",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Like going out]": "going_out",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Like staying in ]": "staying_in",
                   "I am answering about:": "status"

                  }, inplace=True)

df.rename(columns={'Your Zodiac': 'zodiac',
                   "Your Ex/Partner's Zodiac": "p_zodiac",
                   "Age Range": "age",
                   "Ex/Partner's Age Range": "p_age",
                   "Your Gender?": "gender",
                   "Your ex/partner's Gender?": "p_gender",
                   "On a scale from 1-10, how happy were/are you in your relationship?": "happy",
                   "On a scale from 1-10, how compatible did/do you feel you both are?": "compatible",
                   "Income": "income",
                   "Are you and your ex/partner the same ethnicity?": "ethnicity",
                   "Your highest level of education? (Or in progress)": "education",
                   "Your ex/partner's highest level of education? (Or in progress)": "p_education",
                   "Did/do you and your partner generally hold the same political views?": "political",
                   "Did/do you and your partner hold the same religious views?":"religion",
                   "Preferences (select for you and your ex/partner if yes) [Smoke?]": "smoke",
                   "Preferences (select for you and your ex/partner if yes) [Drink?]": "drink",
                   "Preferences (select for you and your ex/partner if yes) [Drug use?]": "drug",
                   "Preferences (select for you and your ex/partner if yes) [Premarital sex?]": "premarital_sex",
                   "Preferences (select for you and your ex/partner if yes) [Want to have kids?]": "kids",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Calm]": "calm",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Rational]": "rational",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Emotional ]": "emotional",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Stubborn]": "stubborn",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Adventurous]": "adventurous",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Creative]": "creative",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Analytical]": "analytical",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Introvert]": "introvert",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Extrovert]": "extrovert",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Like going out]": "going_out",
                   "Select whether each trait pertains to you, your ex/partner, or both of you. Leave blank if neither of you has that trait. [Like staying in ]": "staying_in",
                   "I am answering about:": "status"

                  }, inplace=True)

og_df.replace('', np.nan, inplace=True)
og_df.fillna(0, inplace= True)
og_df.drop(columns=['Timestamp'], axis=0, inplace= True)

df.replace('', np.nan, inplace=True)
df.fillna(0, inplace= True)
df.drop(columns=['Timestamp'], axis=0, inplace= True)

## CREATING OG DF FOR SCATTERPLOT
og_df['Ethnicity'].replace(to_replace={'Yes': "Same", 'No': "Different"}, inplace= True)
og_df['Political Views'].replace(to_replace={'Yes': "Same Views", 'No': "Different Views", "Maybe": "Unsure"}, inplace = True)

pref_r = {'You, Your Partner': "Respondent and their Partner",
          'You': "Respondent Only",
        'Your Partner': "Partner Only", 0: 'Neither'}

og_df['Smoking'].replace(to_replace=pref_r, inplace= True)
og_df['Drinking'].replace(to_replace=pref_r, inplace= True)
og_df['Drug Use'].replace(to_replace=pref_r, inplace= True)
og_df['Premarital Sex'].replace(to_replace=pref_r, inplace= True)
og_df['Wants Kids'].replace(to_replace=pref_r, inplace= True)

og_df['calm'].replace(to_replace=pref_r, inplace= True)
og_df['rational'].replace(to_replace=pref_r, inplace= True)
og_df['emotional'].replace(to_replace=pref_r, inplace= True)
og_df['stubborn'].replace(to_replace=pref_r, inplace= True)
og_df['adventurous'].replace(to_replace=pref_r, inplace= True)
og_df['creative'].replace(to_replace=pref_r, inplace= True)
og_df['analytical'].replace(to_replace=pref_r, inplace= True)
og_df['introvert'].replace(to_replace=pref_r, inplace= True)
og_df['extrovert'].replace(to_replace=pref_r, inplace= True)
og_df['going_out'].replace(to_replace=pref_r, inplace= True)
og_df['staying_in'].replace(to_replace=pref_r, inplace= True)

og_df['Zodiac'].replace(to_replace = {'Scorpio (October 23 - November 21)': 'Scorpio',
    'Cancer (June 21 - July 22)': 'Cancer',
       'Capricorn (December 22 - January 19)': 'Capricorn',
       'Aries (March 21 - April 19)': 'Aries',
       'Aquarius (January 20 - February 18)': 'Aquarius',
       'Sagittarius (November 22 - December 21)': 'Sagittarius',
       'Taurus (April 20 - May 20)': 'Taurus', 'Virgo (August 23 - September 22)': 'Virgo',
       'Leo (July 23 - August 22)': 'Leo', 'Gemini (May 21 - June 20)': 'Gemini',
       'Pisces (February 19 - March 20)': 'Pisces',
       'Libra (September 23 - October 22)': 'Libra'}, inplace = True)
og_df["Partner's Zodiac"].replace(to_replace = {'Scorpio (October 23 - November 21)': 'Scorpio',
    'Cancer (June 21 - July 22)': 'Cancer',
       'Capricorn (December 22 - January 19)': 'Capricorn',
       'Aries (March 21 - April 19)': 'Aries',
       'Aquarius (January 20 - February 18)': 'Aquarius',
       'Sagittarius (November 22 - December 21)': 'Sagittarius',
       'Taurus (April 20 - May 20)': 'Taurus', 'Virgo (August 23 - September 22)': 'Virgo',
       'Leo (July 23 - August 22)': 'Leo', 'Gemini (May 21 - June 20)': 'Gemini',
       'Pisces (February 19 - March 20)': 'Pisces',
       'Libra (September 23 - October 22)': 'Libra'}, inplace = True)

graph_options = ["Respondent's Age", "Partner's Age",
       'Respondent Gender', "Partner's Gender", 'Happiness', 'Compatibility',
       'Income', 'Ethnicity', "Respondent's Education", "Partner's Education",
       'Political Views', 'Religion', 'Smoking', 'Drinking', 'Drug Use',
       'Premarital Sex', 'Wants Kids', 'calm', 'rational', 'emotional',
       'stubborn', 'adventurous', 'creative', 'analytical', 'introvert',
       'extrovert', 'going_out', 'staying_in', 'status', "Zodiac", "Partner's Zodiac"]

numeric_options = ['Happiness', 'Compatibility']

## CORRELATION Matrix
## transforming categorical variables

# BACKGROUND
pref_r = {'You, Your Partner': 1,
          'You': 2,
        'Your Partner': 3}

df['smoke'].replace(to_replace=pref_r, inplace= True)
df['drink'].replace(to_replace=pref_r, inplace= True)
df['drug'].replace(to_replace=pref_r, inplace= True)
df['premarital_sex'].replace(to_replace=pref_r, inplace= True)
df['kids'].replace(to_replace=pref_r, inplace= True)

df['calm'].replace(to_replace=pref_r, inplace= True)
df['rational'].replace(to_replace=pref_r, inplace= True)
df['emotional'].replace(to_replace=pref_r, inplace= True)
df['stubborn'].replace(to_replace=pref_r, inplace= True)
df['adventurous'].replace(to_replace=pref_r, inplace= True)
df['creative'].replace(to_replace=pref_r, inplace= True)
df['analytical'].replace(to_replace=pref_r, inplace= True)
df['introvert'].replace(to_replace=pref_r, inplace= True)
df['extrovert'].replace(to_replace=pref_r, inplace= True)
df['going_out'].replace(to_replace=pref_r, inplace= True)
df['staying_in'].replace(to_replace=pref_r, inplace= True)

df['age'].replace(to_replace= {'<20': 0, '20-29': 1, "30-49": 2, "30-50": 2, "50+":3}, inplace= True)
df['p_age'].replace(to_replace= {'<20': 0, '20-29': 1, "30-49": 2, "30-50": 2, "50+":3}, inplace= True)

df['gender'].replace(to_replace= {'Female':0, 'Male':1}, inplace= True)
df['p_gender'].replace(to_replace={'Female':0, 'Male':1}, inplace= True)
df['income'].replace(to_replace={'Neither of us have income': 0,
                                'My ex/partner has no income': 1,
                                'I have no income': 2,
                                'I make the same as my ex/partner': 3,
                                'My ex/partner makes more than me': 4,
                                'I make more than my ex/partner': 5}, inplace = True)

df['ethnicity'].replace(to_replace={'Yes':1, 'No':0}, inplace= True)


df['education'].replace(to_replace={'None':0,
                                    'High School':1,
                                    'Associates': 2,
                                   'Bachelors': 3,
                                   'Masters': 4,
                                   'PhD': 5,
                                   'Other professional degree': 6}, inplace= True)

df['p_education'].replace(to_replace={'None':0,
                                    'High School':1,
                                    'Associates': 2,
                                   'Bachelors': 3,
                                   'Masters': 4,
                                   'PhD': 5,
                                   'Other professional degree': 6}, inplace= True)

df['political'].replace(to_replace={'Yes':1, 'No':0, 'Maybe':2}, inplace= True)

corr = df.corr()
corr2 = pd.melt(corr.reset_index(), id_vars='index')
corr2.columns = ['x', 'y', 'value']

x_labels = [v for v in sorted(corr2['x'].unique())]
y_labels = [v for v in sorted(corr2['y'].unique())]

corr_matrix = go.Figure(data=go.Heatmap(z=corr, x = x_labels, y= y_labels))
corr_matrix.update_layout(width = 1000, height = 1000,
                  title = {'text': "Characteristics Correlation Matrix", 'xanchor': 'center','x':0.5,})

def graph(zod1, zod2, xaxis, yaxis, size, color):
    mask1 = [zod in zod1 for zod in og_df['Zodiac']]
    temp = og_df[mask1]
    mask2 = [zod in zod2 for zod in temp["Partner's Zodiac"]]
    dff = temp[mask2]
    fig = px.scatter(dff, x = xaxis, y = yaxis, size = size, color = color, opacity = 0.5)
    fig.update_layout(title = {'text': u'{} v. {}'.format(xaxis, yaxis), 'x': 0.5}, height = 750)
    return fig

output = html.Div([
    dcc.Graph(id = 'graph_output')
])

header = html.Div([
    html.Br(),
    dbc.Jumbotron([
        html.H1('What Patterns Can You Find?'),
        html.P("Explore some interactive visualizations of our user generated data."),
        ]
    ),
    html.Br()
])

graph_builder = html.Div([
    html.Br(),
    dbc.Container([
        dbc.Label('Select one or more primary signs', html_for = 'dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'Aquarius (January 20 - February 18)', 'value': 'Aquarius'},
                {'label': 'Pisces (February 19 - March 20)', 'value': 'Pisces'},
                {'label': 'Aries (March 21 - April 19)', 'value': 'Aries'},
                {'label': 'Taurus (April 20 - May 20)', 'value': 'Taurus'},
                {'label': 'Gemini (May 21 - June 20)', 'value': 'Gemini'},
                {'label': 'Cancer (June 21 - July 22)', 'value': 'Cancer'},
                {'label': 'Leo (July 23 - August 22)', 'value': 'Leo'},
                {'label': 'Virgo (August 23 - September 22)', 'value': 'Virgo'},
                {'label': 'Libra (September 23 - October 22)', 'value': 'Libra'},
                {'label': 'Scorpio (October 23 - November 21)', 'value': 'Scorpio'},
                {'label': 'Sagittarius (November 22 - December 21)', 'value': 'Sagittarius'},
                {'label': 'Capricorn (December 22 - January 19)', 'value': 'Capricorn'},
            ],
            id = 'zodiac-1',
            multi = True
        ),]
    ),
    html.Br(),
    dbc.Container([
        dbc.Label('Select one or more partner signs', html_for = 'dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'Aquarius (January 20 - February 18)', 'value': 'Aquarius'},
                {'label': 'Pisces (February 19 - March 20)', 'value': 'Pisces'},
                {'label': 'Aries (March 21 - April 19)', 'value': 'Aries'},
                {'label': 'Taurus (April 20 - May 20)', 'value': 'Taurus'},
                {'label': 'Gemini (May 21 - June 20)', 'value': 'Gemini'},
                {'label': 'Cancer (June 21 - July 22)', 'value': 'Cancer'},
                {'label': 'Leo (July 23 - August 22)', 'value': 'Leo'},
                {'label': 'Virgo (August 23 - September 22)', 'value': 'Virgo'},
                {'label': 'Libra (September 23 - October 22)', 'value': 'Libra'},
                {'label': 'Scorpio (October 23 - November 21)', 'value': 'Scorpio'},
                {'label': 'Sagittarius (November 22 - December 21)', 'value': 'Sagittarius'},
                {'label': 'Capricorn (December 22 - January 19)', 'value': 'Capricorn'},
            ],
            id = 'zodiac-2',
            multi = True
        )
    ]),
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Label('X Axis Variable', html_for = 'dropdown'),
                dbc.Select(
                    options = [{'label': i, 'value': i} for i in graph_options],
                    id = 'x'
                )
            ]),
            dbc.Col([
                dbc.Label('Y Axis Variable', html_for = 'dropdown'),
                dbc.Select(
                    options = [{'label': i, 'value': i} for i in graph_options],
                    id = 'y'
                )
            ])
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Classify by Size', html_for = 'dropdown'),
                dbc.Select(
                    options = [{'label': i, 'value': i} for i in numeric_options],
                    id = 'size'
                )
            ]),
            dbc.Col([
                dbc.Label('Classify by Color', html_for = 'dropdown'),
                dbc.Select(
                    options = [{'label': i, 'value': i} for i in graph_options],
                    id = 'color'
                    )
            ])
        ])
    ]),
    html.Br()
])

def trends():
    layout = html.Div([
        navbar(),
        header,
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure = corr_matrix, id = 'corr')
            ])
        ], justify = "center"),
        graph_builder,
        output,
        html.Br(),
        footer()
    ])
    return layout

'''
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = trends()

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



if __name__ == '__main__':
    app.run_server(debug=True)

'''
