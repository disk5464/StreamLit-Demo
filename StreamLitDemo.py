import streamlit as st
import requests
import uuid
import json
import urllib.parse
import sys
import os
########################################################################
#This is the page title
st.title("Radio ID Refresher")

#Create a form so that we can get the ID without refreshing the page everytime.
with st.form("radio_form"):
    radio_id_input = st.text_input("Enter Radio ID or VIN:")
    submitted = st.form_submit_button("Submit")  # Enter also submits

#When the user hits the submit button, run the script. 
if submitted:
    radio_id_input = radio_id_input.upper()  # same place in flow as your original
    uuid4 = str(uuid.uuid4())
    st.write(f"**Input (uppercased):** {radio_id_input}")
    st.write(f"**Generated UUID:** {uuid4}")
########################################################################