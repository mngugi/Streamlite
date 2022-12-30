```python
# Streamlite

# Learning Streamlit library app!

import streamlit as st
import pandas as pd
import numpy as np
st.write('Create our first table of two columns')
df = pd.DataFrame({ 'Column1': [10,20,30,40,50], 'Column2' : [100,200,300,400,500]})
df
st.write("--------------------------------------------------------")
st.write("Example 1: This function uses st.write() alternative to pd.DataFrame")
st.write(pd.DataFrame({ 'Column3': [10,20,30,40,50], 'Column4' : [100,200,300,400,500]}))

st.write("--------------------------------------------------------")
st.write("Example 2: This function uses st.dataframe() method to draw an interactive table ")
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

st.write("--------------------------------------------------------")
st.write("Example 3: This function uses Styler object to highlight int some elements in the interactive table ")
df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))


st.write("--------------------------------------------------------")
st.write("Example 4: This function uses Streamlit also has a method for static table generation: st.table().")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.write("-------------------End.---------------------------")
```

a Streamlit app that demonstrates some of the features available for displaying data in a Streamlit app.

In example 1, you used the st.write() function to display a Pandas DataFrame. This is a simple way to display a DataFrame, but it is not interactive and does not allow the user to sort or filter the data.

In example 2, you used the st.dataframe() function to display an interactive table. This table allows the user to sort and filter the data, as well as resize and scroll through the table.

In example 3, you used the style attribute of a Pandas DataFrame to highlight the maximum value in each column of the DataFrame. The resulting DataFrame is then passed to the st.dataframe() function to display an interactive table.

In example 4, you used the st.table() function to display a static table. This table does not allow the user to interact with the data in any way, but it may be useful for displaying small amounts of data or for displaying data in a specific format.

Overall, Streamlit provides several options for displaying data in your app, allowing you to choose the best option for your needs.
