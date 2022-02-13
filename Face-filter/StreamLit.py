import streamlit as st

import Source
from Source import *
#from numpy import asarray
from PIL import Image as Im

file_uploaded = st.file_uploader("Upload your file PLEASE")
# st.write("We are goign to take a picture so be ready and put odem :)")
# file_uploaded = st.camera_input("CAM")
if(file_uploaded is not None):
    image_file = file_uploaded.read()
    st.image(image_file)
    #image_np = np.ndarray(image_file)
    #print(image_file)
    image_file = Im.open(file_uploaded)
    data = asarray(image_file)
    final_image = Source.main(data)
    butt = st.button("Detect Face")
    if(butt):
        st.image(final_image)