'''
utils.py should only contain methods which perform approximately one function. Basically, if you need to refactor some complicated process
it will probably go into utils
'''

import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.io as pio
import streamlit as st
from gsheetsdb import connect

pio.templates

conn = connect()
sheet_url = st.secrets['public_gsheets_url']

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

def build_table():
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    df = pd.DataFrame(columns=['timestamp', 'user', 'wt_lb', 'wt_kg'])
    for row in rows:
        _ = pd.DataFrame([[row.timestamp, row.user, row.wt_lb, row.wt_kg]],
                         columns=['timestamp', 'user', 'wt_lb', 'wt_kg'])
        df = df.append(_, ignore_index=True)
    return df


# Data Submission
#@st.cache(suppress_st_warning=True)
def submit_info(info = []):
    df = pd.read_csv('dummy.csv')


    #fname = users_ls[str(info['uid'])]

    #if info['attribute'] == 'Body Weight':
    #    st.write(f'''{fname} weighs {info['amt']} pounds!''')

    #elif info['attribute'] == 'Running':
    #    st.write(f'''{fname} ran {info['reps']} miles in {info['amt']} minutes!''')
    
    #elif info['attribute'] == 'Lifts':
    #    st.write(f'''{fname} lifted {info['amt']} pounds {info['reps']} times for {info['lift']}!''')
    
    df = df.append(info, ignore_index=True)
    #df.to_csv('dummy.csv', index=False)
    st.table(df)

# Calculating ORM for Lifts
# def normalize(amt, reps):
#     if reps == 1:
#         orm = amt
#     else:
#         orm = round(amt*(1+(0.0333*reps)), 2)

#     return orm

# Convert to actionable weights to use in the gym
# def gym_convert(wt, pct=1):
#     #adjusted_orm = 0.9*orm

#     cur_total_wt = pct*wt

#     side_wt = (cur_total_wt - 45)/2

#     if side_wt % 5.0 > side_wt % 10.0:
#         side_wt = side_wt - side_wt % 10.0
#     else:
#         side_wt = side_wt - side_wt % 5.0
#     side_wt = round(side_wt, 0)

#     gym_total_wt = side_wt*2 + 45

#     set_up = {'Gym Wt': gym_total_wt,
#               'Side Wt': side_wt}

#     return set_up

# Populate table with work out set suggestions
# def weight_table(orm):
#     st.write(f'''User has a one-rep max of {orm} pounds!''')

#     tbl = pd.read_csv('wt_table.csv')

#     pct_ls = [] 

#     for i in tbl['% of ORM']:
#         pct = float(i.strip('%'))/100
#         pct_ls.append(pct)

#     tbl['Actual Wt (lbs)'] = np.array(pct_ls) * orm
#     tbl['Gym Wt (lbs)'] = [gym_convert(wt)['Gym Wt'] for wt in tbl['Actual Wt (lbs)']]
#     tbl['Wt to Put On (lbs)'] = [gym_convert(wt)['Side Wt'] for wt in tbl['Actual Wt (lbs)']]

#     st.table(tbl)

# Summarize user performance over time
# def summary_graph(info=[]):
#     df = pd.read_csv('dummy.csv')
#     df = df.append(info, ignore_index=True)
#     set_df = df[(df['lift'] == info['lift']) & (df['ingestion'] == 'Set')].reset_index()
#     goal = int(df[(df['lift'] == info['lift']) & (df['ingestion'] == 'Goal')]['orm'])
#     fig = px.line(set_df,
#                   x=(set_df.index+1).astype(str),
#                   y='orm',
#                   title='User Performance Summary',
#                   labels={'x': 'Days',
#                           'orm': ''})
#     fig.add_hline(y=goal, line_color='lightgrey', line_dash='dash')
#     fig.add_hrect(y0=goal-5, y1=goal+5, line_width=0, fillcolor='yellow', opacity=0.2)

#     st.plotly_chart(fig)

# Export data to Google Sheet
def export_info(info=[]):
    pass