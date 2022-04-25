'''
app.py should remain pretty minimal. It lays out the general flow of the app
'''

import pandas as pd
import streamlit as st
import views

views.welcome()
user = views.user()
views.weight_form(user)
views.pushup_form(user)