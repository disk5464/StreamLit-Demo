import streamlit as st
import requests
import uuid
import json
import urllib.parse
import sys
import os
########################################################################
#This is the page title
st.title("Radio Refresher")

#Create a form so that we can get the ID without refreshing the page everytime.
with st.form("radio_form"):
    radio_id_input = st.text_input("Enter Radio ID or VIN:")
    submitted = st.form_submit_button("Submit")  # Enter also submits

#When the user hits the submit button, run the script. 
if submitted:
    #Take the radio ID and uppercase it. Also generate a UUID.
    radio_id_input = radio_id_input.upper() 
    uuid4 = str(uuid.uuid4())
    
    st.write(f"**Input (uppercased):** {radio_id_input}")
    st.write(f"**Generated UUID:** {uuid4}")
########################################################################

if len(radio_id_input) == 17:
    # VIN Activiation
    print("login")
    auth_token = login()
    print("versionControl")
    versionControl()
    print("getProperties")
    getProperties()
    print("update_1_vin")
    seq = update_1_vin()
    print("USDealerVehicleData")
    radio_id_result = USDealerVehicleData()
    if radio_id_result is None:
        sys.exit(1)
    radio_id_input = radio_id_result
    print("getCRM")
    getCRM()
    print("blocklist")
    blocklist()
    print("createAccount")
    createAccount()
    print("update_2")
    update_2()
elif len(radio_id_input) == 8 or len(radio_id_input) == 12:
    # Radio ID Activation
    print("login")
    auth_token = login()
    print("versionControl")
    versionControl()
    print("getProperties")
    getProperties()
    print("update_1")
    seq = update_1()
    print("getCRM")
    getCRM()
    print("blocklist")
    blocklist()
    print("createAccount")
    createAccount()
    print("update_2")
    update_2()
else:
    print("The VIN/Radio ID you entered is incorrect. Radio IDs are either 8 characters or 12 digits long and VINs are 17 characters long.")