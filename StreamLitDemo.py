import streamlit as st

st.write("Hello World")
text = st.text_input("Type something:")
if text:
    st.write("You wrote:", text)