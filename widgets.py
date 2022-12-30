import streamlit as st 
import numpy as np
import pandas as pd 

st.write ("                     Widgets               ")
st.write("Widgets When you have got the data or model into the state that you want to explore, you can add in widgets like st.slider(), st.button() or st.selectbox(). It is really straightforward — treat widgets as variables:")

x = st.slider('x')
st.write(x, 'Squared is ', x*x)

st.write('Input Box')

st.write("Widget using st.text_input() and call st.session_state.name")
name = st.text_input("Your name:", key="name")

st.session_state.name

st.write("Widget using st.checkbox()")

if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b', 'c'])
    
    chart_data
    
st.write("Use a selectbox for options")
st.write("Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.")

df = pd.DataFrame({'column1' : [1,2,3,4], 'column2': [10,20,30,40]})
option = st.selectbox('Best number', df['column1'])
st.write('selected :' , option)





