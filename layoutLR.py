import streamlit as st 

left_column, right_column = st.columns(2)
left_column.button('Press')

with right_column:
    chosen =  st.radio('sorting hat', ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write("You are in {chosen} house!")
