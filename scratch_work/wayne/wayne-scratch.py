import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime

spreadsheet_id = '10dR2sGTVPDbEZSIyfugg49khBsRvXbPP0tVzf211zTM'
range_name = 'A1:AA1000'

st.title('Trkkr')
st.subheader('Welcome back, User')

user_ls = ['Wayne', 'Ian']

# Form
with st.form(key='my_form'):
    uid = st.text_input(label='User ID:')
    lift = st.radio('Lift', ['Bench Press', 'Deadlift'])
    weight_input = st.number_input(label='Weight (lbs):')
    rep_input = st.number_input(label='Reps:')
    ingestion = st.radio('Ingestion', ['Real-time', 'Historical'])
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    timestamp = datetime.now()
    st.write(f'{user_ls[int(uid)]} lifted {int(weight_input)} pounds {int(rep_input)} times for {lift} on {timestamp}.')

    table = pd.DataFrame(columns={'% of ORM', 'Weight (lbs)', 'Reps'})
    table = table[['% of ORM', 'Weight (lbs)', 'Reps']]

    if rep_input == 1:
        orm = weight_input
    else:
        orm = weight_input*(1+(0.0333*rep_input))

    st.caption(f'Your 1-rep max is: {orm} pounds!')

    pct = []
    wt = []
    rp = [1, 2, 4, 6, 8, 10, 12, 16, 20, 24, 30]
    for i in range(100, 45, -5):
        pct.append(str(i) + '%')
        wt.append(i/100*orm)

    table['% of ORM'] = pct
    table['Weight (lbs)'] = wt
    table['Reps'] = rp
    st.table(table)

    write = pd.DataFrame(columns={'Date', 'UserID', 'Lift', 'Weight', 'Reps', 'ORM', 'IngestionType'})
    write = write[['Date', 'UserID', 'Lift', 'Weight', 'Reps', 'ORM', 'IngestionType']]

    write = write.append({'Date': timestamp,
                  'UserID': uid,
                  'Lift': lift,
                  'Weight': weight_input,
                  'Reps': rep_input,
                  'ORM': orm,
                  'IngestionType': ingestion
    }, ignore_index=True)

    st.table(write)

#a = st.sidebar.radio('R:',[1,2])

#st.slider('Slide me', min_value=0, max_value=10)

#st.select_slider('Slide to select', options=[1,'2'])