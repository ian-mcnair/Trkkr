import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time

st.title('My Fitness Tracker')
st.subheader('Welcome back, User')

# Form
with st.form(key='my_form'):
    weight_input = st.number_input(label='Weight (lbs):')
    rep_input = st.number_input(label='Reps:')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'{int(weight_input)} pounds lifted {int(rep_input)} times.')

table = pd.DataFrame(columns={'% of ORM', 'Weight (lbs)', 'Reps'})
table = table[['% of ORM', 'Weight (lbs)', 'Reps']]

if rep_input == 1:
    orm = weight_input
else:
    orm = weight_input*(1+(0.0333*rep_input))

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