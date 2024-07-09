import streamlit as st
from PIL import Image
from cnn import pred
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image has been uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
else:
    st.write("Please upload an image.")
st.write