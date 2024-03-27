import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def image_collage_per_label(label, nrows, ncols, img_height, img_width):
    '''
    Function creates a collage of images from the train folder
    using for a specific label
    '''
    print(f'{label} Images')
    n_images = nrows * ncols
    images_label = os.listdir('inputs/OCTdata/val/' + label)
    random.shuffle(images_label)
    images_list = images_label[0: n_images]
    position_list = list(itertools.product(range(nrows), range(ncols)))
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(img_height, img_width))
    count = 0
    for image_name in images_list:
        img = imread('inputs/OCTdata/val/' + label + '/' + image_name)
        axes[position_list[count][0], position_list[count][1]].imshow(img)
        axes[position_list[count][0], position_list[count][1]].set_xticks([])
        axes[position_list[count][0], position_list[count][1]].set_yticks([])
        count += 1
    
    plt.tight_layout()
    st.pyplot(fig=fig)


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

    if st.checkbox("OCT Images motage \n"):
        st.write('Click on **Display montage** to refresh images')
        data_path = 'inputs/OCTdata/val'
        labels = os.listdir(data_path)
        label_to_display = st.selectbox(
            label='Select a label to display',
            options = labels,
            index=0
        )
        st.info('Images might take few second to be displayed')
        if st.button('Display montage'):
            image_collage_per_label(label=label_to_display,
            nrows=2,
            ncols=3,
            img_height=10,
            img_width=10)