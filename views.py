'''
views.py is essentially the "frontend" while utils is the "backend". Functions in views should mostly 
set up the layout of the application. Any othe rfunctionality can probably reside in utils or elsewhere
'''

import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
#import streamlit_authenticator as stauth
import utils
import time
import plots


def welcome():
    st.write(f"# Trkkr")

def form():
    amt = np.empty(1)
    reps = np.empty(1)
    lift = ''
    
    df = utils.build_table()

    # User
    t = st.empty()
    t.write(f'### Welcome back, User!')

    
    name = st.selectbox(
        'Who is this?',
        ('Select User', 'Ian McNair', 'Wayne Chim')
    )

    chart = st.empty()

    if name == 'Select User':
        # Wayne, please delete if you think it is unneeded -----------------------------
        # user_ls = df.user.value_counts().index.tolist()
        # user_df = pd.DataFrame()
        # for u_name in user_ls:
        #     u_wt = df[df.user==u_name].wt_lb.tolist()
        #     user_df[u_name] = u_wt
        st.plotly_chart(plots.general_weight(df))       
        

    else:
        fname = name.split()[0]
        t.write(f'### Welcome back, {fname}!')
        # Wayne, please delete the below if you think it is unneeded --------------------
        # u_df = df[df.user == name]
        # u_df = u_df.reset_index()
        # chart.line_chart(u_df['wt_lb'])
        fig, slope = plots.weight(df, name)
        st.plotly_chart(fig)
        st.write(f'{name} is changing weight by {round(slope, 2)} per day on average')

    # WE SHOULD DEF PUSH THIS (below) INTO ANOTHER FUNCTIONS MAYBE???
    # LIKE A FORMATTING.PY FILE???? 
    # Just seems like a lot happening and its hard to read/follow at a glance.
    
    # Attribute
    
    attribute = st.radio(
        'Attribute', ['Body Weight']
    )

    if attribute == 'Body Weight':
        amt_label = 'Weight'
        lift = 'Body Weight'
        #reps = 1

        amt = st.number_input(
            label = amt_label,
            min_value = 0.0,
            step = 0.1)

    # metric
    metric = st.radio(
        'Metric', ['Pounds', 'Kilograms']
    )

    if metric == 'Pounds':
        lb = round(amt,2)
        kg = round(amt/2.2,2)
        st.write(f'{lb} lb or {kg} kg')
    elif metric == 'Kilograms':
        lb = round(amt*2.2,2)
        kg = round(amt,2)
        st.write(f'{lb} lb or {kg} kg')

    '''elif attribute == 'Lifts':
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
            step = 1)'''

    # Data Ingestion    
    '''ingestion = st.radio(
        'Ingestion', ['Set', 'Goal']
        )'''
    
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
        
        with st.spinner('One moment...'):
            time.sleep(1)
            st.success("All done!")

        st.json(entry)
        #utils.submit_info(entry)

    '''if submit_button:
        
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

        #utils.print_log()'''

def goals():
    pass