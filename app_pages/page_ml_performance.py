import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
import joblib


def page_ml_performance_metrics():
    version = 'v3'

    st.write(
        f"### Train, Validation and Test Dataset: Counts per label  \n"
        f"As evident in the figure below, the datasets are well balanced"
    )

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write(
        f"### Model Training History  \n"
        f"The figures below show the model occuracy and loss during training. "
        f"The monotonous behaviour of the curves and sumilarity of absolute "
        f"values show no overfitting during training"
    )
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")


    st.write('### Loss and Occuracy of Train Dataset  \n')
    evaluation = joblib.load(f"outputs/{version}/evaluation.pkl")
    evaluation = ['%.2f' % elem for elem in evaluation]
    st.dataframe(pd.DataFrame(data=evaluation, columns=['Values',], index=['Loss', 'Accuracy']))
    st.write("---")

    st.write(
        f"### Model Performance  \n"
        f"The figures below show the confussion matrices for all datasets. "
    )
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        confussion_mat_train = plt.imread(f"outputs/{version}/confussion_matrix_train.png")
        st.image(confussion_mat_train, caption='Confussion Matrix for Training Set')
    with col2:
        confussion_mat_val = plt.imread(f"outputs/{version}/confussion_matrix_train.png")
        st.image(confussion_mat_val, caption='Confussion Matrix for Validation Set')
    with col3:
        confussion_mat_test = plt.imread(f"outputs/{version}/confussion_matrix_train.png")
        st.image(confussion_mat_test, caption='Confussion Matrix for Test Set')

