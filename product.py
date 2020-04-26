#the real thing!

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import joblib

from nav import navbar
nav = navbar()

model_filename = 'zodiac.joblib.z'
model_zodiac = joblib.load(model_filename)
chars_model_dictionary = joblib.load('char_dict.joblib.z')

zodiac_signs = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces',
        'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']

char_response_dict = {
    'p_smoke' : "Your ideal partner may enjoy a quick smoke",
    'p_drink' : "Your ideal partner probably indulges in a drink or two",
    'p_drug' : "They are someone who likely enjoys drugs",
    'p_premarital_sex' : "Premarital sex doesn't scare them.",
    'p_kids' : "They may look forward to having kids in the future",
    'p_calm' : "Your ideal partner is someone who makes you feel calm",
    'p_rational' : "Your ideal partner will be rational",
    'p_emotional' : "Their emotional side will keep you on your toes",
    'p_stubborn' : "Surprise, surpise, your ideal partner will probably be a stubborn person, but you know how to handle it",
    'p_adventurous' : "Your ideal partner will be adventurous and show you new paths",
    'p_creative' : "Your ideal partner is someone who is creative",
    'p_analytical' : "This person will be analytical, too",
    'p_introvert' : "Your ideal partner's introvertedness may be unexpectedly endearing",
    'p_extrovert' : "Your ideal partner will have extroverted tendencies which you might find strangely heartwarming",
    'p_going_out' : "Your ideal partner is someone who likes to go out, so without further ado, put yourself out there because your perfect life partner is waiting for you",
    'p_staying_in':  "Your ideal partner may be someone who likes to stay in, but that won't stop you from finding each other soon."
}

def zod_predictions(resp):
    text = "Your most compatible sign is: "
    zod = model_zodiac.predict(resp).tolist()[0]
    ind = zod.index(1)
    comp_sign = zodiac_signs[ind]
    text = text + comp_sign + ". "
    return html.H5(text, className="card-title")

def char_predictions(resp):
  text = ""
  for p in chars_model_dictionary:
    mod = chars_model_dictionary[p]
    pred = mod.predict(resp)[0]
    if pred >= 0.5:
      text += char_response_dict[p] + ". "
  return html.P(
                text,
                className="card-text",
            )

def total_predictions(resp):
  a = zod_predictions(resp)
  b = char_predictions(resp)
  return dbc.CardBody([a, b])

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

