import streamlit as st


n = st.slider('n')
st.write(n, "Squared is:", n*n)

st.text_input("Enter Name: ", key="name")

st.session_state.name



