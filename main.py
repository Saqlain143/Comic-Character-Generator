import streamlit as st
import requests
import time
import os


API_TOKEN = "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" # Replace with your Hugging Face API token

st.markdown("<h1 style='text-align: center;'>COMIC CHARACTER GENERATOR</h1>", unsafe_allow_html=True)

with st.form("my_form", clear_on_submit=True):
    prompt = st.text_area("Enter your Prompt:")
    submit_button = st.form_submit_button(label="Generate Image")

if submit_button:
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
