import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
from multipage import MultiPage
from pages import brownspot,gudi_rotten,healthy,leaf_blast,leaf_blight,leaf_smut,sheath_blight,tungro

#---Use local CSS
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_loader = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_Bom6gU.json")

#---LOADING THE PREDICTION MODEL---

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache_resource
def load_model():
    model=tf.keras.models.load_model("D:/MAJOR_PROJECT/plant-disease-detection/models/plant.h5")
    return model
with st.spinner('Model is being loaded..'):
  model=load_model()


st.write("""
         # Rice Disease Detection
         """
        )

file = st.file_uploader("", type=["jpg", "png"])
# file = st.camera_input("Take a picture")
# if picture:
#   file = st.image(picture)

def import_and_predict(image_data, model):
  size = (256,256)    
  image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img = np.asarray(image)
  img_reshape = img[np.newaxis,...]
  prediction = model.predict(img_reshape)
  return prediction

def class_prediction():
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ['Brownspot','Gudi Rotten','Healthy','Leaf Blast','Leaf Blight','Leaf Smut','Sheath Blight','Tungro']
    
    string = "Prediction : " + class_names[np.argmax(predictions)]
    # st.success(string)
    if class_names[np.argmax(predictions)] == 'Healthy':
        st.success(string)
    else:
        st.warning(string)


if st.button('Predict ✨'):
  if file is None:
    st.text("Please upload an image file")
  else:
    class_prediction()
    

    









