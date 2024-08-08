import streamlit as st

add_selectbox = st.sidebar.selectbox('Select Contact mode', ('Email', 'Work phone', 'Cell Phone', ' Repository'))

add_slider = st.sidebar.slider('Select range of values', 0.0,100.0,(25.0,75.0))


