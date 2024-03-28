import pandas as pd
import numpy as np
import os
import joblib
from tensorflow.keras.models import load_model
from PIL import Image


def model_load(ver):
    from keras.models import load_model
    my_model = load_model(f'outputs/{ver}/OCTreader_model.h5')
    return my_model


def resize_image(img):
    '''
    Read image_shape from outputs
    resize my_image
    '''
    image_shape = joblib.load(f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def make_prediction(ver):
    model = model_load(ver)
    target_map = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
    pred_proba = model.predict(my_image)
    max_prob_pos = np.argmax(pred_proba)
    class_prediction = target_map[max_prob_pos]

    return pred_proba, class_prediction
