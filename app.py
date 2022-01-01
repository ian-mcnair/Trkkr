'''
app.py should remain pretty minimal. It lays out the general flow of the app
'''

import pandas as pd
import streamlit as st
import views

views.welcome()
views.form()
views.goals()