import streamlit as st
import time
from rembg import remove 
from PIL import Image
from io import BytesIO


# Setting up the App   
st.set_page_config(page_title="Background Removal App", page_icon=":tada:", layout="centered")

st.sidebar.markdown("<h1 style='text-align: center;'>BACKGROUND REMOVAL APP</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BACKGROUND REMOVAL APP</h1>", unsafe_allow_html=True)

with st.form("my_form", clear_on_submit=True):
    file_upload = st.file_uploader("Upload an image", type="png")
    submit_button = st.form_submit_button(label="Remove Background", use_container_width=True)

if submit_button:
    if submit_button:
        if file_upload is not None:
            st.markdown("<h3 style='text-align: center;'>Your Generated Image without Background:</h3>", unsafe_allow_html=True)

            if file_upload is not None:
                input_image = Image.open(file_upload)

                with st.spinner('Removing Background...'):
                    time.sleep(2)
                    output_image = remove(input_image)
                    buf = BytesIO()
                    output_image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    fixed_image = st.image(output_image, use_column_width=True, caption="Image without background")

                    if fixed_image:
                        fixed_button = st.download_button(label="Download Image", data=byte_im, file_name="image_no_bg.png", mime="image/png")

                        if fixed_button:
                            st.success('Done!')        

if submit_button and file_upload is None:
    st.warning("Please upload an image.")