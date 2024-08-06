import streamlit as st
import numpy as np
import pandas as pd

mapData = pd.DataFrame(
    np.random.randn(4000, 2) / [31, 115] + [-31.974162, 115.896377],


    columns=['lat', 'lon']
    )

st.map(mapData)
