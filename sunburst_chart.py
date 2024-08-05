import plotly.express as px
import streamlit as st
import pandas as pd

data = {
    'userName': [ "Angel", "Ben", "Cat", "Dougie", "Eve", "Father", "Gloria"],
    'Value': [10,15,9,18,20,10,13],

         }
df = pd.DataFrame(data)
figure = px.sunburst(data, names = 'userName', values= 'Value')

figure.update_layout(title_text= "Sunburst Chart ")

st.plotly_chart(figure)