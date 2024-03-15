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
    st.write('## OCT Image Visualiser')
    st.info('### Business Requirement 1  \n'
        f'The client requires to understand visual differences between the different macular conditions and healthy maculas.  \n'
    )

    version = 'v1'
    output_path = f'outputs/{version}'
    if st.checkbox("Image average and variability for different macular conditions \n"):
      
      avg_normal = plt.imread(f"{output_path}/NORMAL_mean_std.png")
      avg_CNV = plt.imread(f"{output_path}/CNV_mean_std.png")
      avg_DME = plt.imread(f"{output_path}/DME_mean_std.png")
      avg_drusen = plt.imread(f"{output_path}/DRUSEN_mean_std.png")

      st.image(avg_normal, caption='Average and Variability of OCT images for Normal Macula')
      st.image(avg_CNV, caption='Average and Variability of OCT images for macula presenting CNV')
      st.image(avg_DME, caption='Average and Variability of OCT images for presenting DME')
      st.image(avg_drusen, caption='Average and Variability of OCT images for macula presenting Drussen')
      st.write("---")

    if st.checkbox("Aritmethic difference between pair of average iamges for macular conditions \n"):
        conditions = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
        for i in range(len(conditions)-1):
            for j in range(i+1, len(conditions)):
                image_path = f'{output_path}/{conditions[i]}_{conditions[j]}_diff.png'
                img = plt.imread(image_path)
                st.image(img, caption=f'Average image difference between {conditions[i]} and {conditions[j]}')