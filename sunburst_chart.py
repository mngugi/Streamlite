import streamlit as st
import plotly.express as px
import pandas as pd

# Data
data = {
    'userName': ["Angel", "Ben", "Cat", "Dougie", "Eve", "Father", "Gloria"],
    'Value': [10, 15, 9, 18, 20, 10, 13],
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)
st.write("### Data Table")
st.dataframe(df)

# Create a sunburst chart using Plotly
fig = px.sunburst(df, path=['userName'], values='Value')

# Update the layout of the figure
st.write("### Sunburst Chart")

# Display the sunburst chart in Streamlit
st.plotly_chart(fig)
