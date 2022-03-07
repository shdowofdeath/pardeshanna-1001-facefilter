import streamlit as st

import Source
from Source import *
from PIL import Image as Im


def get_image_data(file_uploaded):
    image_file = file_uploaded.read()
    st.image(image_file)
    image_file = Im.open(file_uploaded)
    resized_img = image_file.resize((400, 400))
    data = asarray(resized_img)
    return data, resized_img

def get_filters():
    st.write("\nChoose which filters you want")
    glasses_label = st.checkbox("Glasses")
    hat_label = st.checkbox("Hat")
    lips_label = st.checkbox("lips")

    filters = [False] * 3  # filters list. 0-glasses, 1-hat, 2-lips

    if (glasses_label):
        filters[0] = True
    if (lips_label):
        filters[1] = True
    if (hat_label):
        filters[2] = True

    return filters

def do_options(file_uploaded, options):
    filters = []
    if (options == "Edge Detection"):
        show_final_img(filters, file_uploaded, 0)

    elif (options == "Filters"):
        filters = get_filters()
        show_final_img(filters, file_uploaded, 1)


def show_final_img(filters, file_uploaded, is_filters):
    if (file_uploaded is not None):#uploaded file
        data, resized_img = get_image_data(file_uploaded)  # gets image as array data and resized image
        final_image = Source.run(data, resized_img, filters, is_filters)
        st.image(final_image)#shows image

def main():
    picture = st.checkbox("Take Picture")
    upload_image = st.checkbox("Upload Image")
    if(upload_image):#uploaded image
        options = st.selectbox("\nChoose an option: ", ("", "Edge Detection", "Filters"))
        file_uploaded = st.file_uploader("Upload your file PLEASE")
        do_options(file_uploaded, options)

    elif(picture):#take picture
        options = st.selectbox("\nChoose an option: ", ("", "Edge Detection", "Filters"))
        file_uploaded = st.camera_input("Camera")
        do_options(file_uploaded, options)

if __name__ == "__main__":
    main()