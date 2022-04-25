'''
views.py is essentially the "frontend" while utils is the "backend". Functions in views should mostly 
set up the layout of the application. Any other functionality can probably reside in utils or elsewhere
'''

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time

import streamlit as st

import utils
import plots
import format

def welcome():
    st.set_page_config(page_title='Trkkr',
                       page_icon=':muscle:',
                       layout='wide')
    st.title('Trkkr')

def user():
    df = utils.load_table()
    leaderboard = format.for_leaderboard(df)

    welcome_msg = st.empty()
    welcome_msg.write(f'### Welcome back, User!')

    # select user
    user = st.selectbox('Who is this?',
                        ('Select User',
                         'Ian McNair',
                         'Wayne Chim',
                         'Joyce Chan',
                         'Sideman Wu'))

    metric_ph = st.empty()
    graph_ph = st.empty()

    if user == 'Select User':
        st.subheader('Leaderboard')
        st.table(leaderboard)
        st.plotly_chart(plots.general_weight(df))
    else:
        fname = user.split()[0]
        welcome_msg.write(f'### Welcome back, {fname}!')

        with metric_ph.container():
            col1, col2, col3, col4 = st.columns(4)
            plots.day_over_day(df, user, col1)
            plots.moving_avg(df, user, col2)
            plots.first_weighin(df, user, col3)
            plots.leaderboard_pos(leaderboard, user, col4)
            plots.last_updated(df, user)

        try:
            fig, slope = plots.weight_track(df, user)
            st.caption(f'{user} is changing weight by {slope} pounds per day on average')
            with graph_ph.container():
                st.plotly_chart(fig)
        except:
            pass

    return user

def weight_form(user):
    df = utils.load_table()
    if user == 'Select User':
        pass
    else:
        with st.sidebar:
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
                    #dt = str(datetime.now() - timedelta(hours=4))
                    dt = str(datetime.now())

                    entry = {'timestamp': dt,
                             'user': user,
                             'wt_lb': lb,
                             'wt_kg': kg}

                    #st.json(entry)
                    utils.submit(entry, df)

def pushup_form(user):
    if user == 'Select User':
        pass
    else:
        with st.sidebar:
            with st.form('pushup_form', clear_on_submit=True):
                count = st.number_input(label='Push Ups',
                                        min_value = 0,
                                        step = 1)

                submit_button = st.form_submit_button('Submit Data')

                if submit_button:

                    dt = str(datetime.now() - timedelta(hours=4))

                    entry = {'timestamp': dt,
                            'user': user,
                            'count': count}

                    st.json(entry)

