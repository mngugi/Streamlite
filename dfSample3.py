import streamlit as st
import pandas as pd
import numpy as np

# Generate a random dataframe with 10 rows and 20 columns
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

# Use Streamlit to display the dataframe with highlighted maximum values in each column
st.dataframe(dataframe.style.highlight_max(axis=0))

st.map(dataframe)
