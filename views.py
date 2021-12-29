from typing import NamedTuple
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
#import streamlit_authenticator as stauth
import utils


def welcome():
    st.write(f"# Trkkr")

def form():
    amt = np.empty(1)
    reps = np.empty(1)
    lift = ''
    
    # User
    t = st.empty()
    
    t.write(f'### Welcome back, User!')
    
    name = st.selectbox(
        'Who is this?',
        ('Select User', 'Ian McNair', 'Wayne Chim')
    )

    if name == 'Select User':
        t.write(f'### Welcome back, User!')
    else:
        fname = name.split()[0]
        t.write(f'### Welcome back, {fname}!')

    # Attribute
    attribute = st.radio(
        'Attribute', ['Body Weight', 'Lifts', 'Running']
    )

    if attribute == 'Body Weight':
        amt_label = 'Weight (lbs)'
        lift = 'Body Weight'
        reps = 1

        amt = st.number_input(
            label = amt_label,
            min_value = 0,
            step = 1)

    elif attribute == 'Lifts':
        amt_label = 'Weight (lbs)'
        rep_label = 'Reps'

        amt = st.number_input(
            label = amt_label,
            min_value = 0,
            step = 1)

        reps = st.number_input(
            label = rep_label,
            min_value = 0,
            step = 1)

        lift = st.selectbox(
            'Lift Type', ('Deadlift', 'Bench Press', 'Squat', 'Military Press'))
    elif attribute == 'Running':
        amt_label = 'Time'
        rep_label = 'Distance Ran (in miles)'
        lift = 'Running'

        amt = st.text_input(
            label = amt_label,
            )

        reps = st.number_input(
            label = rep_label,
            min_value = 0,
            step = 1)

    # Data Ingestion    
    ingestion = st.radio(
        'Ingestion', ['Set', 'Goal']
        )
    
    # Data Submission
    submit_button = st.button('Submit Data')

    # Package Data into JSON
    if submit_button:
        
        dt = str(datetime.now())
        
        if attribute == 'Lifts':
            orm = utils.normalize(amt, reps)
        else:
            orm = amt
        
        info = {
            'uid': uid,
            'datetime': dt,
            'attribute': attribute,
            'lift': lift,
            'amt': str(amt),
            'reps': reps,
            'orm': str(orm),
            'ingestion': ingestion
            }

        utils.submit_info(info)

        if info['attribute'] == 'Lifts' and info['ingestion'] == 'Set':
            utils.summary_graph(info)
            utils.weight_table(orm)
        else:
            pass

        #utils.print_log()

def goals():
    pass