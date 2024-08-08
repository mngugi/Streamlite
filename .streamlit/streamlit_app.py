# streamlit_app.py

import streamlit as st

conn = st.experimental_connection('pets_db', type='sql')
