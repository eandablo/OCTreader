import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_introduction import page_introduction_body

app = MultiPage(app_name="OCT macular inspector")


app.add_page("Quick Project Summary", page_summary_body)

app.run()