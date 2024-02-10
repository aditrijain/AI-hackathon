import streamlit as st

import pandas as pd

import numpy as np

import time

import os

st.title("hello")

# File uploader for image
image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# File uploader for PDF
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

# Text input
text_input = st.text_area("Enter Text")
if st.button("Submit"):
    # Call backend model with inputs
    backend_result = backend_model(image_file, pdf_file, text_input)

    # Display result
    st.subheader("Backend Model Output:")
    st.write(backend_result)
