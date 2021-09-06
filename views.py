import streamlit as st
import pandas as pd

def title():
    st.title("Testing the Local App")

def form():
    with st.form(key='my_form'):
        uid = st.text_input(label='User ID:')
        lift = st.radio('Lift', ['Bench Press', 'Deadlift'])
        weight_input = st.number_input(label='Weight (lbs):')
        rep_input = st.number_input(label='Reps:')
        ingestion = st.radio('Ingestion', ['Real-time', 'Historical'])
        submit_button = st.form_submit_button(label='Submit')