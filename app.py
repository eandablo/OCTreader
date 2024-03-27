import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_introduction import page_introduction_body
from app_pages.page_data_image_visualiser import data_image_visualiser_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body

app = MultiPage(app_name="OCT macular inspector")


app.add_page("Quick Project Summary", page_introduction_body)
app.add_page("OCT Image Visualiser", data_image_visualiser_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.run()