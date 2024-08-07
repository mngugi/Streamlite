import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['apples','bananas', 'oranges']
            )
    chart_data

    df = pd.DataFrame({'Col_1': [1,2,3,4,5],
                        'Col_2': [10,20,30,40,50]})

    option = st.selectbox( 'which number do you like better?',
      df['Col_1'])


    "You selected : ", option