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
from footer import footer

#navigation
nav = navbar()

#loading models and response text
model_filename = 'zodiac.joblib.z'
model_zodiac = joblib.load(model_filename)
chars_model_dictionary = joblib.load('char_dict.joblib.z')

zodiac_signs = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini', 'Leo', 'Libra', 'Pisces',
        'Sagittarius', 'Scorpio', 'Taurus', 'Virgo']

char_response_dict = {
    'p_smoke' : "Your ideal partner may enjoy a quick smoke",
    'p_drink' : "Your ideal partner probably indulges in a drink or two",
    'p_drug' : "They are someone who likely enjoys drugs",
    'p_premarital_sex' : "Premarital sex doesn't scare them",
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

zod_desc_dict = {
    'Aquarius': "Your top match is an Aquarius! You've got yourself a free-spirited intellectual, eager to change the world for the better. They love to get ahead in life and are naturally-driven. Sometimes their energy may come off too strong or overbearing, but that's because they love their independence. It may take time to build a relationship with an Aquarius, but once they've gained your trust, they'll never let you go. ",
    'Pisces': "Your ideal partner is a Pisces — a deep, loving water sign. Pisces value openness and honesty in the relationship. They are not afraid to show their emotions or speak their mind. At times, you may find yourself to be more emotionally distant than your partner but to rekindle your love, simply just show them your romantic, compassionate side. They are idealistic, often imaginitive and love to see the best in everything.",
    'Aries': "You've got Aries as your top match! This fire sign is fun, outgoing, and loves to be the leader.  They are bold, adventurous, and competitive. Aries definitely can be hot-headed at times, but don't let that get in the way. At the end of the day, they will proudly love you, make you feel secure, and will stand up for you no matter what.",
    'Taurus': "You've got a Taurus! They are tenacious, hard-working, grounded individuals. They're strong-willed and are ready to make a difference in the world. They love the great outdoors but sometimes they need some time to themselves and might prefer to just stay home. You may find some materialistic, stubborn tendencies but they promise a relationship filled with love and stability. You can rely on them and seek inspiration in their perserverence and talents.",
    'Gemini': "Your top match is a Gemini! Gemini are fun, dynamic, sometimes intense lovers. They love adventure but also are cautious in their actions. They value their independence and aren't afraid to take the reins in the relationship. Geminis are the twins, so you may notice duality in their personality but that's part of the fun and dynamism. They are not afraid to express their feelings so be bold, open, and flirty too.",
    'Cancer': "Your ideal match is a Cancer! Hold on to a Cancer because they are fun, sensitive, loyal partners. They are water signs and are ready to show you their romantic side. They are easy to talk to so you've got yourself a great friend too. You may find it difficult for them to trust you at first, but once they do, you're on your way to a blossoming relationship. ",
    'Leo': "You've got yourself a Leo! Here's to a relationship filled with fun, fire, and passion! Leos are playful, social butterfies who love to have a good time. These lions lead busy, sometimes even independent, lives so it might be hard to keep up with them once in a while. They tend to hide their emotional side to them but that doesn't mean they don't have a special place in their heart for you! ",
    'Virgo': "Your ideal partner is a Virgo! Virgos are very observant and will pay attention to the small things. They are rational and grounded so they may not outwardly express their emotions but don't misunderstand that. They are equally loyal, loving and make strong partners. They prefer organization and can be critical so don't be caught off guard by their calenders, planning, and schedules.",
    'Libra': "You're ideal partner is a Libra! Libras are talented, free-willed individuals who love to display their creative side to them. While they are open and honest, Libras are non-confrontation and could hold grudges if you nudge them the wrong way. Your partner will have a charming personality and will lead a balanced life. They are your 'chaotic-good' lovers who are open and ready to try new experiences.",
    'Scorpio': "Your ideal match is a Scorpio! You've got yourself a powerful, passionate, and fierce individual. Scorpios are natural leaders who aren't afraid to express their mind. They are confident and truly believe if there is a will, there is a way. Help slow them down, as they can be aggressive, sometimes even jealous. You may not see their emotional side upfront, but deep down, this water sign will give you their world.",
    'Sagittarius': "Your top sign is a Sagittarius! They are curious, energetic people that truly like to live life unconventionally. Sagittarius love their freedom so never get in their way and appreciate space between you two. You may find that they love to be right and are impatient. Sagittarius are ultimately warm, honest individuals that will always look out for you and help you grow.",
    'Capricorn': "You've got a Capricorn! This Earth sign is practical, ambitious, career-driven and treasure their values. They work hard so they can show off their best self to crowds. They have materialistic, conceited tendencies but they appreciate you keeping them grounded. They are guided by realistic, disciplined approaches to life so nothing will ever cloud their judgement once they set their mind to something. Success and abundance will be a guiding principle in your relationship long-term.",
}

#running models on user submitted data (prediction methods)
def zod_predictions(resp):
    text = "Your most compatible sign is: "
    zod = model_zodiac.predict(resp).tolist()[0]
    ind = zod.index(1)
    comp_sign = zodiac_signs[ind]
    text = text + comp_sign + ". "
    desc = zod_desc_dict[comp_sign]
    return html.H5(text, className="card-title"), html.P(desc)

def char_predictions(resp):
  text = ""
  predictions = {}
  for p in chars_model_dictionary:
    mod = chars_model_dictionary[p]
    pred = mod.predict(resp)[0]
    if pred >= 0.5:
      predictions[p] = pred
  if 'p_extrovert' in predictions and 'p_introvert' in predictions:
    if predictions['p_extrovert'] >= predictions['p_introvert']:
      del predictions['p_introvert']
    else:
      del predictions['p_extrovert']
  if 'p_staying_in' in predictions.keys():
    if 'p_going_out' in predictions.keys():
      if predictions['p_going_out'] >= predictions['p_staying_in']:
        del predictions['p_staying_in']
      else:
        del predictions['p_going_out']
  for key in predictions.keys():
    text += char_response_dict[key] + ". "
  return html.P(
                text,
                className="card-text",
            )

#returns results text
def total_predictions(resp):
  a, b = zod_predictions(resp)
  c = char_predictions(resp)
  return dbc.CardBody([a, b, c])

#creating survey
survey = html.Div(children=[
        dbc.Row(
            dbc.Col(html.H1(children='Your Ideal Zodiac Partner'), width = {'offset': 2})
        ),

        dbc.Row(
            dbc.Col(html.Div(children='''Take this quiz and find out about your ideal life partner.'''),
                width = {'offset': 2})
        ),

        html.Br(),
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
                dbc.Label('Do you want your partner to follow the same religion as you?'),
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

# Results Pop Up
res = html.Div([
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Card(id = 'result', color = "info", inverse = True),
                width = 7
                ),
            justify = 'center',
        )])

#building page
def product():
    layout = html.Div([
        nav,
        html.Br(),
        survey,
        res,
        html.Br(),
        footer(),
    ])
    return layout

#taking in survey data and running prediction methods to generate results
def result(name, q1, q2, q3, q4, q5, q6, q7, q8, q9):

    #one hot encoding characteristics
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

    #one hot encoding zodiac sign
    zodiac = []
    for sign in zodiac_signs:
        if sign == q1:
            zodiac.append(1)
        else:
            zodiac.append(0)

    #one hot encoding age category via dictionary
    ages = {'<20': [0, 0, 0, 0, 1],
    '20-29': [1, 0, 0, 0, 0],
    '30-50': [0, 0, 1, 0, 0],
    '50+': [0, 0, 0, 1, 0]}

    age = ages[q2]

    #one hot encoding education category via dictionary
    education = {'ba': [1, 0, 0, 0, 0], 'hs': [0, 1, 0, 0, 0],
    'm': [0, 0, 1, 0, 0], 'phd': [0, 0, 0, 0, 1], 'p': [0, 0, 0, 1, 0]}
    ed = education[q7]

    #creating 1 row dataframe of inputs for models
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
