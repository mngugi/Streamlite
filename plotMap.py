import streamlit as st
import numpy as np
import pandas as pd

mapData = pd.DataFrame(
    np.random.randn(1000, 2) / [30,50] + [30.76, -233.4],
    columns=['lat', 'lon']
    )

st.map(mapData)
