import streamlit as st
import pandas as pd
import utils

def welcome():
    st.write(f"# Trkker")
    st.write(f'## Welcome back user!')

def form():
    amt = 0
    reps = 0
    
    uid = st.selectbox(
        'Select your user',
        ('Ian', 'Gladys', 'Linda', 'Wayne', 'Rando')
    )
    measure = st.radio(
        'Measurement', [
            'Weight',
            'Bench Press', 
            'Deadlift',
            'Running'
        ])
    if measure == 'Running':
        amt_label = 'Distance Ran'
        rep_label = 'Time'
    else:
        amt_label = 'Amount (lbs):'
        rep_label = 'Reps (if applicable)'

    amt = st.number_input(
        label=amt_label,
        min_value = 0,
        step = 1
        )
    reps = st.number_input(
        label=rep_label,
        min_value = 0,
        step = 1
        )
    ingestion = st.radio('Ingestion', [
        'Set', 'Goal'
    ])
    
    submit_button = st.button('Submit Data')
    st.write(submit_button)
    if submit_button:
        utils.submit_info({
            'uid':uid, 
            'measurement': measure, 
            'amt':amt, 
            'reps': reps
        })