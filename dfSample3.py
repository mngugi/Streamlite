import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
np.random.randn(10,20),
columns = ('col %d' % i for i in range(20)))

st.table(dataframe)

)
