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

    if st.checkbox("Image average and variability for different macular conditions \n"):
      
      avg_normal = plt.imread(f"outputs/{version}/model_training_acc.png")
      avg_CNV = plt.imread(f"outputs/{version}/model_training_losses.png")
      avg_DME = plt.imread(f"outputs/{version}/model_training_acc.png")
      avg_drussen = plt.imread(f"outputs/{version}/model_training_losses.png")

      st.image(avg_normal, caption='Average and Variability of OCT images for Normal Macula')
      st.image(avg_CNV, caption='Average and Variability of OCT images for macula presenting CNV')
      st.image(avg_DME, caption='Average and Variability of OCT images for presenting DME')
      st.image(avg_drussen, caption='Average and Variability of OCT images for macula presenting Drussen')
      st.write("---")