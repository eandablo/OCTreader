import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Specialists dedicated to OCT analysis are capable to distinguish certain in non-healthy macula images "
        f"when compare to healthy ones. Based on this, It is plaussible to assume that patterns might emerge in "
        f"OCT images that allow for automatic detection of macular anomalities using the appropriate techniques.  \n"
        f"Average Image, Variability Image and Difference between Averages studies did not reveal"
        f"any clear pattern to differentiate one from another."
    )