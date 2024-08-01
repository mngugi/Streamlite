import streamlit as st
import pandas as pd

st.write("Sample Table for a 3 X 6 matrix solution")
st.write(pd.DataFrame({
'Name' : ("Tom","Curt","Dog","Piet","Man","Honk"),
'x' : [56, 58, 54, 60, 64,65],
'y' : [1, 2, 3, 4, 5,65]

}))

