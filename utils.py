import pandas as pd
import numpy as np
import streamlit as st


def submit_info(info = []):
    if info['measurement'] == 'Weight':
        st.write(f'''{info['uid']} weighs {info['amt']}''')
    elif info['measurement'] == 'Running':
        st.write(f'''{info['uid']} ran {info['amt']} miles in {info['reps']} minutes''')
    else:
        st.write(f'''{info['uid']} did {info['amt']} {info['reps']} times!''')