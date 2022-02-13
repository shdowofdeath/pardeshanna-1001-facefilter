import streamlit as st

import Source
from Source import *
#from numpy import asarray
from PIL import Image as Im


picture = st.checkbox("Take Picture")
upload_image = st.checkbox("Upload Image")
range = st.slider('Range', 1, 30)
edges = st.slider('Edges', 0.01, 0.5)
vert_range = st.slider('Vertical Range', 1, 30)
horiz_range = st.slider('Horizontal Range', 1, 30)
const_nums.RANGE = range
const_nums.EDGES = edges
VERT_RANGE = vert_range
HORIZ_RANGE = horiz_range
if(picture):
    file_uploaded = st.camera_input("Camera")

    if (file_uploaded is not None):
        image_file = file_uploaded.read()
        st.image(image_file)
        # image_np = np.ndarray(image_file)
        # print(image_file)
        image_file = Im.open(file_uploaded)
        data = asarray(image_file)
        final_image = Source.main(data)
        butt = st.button("Detect Face")
        if (butt):
            st.image(final_image)
elif(upload_image):
    file_uploaded = st.file_uploader("Upload your file PLEASE")

    if (file_uploaded is not None):
        image_file = file_uploaded.read()
        st.image(image_file)
        # image_np = np.ndarray(image_file)
        # print(image_file)
        image_file = Im.open(file_uploaded)
        data = asarray(image_file)
        final_image = Source.main(data)
        # butt = st.button("Detect Face")
        # if (butt):
        st.image(final_image)