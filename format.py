'''
format performs all the necessary formatting amd simplication including rounding and other

'''

import numpy as np
import pandas as pd
import streamlit as st

def for_datatable(main):
    main['timestamp'] = pd.to_datetime(main['timestamp'], infer_datetime_format=True)
    main['wt_lb'] = main['wt_lb'].astype(float)
    main['wt_kg'] = main['wt_kg'].astype(float)
    main['date'] = [_.date() for _ in main.timestamp]
    return main

def for_usertable(data, user):
    df = data[data.user == user].copy()
    return df

def for_leaderboard(data):
    _ = data.groupby('user')
    df = pd.concat([_.head(1), _.tail(1)]).sort_values('user').reset_index(drop=True).dropna()
    df['lb_pct'] = df.groupby('user')['wt_lb'].pct_change() * 100
    df['lb_pct'] = df['lb_pct'].round(2).astype('string') + '%'
    df['days_since'] = df.groupby('user')['date'].diff()
    df['days_since'] = df['days_since'].astype('string')

    leaderboard = df.groupby('user').tail(1).dropna(axis=0)[['user', 'lb_pct', 'days_since']].sort_values('lb_pct')
    leaderboard['elg'] = ['False' if int(_.split()[0]) == 0 else 'True' for _ in leaderboard['days_since']]
    leaderboard = leaderboard.sort_values('elg', ascending=False).reset_index(drop=True)
    leaderboard = leaderboard.drop(['elg'], axis=1)
    
    leaderboard.rename(columns={'user': 'User',
                                'lb_pct': '% Change',
                                'days_since': 'Days Since Start'},
                       inplace=True)
    leaderboard.index = leaderboard.index + 1
    #print(leaderboard)
    return leaderboard

def for_weight(uom, input):
    # uom - Unit of measure
    if uom == 'Pounds':
        lb = round(input, 2)
        kg = round(input/2.2, 2)
    elif uom == 'Kilograms':
        lb = round(input*2.2,2)
        kg = round(input,2)
    #print(f'{lb} pounds or {kg} kilograms')
    return lb, kg