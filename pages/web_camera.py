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
    model=tf.keras.models.load_model("D:/MAJOR PROJECT/RICE DETECTION/models/plant.h5")
    return model
with st.spinner('Model is being loaded..'):
  model=load_model()


st.write("""
         # Rice Disease Detection
         """
        )

# file = st.file_uploader("", type=["jpg", "png"])
file = st.camera_input("Take a picture")
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
    # class_names = ['Tomato__Not Diseased', 'Tomato__Diseased']
    # class_names = ['Tomato___Bacterial_spot',
    # 'Tomato___Early_blight',
    # 'Tomato___Healthy',
    # 'Tomato___Late_blight',
    # 'Tomato___Leaf_Mold',
    # 'Tomato___Septoria_leaf_spot',
    # 'Tomato___Spider_mites Two-spotted_spider_mite',
    # 'Tomato___Target_Spot',
    # 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    # 'Tomato___Tomato_mosaic+_virus']
    string = "Prediction : " + class_names[np.argmax(predictions)]
    # st.success(string)
    if class_names[np.argmax(predictions)] == 'Healthy':
        st.success(string)
    else:
        st.warning(string)

# def rice_preds():
   
    # app = MultiPage()
    # app.st = st

    # if preds == "Brownspot":
    #   switch_page("Brownspot")
    # elif preds == "Gudi Rotten":
    #   switch_page("Gudi Rotten")  
    # elif preds == "Leaf Blast":
    #   switch_page("Leaf Blast")
    # elif preds == "Leaf Blight":
    #   switch_page("Leaf Blight")
    # elif preds == "Leaf Smut":
    #   switch_page("Leaf Smut")
    # elif preds == "Sheath Blight":
    #   switch_page("Sheath Blight")
    # elif preds == "Tungro":
    #   switch_page("Tungro")
    # elif preds == "Healthy":
    #   switch_page("Healthy")
    
    # app.run()


if st.button('✨ Predict'):
  if file is None:
    st.text("Please upload an image file")
  else:
    preds = class_prediction()
    app = MultiPage()
    app.st = st
    # st.button("Symptoms and Solutions", on_click=rice_preds())
    # if preds == "Brownspot":
    #   app.add_page("Brownspot",brownspot.app)
    #   app.run()
    # elif preds == "Gudi Rotten":
    #   app.add_page("Gudi Rotten",gudi_rotten.app)
    #   app.run()  
    # elif preds == "Leaf Blast":
    #   app.add_page("Leaf Blast",leaf_blast.app)
    #   app.run()
    # elif preds == "Leaf Blight":
    #   app.add_page("Leaf Blight",leaf_blight.app)
    #   app.run()
    # elif preds == "Leaf Smut":
    #   app.add_page("Leaf Smut",leaf_smut.app)
    #   app.run()
    # elif preds == "Sheath Blight":
    #   app.add_page("Sheath Blight",sheath_blight.app)
    #   app.run()
    # elif preds == "Tungro":
    #   app.add_page("Tungro",tungro.app)
    #   app.run()
    # elif preds == "Healthy":
    #   app.add_page("Healthy",healthy.app)
    #   app.run()
    




