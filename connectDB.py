import streamlit as st

conn = st.connection("world_x.sql")
df = conn.query("select * from my_table")
st.dataframe(df)