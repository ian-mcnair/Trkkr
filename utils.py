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

import format

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

# Loading Data
pio.templates
#@st.cache(ttl=60, suppress_st_warning=True)
def load_table():
    values = sheet.get_all_values()
    main = pd.DataFrame(values[1:], columns=values[0])
    data_table = format.for_datatable(main)
    print(data_table.iloc[-1])
    return data_table

# Submit Form
def submit(entry, data):
    update = data.append(entry, ignore_index=True)
    gd.set_with_dataframe(sheet, update)

    with st.spinner('One moment...'):
        time.sleep(0.75)
        st.success("All done!")

    #return update