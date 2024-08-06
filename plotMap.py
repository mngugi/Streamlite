import streamlit as st
import numpy as np
import pandas as pd

mapData = pd.DataFrame(
    np.random.randn(2000, 2) / [30,30] + [30.86, -133.4],
    columns=['lat', 'lon']
    )

st.map(mapData)
