import pandas as pd
import numpy as np
#import plotly.express as px
import streamlit as st
import utils

def welcome():
    st.write(f"# Trkkr")
    st.write(f'## Welcome back, user!')

def form():
    amt = 0
    reps = 0
    lift = ''
    
    # User
    uid = st.selectbox(
        'Select your user',
        ('Ian', 'Gladys', 'Linda', 'Wayne', 'Rando')
    )

    # Attribute
    measure = st.radio(
        'Measurement', [
            'Body Weight',
            'Lifts',
            'Running'
        ])

    if measure == 'Running':
        amt_label = 'Distance Ran (in miles)'
        rep_label = 'Time'

        amt = st.number_input(
            label = amt_label,
            min_value = 0,
            step = 1
        )
        reps = st.number_input(
            label = rep_label,
            min_value = 0,
            step = 1
        )

    elif measure == 'Lifts':
        amt_label = 'Weight (lbs):'
        rep_label = 'Reps (if applicable)'

        lift = st.selectbox(
        'Lift Type',
        ('Bench Press', 'Squat', 'Deadlift', 'Military Press')
    )

        amt = st.number_input(
            label = amt_label,
            min_value = 0,
            step = 1
        )
        reps = st.number_input(
            label = rep_label,
            min_value = 0,
            step = 1
        )
    else:
        amt_label = 'Weight (lbs):'

        amt = st.number_input(
            label = amt_label,
            min_value = 0,
            step = 1
        )

    # Data Ingestion    
    ingestion = st.radio('Ingestion', [
        'Set', 'Goal'
    ])
    
    # Data Submission
    submit_button = st.button('Submit Data')
    st.write(submit_button)

    # Package Data into JSON
    if submit_button:

        entry = {
            'uid': uid,
            'lift': lift, 
            'measurement': measure, 
            'amt': amt, 
            'reps': reps,
            'ingestion': ingestion
        }

        utils.submit_info(entry)

        if entry['measurement'] == 'Lifts' and entry['ingestion'] == 'Set':
            orm = utils.normalize(entry['amt'], entry['reps'])
            utils.summary_graph(entry['measurement'], orm=orm)
            utils.weight_table(orm)
        elif entry['measurement'] == 'Running' and entry['ingestion'] == 'Set':
            utils.summary_graph(entry['measurement'], rep=entry['reps'])
        elif entry['measurement'] == 'Body Weight' and entry['ingestion'] == 'Set':
            utils.summary_graph(entry['measurement'], amt=entry['amt'])