import streamlit as st
import pandas as pd
import utils

def welcome():
    st.write(f"# Trkker")
    st.write(f'## Welcome back user!')

def form():
    with st.form(key='my_form'):
        uid = st.selectbox(
            'Select your user',
            ('Ian', 'Gladys', 'Linda', 'Wayne', 'Rando')
        )
        measure = st.radio(
            'Measurement', [
                'Weight',
                'Bench Press', 
                'Deadlift'
            ])
        amt = st.number_input(
            label='Amount (lbs):',
            min_value = 0,
            step = 1
            )
        reps = st.number_input(
            label='Reps (if applicable):',
            min_value = 0,
            step = 1
            )
        #ingestion = st.radio('Ingestion', ['Real-time', 'Historical'])
        submission = st.form_submit_button(label='Submit')
        utils.submit_info({
            'uid':uid, 
            'measurement': measure, 
            'amt':amt, 
            'reps': reps
        })