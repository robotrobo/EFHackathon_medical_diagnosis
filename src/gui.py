from io import StringIO
import streamlit as st
import random
from time import sleep
from start_conversation import start_conversation
from backend import prep_chain
from streamlit_elements import elements, mui, html


st.set_page_config(page_title = 'gnosis🧠', page_icon="🧠", layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

patient_info = ""


# Setup the headers
st.header('Gnosis 🧠')
st.subheader('Patient Information')
uploaded_file = st.file_uploader('Enter patient history file.', type=['txt'])
st.divider()
st.subheader("About Me")
st.markdown("""<p class="big-font">🤖 I'm an AI-powered diagnosis assistant, <b>Gnosis</b>(Greek for knowledge), and my job is to help doctors and patients with diagnosing and reporting medical information.<br>
🤓 I'm trained on 1000s of medical diagnoses. I can find the most optimal way for a doctor to diagnose a patient.<br>
🎤 I listen in on doctor-patient conversations and use speech-to-text technology to create a transcript of what's being said. I then analyze this transcript using cutting-edge language models to generate a diagnosis report.<br>
📝 This report takes. I'm designed to be transparent and to not provide information that I'm not confident about.</p>"""
, unsafe_allow_html=True)



if uploaded_file is not None:
    # To read file as bytes:
    patient_info = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

st.sidebar.button('Start Conversation', use_container_width=True, on_click=start_conversation, args=[patient_info,])

stop_button = st.sidebar.button('Stop', use_container_width=True, )

if stop_button:
    st.experimental_rerun()

