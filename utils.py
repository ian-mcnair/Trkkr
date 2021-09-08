import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Data Submission
def submit_info(info = []):
    if info['measurement'] == 'Body Weight':
        st.write(f'''{info['uid']} weighs {info['amt']} pounds!''')
    elif info['measurement'] == 'Running':
        st.write(f'''{info['uid']} ran {info['amt']} miles in {info['reps']} minutes!''')
    else:
        st.write(f'''{info['uid']} lifted {info['amt']} pounds {info['reps']} times for {info['lift']}!''')

# Calculating ORM for Lifts
def normalize(amt, reps):
    if reps == 1:
        orm = amt
    else:
        orm = round(amt*(1+(0.0333*reps)), 2)
    return orm

# Populate table with work out set suggestions
def weight_table(orm):
    st.write(f'''User has a one-rep max of {orm} pounds!''')

    tbl = pd.DataFrame(columns={'% of ORM', 'Actual Weight (lbs)', 'Reps'})
    tbl = tbl[['% of ORM', 'Actual Weight (lbs)', 'Reps']]

    pct = []
    wt = []
    rp = [1, 2, 4, 6, 8, 10, 12, 16, 20, 24, 30]

    for i in range(100, 45, -5):
        pct.append(str(i) + '%')
        wt.append(round(i/100*orm,2))
    
    tbl['% of ORM'] = pct
    tbl['Actual Weight (lbs)'] = wt
    tbl['Reps'] = rp

    st.table(tbl)

# Summarize user performance over time
def summary_graph(measurement, amt=0, rep=0, orm=0):
    # Dummy data
    days = ['1', '2', '3']

    if measurement == 'Lifts':
        wt = [135, 225]

        wt.append(orm)

        fig = px.line(x=days, y=wt, title='User Lifts Performance Summary')
    elif measurement == 'Running':
        # Should be standardized to per mile
        time = [10, 8]

        time.append(rep)

        fig = px.line(x=days, y=time, title='User Runs Performance Summary')
    else:
        bd = [1.5*amt, 1.2*amt]

        bd.append(amt)

        fig = px.line(x=days, y=bd, title='User Body Weight Summary')
        
    st.plotly_chart(fig, use_container_width=True)

# Export data to Google Sheet
def export_info(info=[]):
    pass