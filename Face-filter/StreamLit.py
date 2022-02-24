import streamlit as st

import Source
from Source import *
from PIL import Image as Im

picture = st.checkbox("Take Picture")
upload_image = st.checkbox("Upload Image")

if(picture):
    file_uploaded = st.camera_input("Camera")

    if (file_uploaded is not None):
        image_file = file_uploaded.read()
        st.image(image_file)
        image_file = Im.open(file_uploaded).convert("RGBA")
        data = asarray(image_file)
        final_image = Source.main(data)
        butt = st.button("Detect Face")
        if (butt):
            st.image(final_image)

elif(upload_image):

    options = st.selectbox("\nChoose an option: ", ("", "Edge Detection", "Filters"))

    if(options == "Edge Detection"):
        file_uploaded = st.file_uploader("Upload your file PLEASE")
        filters = []

        if (file_uploaded is not None):
            image_file = file_uploaded.read()
            st.image(image_file)
            image_file = Im.open(file_uploaded)
            resized_img = image_file.resize((400, 400))
            data = asarray(resized_img)
            final_image = Source.main(data, resized_img, filters, 0)
            st.image(final_image)

    elif(options == "Filters"):
        st.write("\nChoose which filters you want")
        glasses_label = st.checkbox("Glasses")
        hat_label = st.checkbox("Hat")
        lips_label = st.checkbox("lips")

        filters = [False]*3 #filters list. 0-glasses, 1-hat, 2-lips

        if(glasses_label):
            filters[0] = True
        if (lips_label):
            filters[1] = True
        if (hat_label):
            filters[2] = True

        file_uploaded = st.file_uploader("Upload your file PLEASE")

        if (file_uploaded is not None):
            image_file = file_uploaded.read()
            st.image(image_file)
            image_file = Im.open(file_uploaded)
            resized_img = image_file.resize((400, 400))
            data = asarray(resized_img)
            final_image = Source.main(data, resized_img, filters, 1)
            st.image(final_image)