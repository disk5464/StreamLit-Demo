import streamlit as st
import requests
import uuid
import json
import urllib.parse
import sys
import os
########################################################################
st.write("Hello World")
text = st.text_input("Type something:")
if text:
    st.write("You wrote:", text)
########################################################################
radio_id_input = input("Enter Radio ID or VIN: ").upper()
uuid4 = str(uuid.uuid4())
print(uuid4)