'''q1 = dbc.FormGroup(
    [
        dbc.Label('Name?'),
        dbc.Input(id="name", placeholder = 'Type here', type = 'text'),
    ]
)

q2 = dbc.FormGroup(
    [
        dbc.Label("What's your Zodiac sign?"),
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
            placeholder = 'Select...'
        ),
    ]
)

survey = dbc.Form([q1, q2])
'''
survey = html.Div(children=[
        dbc.Row(
            dbc.Col(html.H1(children='Your Ideal Zodiac Partner'), width = {'offset': 2})
        ),

        dbc.Row(
            dbc.Col(html.Div(children='''Take the quiz and find out who's the one for you.'''),
                width = {'offset': 2})
        ),

        html.Br(),

        dbc.Row([dbc.Col([
        dbc.Form([
            dbc.FormGroup([
                dbc.Label('Name?'),
                dbc.Input(id="name", placeholder = 'Type here', type = 'text', style = {'width': '80%'}),
            ]),

            dbc.FormGroup([
                dbc.Label("What's your Zodiac sign?", html_for = 'dropdown'),
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
                    placeholder = 'Select...',
                    id = 'q1',
                    style = {'width': '80%'}
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Age range', html_for = 'dropdown'),
                dcc.Dropdown(
                    options=[
                    {'label': '<20', 'value': '<20'},
                    {'label': '20-29', 'value': '20-29'},
                    {'label': '30-50', 'value': '30-50'},
                    {'label': '50+', 'value': '50+'}
                    ],
                    placeholder = 'Select...',
                    id = 'q2',
                    style = {'width': '80%'}
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Gender'),
                dbc.RadioItems(
                    options = [
                        {'label': 'Female', 'value': 0},
                        {'label': 'Male', 'value': 1},
                    ],
                    id = 'q3',
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Do you want your partner to have the same ethnicity as you?'),
                dbc.RadioItems(
                    options = [
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    id = 'q4'
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Do you want your partner to folow the same religion as you?'),
                dbc.RadioItems(
                    options = [
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    id = 'q5'
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Do you want your partner to have the same political views as you?'),
                dbc.RadioItems(
                    options = [
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0},
                        {'label': 'Maybe', 'value': 2}
                    ],
                    id = 'q6'
                )
            ]),


            dbc.FormGroup([
                dbc.Label('Your highest level of education (or in progress)'),
                dcc.Dropdown(
                    options=[
                    {'label': 'High School', 'value': 'hs'},
                    {'label': 'Bachelors', 'value': 'ba'},
                    {'label': 'Masters', 'value': 'm'},
                    {'label': 'PhD', 'value': 'phd'},
                    {'label': 'Other professional degree', 'value': 'p'}
                    ],
                    placeholder = 'Select...',
                    id = 'q7',
                    style = {'width': '80%'}
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Select all that apply to you.'),
                dbc.Checklist(
                    options=[
                        {'label': 'I smoke', 'value': 'smoke'},
                        {'label': 'I drink', 'value': 'drink'},
                        {'label': 'I use drugs recreationally', 'value': 'drugs'},
                        {'label': 'I do not oppose premarital sex', 'value': 'sex'},
                        {'label': 'I want to have kids', 'value': 'kids'}
                    ],
                    id = 'q8'
                )
            ]),

            dbc.FormGroup([
                dbc.Label('Tell us more about you! Select all the personality traits that apply to you.'),
                dbc.Checklist(
                    options=[
                        {'label': 'Calm', 'value': 'Calm'},
                        {'label': 'Rational', 'value': 'Rational'},
                        {'label': 'Emotional', 'value': 'Emotional'},
                        {'label': 'Stubborn', 'value': 'Stubborn'},
                        {'label': 'Adventurous', 'value': 'Adventurous'},
                        {'label': 'Creative', 'value': 'Creative'},
                        {'label': 'Analytical', 'value': 'Analytical'},
                        {'label': 'Introvert', 'value': 'Introvert'},
                        {'label': 'Extrovert', 'value': 'Extrovert'},
                        {'label': 'Like going out', 'value': 'Out'},
                        {'label': 'Like staying in', 'value': 'In'}
                    ],
                    id = 'q9'
                )
            ]),

        ]),
        ], width = {'offset': 2})]),

        html.Br(),

        dbc.Row([
            dbc.Col([
                dbc.Button('Submit', id = 'user-survey'),
                ],
                width = {'offset': 2}, align = "center"
            ),
            dbc.Col([
                html.P(
                    id = 'error',
                    style = {'color': 'red'}
                )],
                align = "bottom"
            )
        ])
    ])


res = html.Div([
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Card(id = 'result', color = "info", inverse = True),
                width = 7
                ),
            justify = 'center',
        )])

def product():
    layout = html.Div([
        nav,
        html.Br(),
        survey,
        res
    ])
    return layout


def result(name, q1, q2, q3, q4, q5, q6, q7, q8, q9):

    #one hot encoding
    features = ['smoke', 'drink', 'drugs', 'sex', 'kids',
        'Calm', 'Rational', 'Emotional', 'Stubborn', 'Adventurous',
        'Creative', 'Analytical', 'Introvert', 'Extrovert', 'Out', 'In']
    responses = []
    if q8:
        responses.extend(q8)
    if q9:
        responses.extend(q9)
    values = []
    for feature in features:
        if feature in responses:
            values.append(1)
        else:
            values.append(0)

    zodiac = []
    for sign in zodiac_signs:
        if sign == q1:
            zodiac.append(1)
        else:
            zodiac.append(0)

    ages = {'<20': [0, 0, 0, 0, 1],
    '20-29': [1, 0, 0, 0, 0],
    '30-50': [0, 0, 1, 0, 0],
    '50+': [0, 0, 0, 1, 0]}

    age = ages[q2]

    education = {'ba': [1, 0, 0, 0, 0], 'hs': [0, 1, 0, 0, 0],
    'm': [0, 0, 1, 0, 0], 'phd': [0, 0, 0, 0, 1], 'p': [0, 0, 0, 1, 0]}
    ed = education[q7]

    input = pd.DataFrame({'gender': [q3], 'ethnicity': [q4], 'political': [q6],
    'religion': q5, 'r_smoke': values[0], 'r_drink': values[1],
       'r_drug': values[2], 'r_premarital_sex': values[3], 'r_kids': values[4],
       'r_calm': values[5], 'r_rational': values[6], 'r_emotional': values[7],
       'r_stubborn': values[8], 'r_adventurous': values[9], 'r_creative': values[10],
       'r_analytical': values[11], 'r_introvert': values[12], 'r_extrovert': values[13],
       'r_going_out': values[14],'r_staying_in': values[15],
       'zodiac_Aquarius (January 20 - February 18)': zodiac[0],
       'zodiac_Aries (March 21 - April 19)': zodiac[1],
       'zodiac_Cancer (June 21 - July 22)': zodiac[2],
       'zodiac_Capricorn (December 22 - January 19)': zodiac[3],
       'zodiac_Gemini (May 21 - June 20)': zodiac[4],
       'zodiac_Leo (July 23 - August 22)': zodiac[5],
       'zodiac_Libra (September 23 - October 22)': zodiac[6],
       'zodiac_Pisces (February 19 - March 20)': zodiac[7],
       'zodiac_Sagittarius (November 22 - December 21)': zodiac[8],
       'zodiac_Scorpio (October 23 - November 21)': zodiac[9],
       'zodiac_Taurus (April 20 - May 20)': zodiac[10],
       'zodiac_Virgo (August 23 - September 22)': zodiac[11], 'age_20-29': age[0], 'age_30-49': age[1],
       'age_30-50': age[2], 'age_50+':age[3], 'age_<20': age[4], 'education_Bachelors': ed[0],
       'education_High School': ed[1], 'education_Masters': ed[2],
       'education_Other professional degree': ed[3], 'education_PhD': ed[4]})

    return total_predictions(input), ''

'''
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = product()


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




if __name__ == '__main__':
    app.run_server(debug=True)
'''
