'''
plots.py is exactly what it sounds like. It is used to put together any plot and each function should at least return a figure.
'''

from nntplib import decode_header
import plotly.express as px
import streamlit as st

from datetime import datetime
from datetime import timedelta

import format

def weight_track(data, user): # <- I want to add timeline as well
    '''
    Creates a plot based on the user (and eventually a time period)
    '''
    df = data[(data.user == user)].copy()
    
    if len(df) > 0:
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

        try:
            slope = px.get_trendline_results(fig).iloc[0]['px_fit_results'].params[-1]
            slope = round(slope, 2)
        except:
            slope = 0
        
        st.write(f'{user} is changing weight by {slope} pounds per day on average')
        return fig, slope

    else:
        st.write('### User has no data, submit an entry to create your graph!')
        return None, None

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

def last_updated(data, user):
    df = format.for_usertable(data, user)
    if len(df) == 0:
        pass
    else:
        today = df.date.max()
        st.write('Last updated ', str(today))

def day_over_day(data, user, loc):
    '''
    Display day over day weight change for user (currently only in lbs)
    '''

    df = format.for_usertable(data, user)
    label = 'Day Over Day Weight Change (lbs)'

    if len(df) == 0:
        lb_today = 'N/A'
        lb_diff = 0.0
        delta_color = 'off'
    else:
        today = df.date.max()
        lb_today = df[df.date == today]['wt_lb'].values[0]

        if len(df) >= 2:
            prev_day = df[df.date.argsort() == len(df) - 2].date.values[0]
            lb_prev = df[df.date == prev_day]['wt_lb'].values[0]
            lb_diff = round(lb_today - lb_prev, 2)
            delta_color = 'inverse'
        else:
            lb_diff = 0.0
            delta_color = 'off'
    
    loc.metric(label, lb_today, lb_diff, delta_color)

def moving_avg(data, user, loc):
    '''
    Display 5-day moving average change for user (currently only in lbs)
    '''

    df = format.for_usertable(data, user)
    label = '5-Day Moving Average (lbs)'

    if len(df) == 0 or len(df) < 5:
        lb_5dma = 'N/A'
        lb_diff = 0.0
        delta_color = 'off'
    elif len(df) >= 5:
        today = df.date.max()
        lb_today = df[df.date == today]['wt_lb'].values[0]

        lb_5dma = df.sort_values(by='date')[-5:]['wt_lb'].mean()
        lb_5dma = round(lb_5dma, 2)
        lb_diff = round(lb_today - lb_5dma, 2)
        delta_color = 'inverse'

    loc.metric(label, lb_5dma, lb_diff, delta_color)

def first_weighin(data, user, loc):
    '''
    Display first weigh in for user and compare to most recent weigh in (currently only in lbs)
    '''

    df = format.for_usertable(data, user)
    label = 'First Weigh-In (lbs)'

    if len(df) == 0:
        lb_first = 'N/A'
        lb_diff = 0.0
        delta_color = 'off'
    else:
        today = df.date.max()
        lb_today = df[df.date == today]['wt_lb'].values[0]
        lb_first = df.sort_values(by='date', ignore_index=True)[:1]['wt_lb'].values[0]

        if len(df) > 1:
            lb_diff = round(lb_today - lb_first, 2)
            delta_color = 'inverse'
        else:
            lb_diff = 0.0
            delta_color = 'off'
    
    loc.metric(label, lb_first, lb_diff, delta_color)

def leaderboard_pos(data, user, loc):
    '''
    Display user current position on leaderboard
    '''
    
    df = data[data.User == user]
    label = 'Leaderboard Position'

    if len(df) == 0:
        pos = 'N/A'
    else:
        days_since = int(df['Days Since Start'].values[0].split()[0])

        if days_since == 0:
            pos = 'N/A'
        else:
            pos = data[data.User == user].index.values[0]
    
    loc.metric(label, pos)
    

