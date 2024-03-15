import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def data_image_visualiser_body():
    st.write('## OCT image visualiser')
    st.info('### Business Requirement 1'
        f'The client requires to understand visual differences between the different macular conditions and healthy maculas.'
    )