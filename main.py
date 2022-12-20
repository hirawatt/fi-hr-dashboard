import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.graph_objects as go

# positivity        = 1-10 | 1-3 : red, 4-7 : orange, 8-10 : green
# motivation bar    = 1-10
# meditaion         = number of times meditated in a month
# heatmap of the month
# Moods source - https://positive.b-cdn.net/wp-content/uploads/wheel-of-emotions.jpg
mood = ['trust', 'fear', 'suprise', 'sadness', 'disgust', 'anger', 'anticipation', 'joy']
team = ['HR', 'Finance', 'Marketing', 'Sales', 'Technology', 'Management']

# Data Import
df = pd.read_csv("./data/20-12-2022.csv")
with st.expander("Mock Data", expanded=False):
    st.write(df)

p_score = df['Positivity Score']

# Selection of team & employees
co1, co2 = st.columns(2)
teams = co1.multiselect("Teams", df['Team'], default = df['Team'])
people = co2.multiselect("Employee", df['Name'], default = df['Name'])

# Heatmap


# Gauge Charts -> https://plotly.com/python/reference/indicator/
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    delta = {'reference': p_score[0]},
    value = p_score[1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Positivity Score"},
    gauge = {'axis': {'range': [None, 10],
                    'tickmode': 'array',
                    'ticktext': ['Negative', 'Moderate', 'Positive'],
                    'tickvals': [0, 4, 7, 10]},
            'steps': [
                {'range': [0, 3], 'color': "red", 'name': 'Negative'},
                {'range': [3, 7], 'color': "rgb(255,200,0)", 'name': 'Moderate'},
                {'range': [7, 10], 'color': "lightgreen"}]}))

st.plotly_chart(fig, use_container_width=True)

# Data Analysis
col1, col2 = st.columns(2)
col1.bar_chart(df.iloc[:, 3])
col2.bar_chart(df.iloc[:, 4])

st.bar_chart(df.iloc[:, 5])