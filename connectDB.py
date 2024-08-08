import streamlit as st
import mysql.connector
import pandas as pd

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",       # Replace with your database host
    user="root",   # Replace with your database username
    password="#",  # Replace with your database password
    database="world_x"      # Replace with your database name
)

# Perform a query
query = "SELECT * FROM my_table"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the DataFrame in Streamlit
st.dataframe(df)
