'''
plots.py is exactly what it sounds like. It is used to put together any plot and each function should at least return a figure.
'''

import plotly.express as px
import streamlit as st

from datetime import datetime
from datetime import timedelta

def weight_track(data, user): # <- I want to add timeline as well
    '''
    Creates a plot based on the user (and eventually a time period)
    '''
    df = data[
        (data.user == user)
    ].copy()

    fig = px.scatter(
        data_frame = df, 
        x = "timestamp", 
        y ="wt_lb", 
        trendline="ols",
        title= f'{user} Weight Tracking',
        labels = {
            'timestamp': 'Date',
            'wt_lb': 'Weight (lbs)'
        }
    )
    fig.update_layout(yaxis_range=[df.wt_lb.min() - 10, df.wt_lb.max() + 10])
    return fig, px.get_trendline_results(fig).iloc[0]['px_fit_results'].params[-1]

def general_weight(data):
    '''
    Show the overall trends of all users
    '''
    df = data.copy()
    fig = px.scatter(
        data_frame = df, 
        x ="timestamp", 
        y ="wt_lb", 
        trendline ="ols",
        title = f'Weight Tracking',
        labels = {
            'timestamp': 'Date',
            'wt_lb': 'Weight (lbs)'
        },
        color = 'user'
    )
    fig.update_layout(yaxis_range=[df.wt_lb.min() - 20, df.wt_lb.max() + 10])
    return fig

def current_weight(data, user):
    '''
    Display day over day weight change for user (currently only in lbs)
    '''
    df = data[data.user == user].copy()
    df['date'] = [_.date() for _ in df.timestamp]
    today = df.date.max()
    prev_day = today - timedelta(days=1)

    lb_today = df[df.date == today]['wt_lb'].values[0]
    lb_prev = df[df.date == prev_day]['wt_lb'].values[0]
    lb_diff = round(lb_today - lb_prev, 2)

    st.write('Last updated ', str(today))
    st.metric('Day Over Day Weight Change (lbs)', lb_today, lb_diff, 'inverse')
