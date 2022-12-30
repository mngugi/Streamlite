import streamlit as st
import pandas as pd
import numpy as np 

st.write("          Draw Charts and Maps ")
st.write(
'''
Draw charts and maps
Streamlit supports several popular data charting libraries like Matplotlib, Altair, deck.gl, and more. In this section, you'll add a bar chart, line chart, and a map to your app.
''')

st.write(" st.line_chart() method generates a random sample using numpy and then a chart ")
data = pd.DataFrame(np.random.randn(20,3), columns = ['a','b','c']) 
st.line_chart(data)

st.write('A map of Turkey using the st.map() method')

map_data = pd.DataFrame(
np.random.randn(1000,2) / [50,50] + [38, 30],
columns=['lat', 'lon'])

st.map(map_data)
