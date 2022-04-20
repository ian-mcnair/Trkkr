'''
utils.py should only contain methods which perform approximately one function. Basically, if you need to refactor some complicated process
it will probably go into utils
'''

import pandas as pd
from datetime import datetime

import plotly.express as px
import plotly.io as pio
import streamlit as st
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread_dataframe as gd

# Setting up Google Sheets Connect
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
google_key_file = 'trkkr-343522-8d5890e74f07.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(google_key_file, scope)
gc = gspread.authorize(credentials)

spreadsheet_key = '1nAIsnqIm4qpaaFSqdog2zFfO39zfXip4LyvF9AbpYs8'
worksheet_name = 'main'

workbook = gc.open_by_key(spreadsheet_key)
sheet = workbook.worksheet(worksheet_name)
values = sheet.get_all_values()

main = pd.DataFrame(values[1:], columns=values[0])

# Converting Timestamp from String to Datetime
#main['timestamp'] = [datetime.strptime(timestamp, 'MM/dd/yyyy HH:mm:ss') for timestamp in main['timestamp']]
main['timestamp'] = pd.to_datetime(main['timestamp'], infer_datetime_format=True)
main['wt_lb'] = main['wt_lb'].astype(float)
main['wt_kg'] = main['wt_kg'].astype(float)

# Loading Data
pio.templates
@st.cache(ttl=600, suppress_st_warning=True)

def load_table():
    return main

# Submit Form
def submit(new_entry={}):
    update = main.append(new_entry, ignore_index=True)
    gd.set_with_dataframe(sheet, update)

    with st.spinner('One moment...'):
        time.sleep(1)
        st.success("All done!")
