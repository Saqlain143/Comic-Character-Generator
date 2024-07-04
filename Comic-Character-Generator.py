# Importing Required Modules 
import streamlit as st
import requests
import time
import os
from rembg import remove 
from PIL import Image
from io import BytesIO

# Setting up the App   
st.set_page_config(page_title="Comic Character Generator", page_icon=":tada:", layout="centered")

st.sidebar.markdown("<h1 style='text-align: center;'>COMIC CHARACTER GENERATOR</h1>", unsafe_allow_html=True)


API_TOKEN = st.secrets["api_token"] # Replace with your Hugging Face API token

st.markdown("<h1 style='text-align: center;'>COMIC CHARACTER GENERATOR</h1>", unsafe_allow_html=True)

with st.form("my_form", clear_on_submit=True):
    prompt = st.text_area("Enter your Prompt:")
    col1, col2, col3 = st.columns(3)
    submit_button = col2.form_submit_button(label="Generate Image", use_container_width=True)

if submit_button and prompt != "":
    st.markdown("<h3 style='text-align: center;'>Your Generated Image:</h3>", unsafe_allow_html=True)

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer " + API_TOKEN}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": prompt,
    })

    with st.spinner('Generating Image...'):
        time.sleep(2)
        generated_image = st.image(image_bytes, use_column_width=True, caption=prompt)

    st.success('Done!')
    
    if generated_image:
        st.download_button(label="Download Image", data=image_bytes, file_name="image.png", mime="image/png")

if submit_button and prompt == "":
    st.warning("Please enter a prompt.")