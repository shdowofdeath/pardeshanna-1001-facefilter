import streamlit as st

import Source
from Source import *
#from numpy import asarray
from PIL import Image as Im


picture = st.checkbox("Take Picture")
upload_image = st.checkbox("Upload Image")
# range = st.slider('Range', 1, 30)
# edges = st.slider('Edges', 0.01, 0.5)
# vert_range = st.slider('Vertical Range', 1, 60)
# horiz_range = st.slider('Horizontal Range', 1, 60)
# const_nums.RANGE = range
# const_nums.EDGES = edges
# const_nums.VERT_RANGE = vert_range
# const_nums.HORIZ_RANGE = horiz_range
if(picture):
    file_uploaded = st.camera_input("Camera")

    if (file_uploaded is not None):
        image_file = file_uploaded.read()
        st.image(image_file)
        # image_np = np.ndarray(image_file)
        # print(image_file)
        image_file = Im.open(file_uploaded).convert("RGBA")
        data = asarray(image_file)
        final_image = Source.main(data)
        butt = st.button("Detect Face")
        if (butt):
            st.image(final_image)

elif(upload_image):

    st.write("\nChoose:")
    edge_check = st.checkbox("Edge Detection")
    filters_check = st.checkbox("Filters")

    if(edge_check):
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

    elif(filters_check):
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