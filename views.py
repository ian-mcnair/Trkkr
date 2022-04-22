'''
views.py is essentially the "frontend" while utils is the "backend". Functions in views should mostly 
set up the layout of the application. Any other functionality can probably reside in utils or elsewhere
'''

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

import streamlit as st

import utils
import plots
import format

def welcome():
    st.set_page_config(page_title='Trkkr',
                       page_icon=':muscle:',
                       layout='wide')
    st.write(f"# Trkkr")

def form():
    df = utils.load_table()
    leaderboard = format.for_leaderboard(df)

    # User
    welcome_msg = st.empty()
    welcome_msg.write(f'### Welcome back, User!')

    name = st.selectbox(
        'Who is this?',
        ('Select User', 'Ian McNair', 'Wayne Chim')
    )

    if name == 'Select User':
        st.write('###### Leaderboard')
        st.table(leaderboard)
        st.plotly_chart(plots.general_weight(df))
    else:
        fname = name.split()[0]
        welcome_msg.write(f'### Welcome back, {fname}!')

        col1, col2, col3, col4 = st.columns(4)

        dod_label, dod_value, dod_delta, dod_delta_color = plots.day_over_day(df, name)
        col1.metric(dod_label, dod_value, dod_delta, dod_delta_color)
        
        ma_label, ma_value, ma_delta, ma_delta_color = plots.moving_avg(df, name)
        col2.metric(ma_label, ma_value, ma_delta, ma_delta_color)
        
        fw_label, fw_value, fw_delta, fw_delta_color = plots.first_weighin(df, name)
        col3.metric(fw_label, fw_value, fw_delta, fw_delta_color)
        
        lb_label, lb_value = plots.leaderboard_pos(leaderboard, name)
        col4.metric(lb_label, lb_value)
        
        plots.last_updated(df, name)

        fig, slope = plots.weight_track(df, name)
        st.plotly_chart(fig)

        with st.form('weight_form', clear_on_submit=True):
            # Input fields
            weight = st.number_input(label = 'Weight',
                                    min_value = 0.0,
                                    step = 0.1)

            # Unit of Measure
            uom = st.radio('Unit of Measure',
                        ['Pounds', 'Kilograms'])   

            if weight > 0:
                lb, kg = format.for_weight(uom, weight)
            
            # Data Submission
            submit_button = st.form_submit_button('Submit Data')

            # Package Data into JSON
            if submit_button:
                dt = str(datetime.now() - timedelta(hours=4))

                entry = {'timestamp': dt,
                        'user': name,
                        'wt_lb': lb,
                        'wt_kg': kg}

                utils.submit(entry)

def leaderboard():
    pass