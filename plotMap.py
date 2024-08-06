import streamlit as st
import numpy as np
import pandas as pd

mapData = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
    )

st.map(mapData)
