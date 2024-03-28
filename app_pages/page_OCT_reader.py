import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


def page_oct_reader_body():
    st.write("## OCT Analysis")
    st.info(f"The client requires an effective tool to determine"
        f" the medical condition of a macula based on a OCT scan."
        f"The client needs to distinguish amongst CNV, DME, DRUNSEN,"
        f" and healthy maculas."
    )

    st.write("---")

    images_buffer = st.file_uploader('Upload your OCT image',
                                     type='png',accept_multiple_files=True)