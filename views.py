'''
views.py is essentially the "frontend" while utils is the "backend". Functions in views should mostly 
set up the layout of the application. Any othe rfunctionality can probably reside in utils or elsewhere
'''

import pandas as pd
import numpy as np
from datetime import datetime

import streamlit as st

import utils
import plots

def welcome():
    st.set_page_config(page_title='Trkkr',
                       page_icon=':muscle:',
                       layout='wide')
    st.write(f"# Trkkr")

def form():
    weight = np.empty(1)

    df = utils.load_table()

    # User
    t = st.empty()
    t.write(f'### Welcome back, User!')

    name = st.selectbox(
        'Who is this?',
        ('Select User', 'Ian McNair', 'Wayne Chim')
    )

    dod = st.empty()

    if name == 'Select User':
        st.plotly_chart(plots.general_weight(df))       
    else:
        plots.current_weight(df, name)
        fname = name.split()[0]
        t.write(f'### Welcome back, {fname}!')
        fig, slope = plots.weight_track(df, name)
        st.plotly_chart(fig)
        st.write(f'{name} is changing weight by {round(slope, 2)} per day on average')
    # WE SHOULD DEF PUSH THIS (below) INTO ANOTHER FUNCTIONS MAYBE???
    # LIKE A FORMATTING.PY FILE???? 
    # Just seems like a lot happening and its hard to read/follow at a glance.
    
    # Input fields

    weight = st.number_input(label = 'Weight',
                             min_value = 0.0,
                             step = 0.1)

    # Unit of Measure
    uom = st.radio('Unit of Measure',
                   ['Pounds', 'Kilograms'])   

    if weight > 0:
        if uom == 'Pounds':
            lb = round(weight, 2)
            kg = round(weight/2.2, 2)
            st.write(f'{lb} lb or {kg} kg')
        elif uom == 'Kilograms':
            lb = round(weight*2.2,2)
            kg = round(weight,2)
            st.write(f'{lb} lb or {kg} kg')
    
    # Data Submission
    submit_button = st.button('Submit Data')

    # Package Data into JSON
    if submit_button:
        dt = str(datetime.now())

        entry = {
            'timestamp': dt,
            'user': name,
            'wt_lb': lb,
            'wt_kg': kg
        }

        st.json(entry)
        utils.submit(entry)

def goals():
    pass