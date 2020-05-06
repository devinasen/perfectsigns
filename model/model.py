# -*- coding: utf-8 -*-
"""Models for website code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpzwi1JD1A8FNjjmC17V7eADlEs7C50e

Modified greatly.
"""

# Commented out IPython magic to ensure Python compatibility.
import sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import joblib

## DataFrame Set Up
df = pd.read_csv('Data Collection Survey (Responses).csv')
pd.set_option('display.max_columns', 10)

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

# remove timestamp column
# fill na with 0
df.replace('', np.nan, inplace=True)
df.fillna(0, inplace= True)
df.drop(columns=['Timestamp'], axis=0, inplace= True)


#one hot encoding
df_temp = df.iloc[:, 14:]
char_col_name = ['smoke',	'drink',	'drug',	'premarital_sex',	'kids',	'calm',	'rational',	'emotional',	'stubborn',
                 'adventurous',	'creative',	'analytical',	'introvert',	'extrovert',	'going_out',	'staying_in']
chars_df = pd.DataFrame()
for col in char_col_name:
  you = []
  partner = []
  for i in np.arange(len(df)):
    if df[col][i] == 'You':
      you.append(1)
      partner.append(0)
    elif df[col][i] == 'Your Partner':
      partner.append(1)
      you.append(0)
    elif df[col][i] == 'You, Your Partner':
      you.append(1)
      partner.append(1)
    else:
      you.append(0)
      partner.append(0)
  you_name = "r_" + col
  partner_name = "p_" + col
  df[you_name] = you
  df[partner_name] = partner
df.drop(labels = ['smoke',	'drink',	'drug',	'premarital_sex',	'kids',	'calm',	'rational',	'emotional',	'stubborn', 'adventurous',
                  'creative',	'analytical',	'introvert',	'extrovert',	'going_out',	'staying_in'], axis = 1, inplace = True )
df['gender'].replace(to_replace= {'Female':0, 'Male':1}, inplace= True)
df['p_gender'].replace(to_replace={'Female':0, 'Male':1}, inplace= True)
df['ethnicity'].replace(to_replace={'Yes':1, 'No':0}, inplace= True)
df['political'].replace(to_replace={'Yes':1, 'No':0, 'Maybe':2}, inplace= True)
df['religion'].replace(to_replace={'Yes':1, 'No':0}, inplace= True)

"""Zodiac Predictor"""

df_dumb = df.copy()
Y_Matrix =pd.get_dummies(df_dumb['p_zodiac'])
df_dumb.drop(labels = ['p_zodiac', 'status'], inplace = True, axis = 1)
temp_col = df_dumb.columns
cols_to_drop = ['happy', 'compatible', 'income']
for i in temp_col:
  if i[0:2] == 'p_':
    cols_to_drop.append(i)
df_dumb.drop(labels = cols_to_drop, inplace = True, axis = 1)
X = pd.get_dummies(df_dumb)

"""Features being used for this DF:


* Gender
* Same Ethnicity
* Same Religion
* Same Political Views
* Smoke
* Drink
* Drug
* Premarital Sex
* Kids
* Calm
* Rational
* Emotional
* Stubborn
* Adventurous
* Creative
* Analytical
* Introvert
* Extrovery
* Going Out
* Staying In
* Zodiac
* Education
* Age
"""

#building and training model
model_zodiac = DecisionTreeClassifier()
model_zodiac.fit(X, Y_Matrix)

joblib.dump(model_zodiac, 'zodiac.joblib.z')
#to retrieve: model_zodiac = externals.joblib.load('zodiac.job.lib.z')

"""Characteristic Predictor"""

temp_col = df.columns
p_cols = []
for i in temp_col:
  if i[0:2] == 'p_':
    p_cols.append(i)
Y_mat_chars = df.loc[:, p_cols]
Y_mat_chars.drop(labels = ['p_age', 'p_gender', 'p_education', 'p_zodiac'], inplace = True, axis = 1)

#building and training models for each characteristic, storing in dictionary
chars_model_dictionary = {}
for p in Y_mat_chars.columns:
  model_chars = LogisticRegression()
  model_chars.fit(X, Y_mat_chars[p])
  chars_model_dictionary[p] = model_chars

joblib.dump(chars_model_dictionary, 'char_dict.joblib.z')
#to retrieve: chars_model_dictionary = externals.joblib.load('char_dict.joblib.z')




"""Response Generator
    The following code is not utilized here but replicated and adjusted in product.py.
    It is left here to demonstrate how the above models are used to generate text results. """

def zod_predictions(resp):
  text = "Your most compatible sign is: "
  zod = model_zodiac.predict(resp).tolist()[0]
  ind = zod.index(1)
  comp_sign = Y_Matrix.columns[ind]
  text = text + comp_sign + ". "
  return text

char_response_dict = {
    'p_smoke' : "Your ideal partner is someone who enjoys a quick smoke",
    'p_drink' : "Your ideal partner is someone who enjoys a drink or two",
    'p_drug' : "Your ideal partner is someone who enjoys a drugs",
    'p_premarital_sex' : "Your ideal partner is someone who believes in premarital sex",
    'p_kids' : "Your ideal partner is someone who wants to have kids",
    'p_calm' : "Your ideal partner is someone who is calm",
    'p_rational' : "Your ideal partner is someone who is rational",
    'p_emotional' : "Your ideal partner is someone who is emotional",
    'p_stubborn' : "Your ideal partner is someone who is stubborn",
    'p_adventurous' : "Your ideal partner is someone who is adventurous",
    'p_creative' : "Your ideal partner is someone who is creative",
    'p_analytical' : "Your ideal partner is someone who is analytical",
    'p_introvert' : "Your ideal partner is someone who is an introvert",
    'p_extrovert' : "Your ideal partner is someone who is an extrovert",
    'p_going_out' : "Your ideal partner is someone who likes to go out",
    'p_staying_in':  "Your ideal partner is someone who like to stay in"
}

def char_predictions(resp):
  text = ""
  for p in chars_model_dictionary:
    mod = chars_model_dictionary[p]
    pred = mod.predict(resp)[0]
    if pred >= 0.5:
      text += char_response_dict[p] + ". "
  return text

def total_predictions(resp):
  a = zod_predictions(resp)
  b = char_predictions(resp)
  return a  + b