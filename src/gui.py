from io import StringIO
import streamlit as st
import random
from time import sleep
from start_conversation import start_conversation
from backend import prep_chain
st.set_page_config(page_title = 'MediMind🧠', page_icon="🧠", layout="wide")


patient_info = ""


# Setup the headers
st.header('MediMind🧠')
st.subheader('Patient Information')
uploaded_file = st.file_uploader('Enter patient history file.', type=['txt'])

if uploaded_file is not None:
    # To read file as bytes:
    patient_info = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

st.sidebar.button('Start Conversation', use_container_width=True, on_click=start_conversation, args=[patient_info,])

st.sidebar.button('Stop', use_container_width=True, on_click=st.stop)



