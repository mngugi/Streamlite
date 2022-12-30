# Learning Streamlit library app!

import streamlit as st
import pandas as pd
import numpy as np
st.write('Create our first table of two columns')
df = pd.DataFrame({ 'Column1': [10,20,30,40,50], 'Column2' : [100,200,300,400,500]})
df
st.write("--------------------------------------------------------")
st.write("Example 1: This function uses st.write() alternative to pd.DataFrame")
st.write(pd.DataFrame({ 'Column3': [10,20,30,40,50], 'Column4' : [100,200,300,400,500]}))

st.write("--------------------------------------------------------")
st.write("Example 2: This function uses st.dataframe() method to draw an interactive table ")
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

st.write("--------------------------------------------------------")
st.write("Example 3: This function uses Styler object to highlight int some elements in the interactive table ")
df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))


st.write("--------------------------------------------------------")
st.write("Example 4: This function uses Streamlit also has a method for static table generation: st.table().")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.write("-------------------End.---------------------------")
