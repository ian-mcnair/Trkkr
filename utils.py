import pandas as pd
import numpy as np
import streamlit as st


def submit_info(info = []):
    is_weight = info['measurement'] == 'Weight'
    if is_weight:
        st.write(f'''{info['uid']} weighs {info['amt']}''')
    else:
        st.write(f'''{info['uid']} did {info['amt']} {info['reps']} times!''')