import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import gradio as gr

class_names=['Ayam Goreng','Bakso','Bubur Ayam','Lele Goreng','Mi Goreng','Nasi Putih','Sate','Soto','Telur Dadar','Telur Mata Sapi','ikan goreng','lontong','pempek','singkong goreng','tempe goreng']

model=tf.keras.models.load_model('./my_model_1')

def import_and_predict(image_data):  
    x = image_data.reshape((-1, 224, 224, 3))
    x = tf.keras.applications.imagenet_utils.preprocess_input(x, mode="tf")
    prediction = model.predict(x)
    labels=class_names
    confidences = {labels[i]: float(prediction[0][i]) for i in range(15)}   
    return confidences

gr.Interface(fn=import_and_predict, 
             inputs=gr.inputs.Image(shape=(224, 224)),
             outputs=gr.outputs.Label(num_top_classes=3),
             cache_examples=False).launch()

#examples=["Bakso.jpeg", "Sate.jpeg"]