import streamlit as st
from PIL import Image
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
from multipage import MultiPage
from pages import brownspot,gudi_rotten,healthy,leaf_blast,leaf_blight,leaf_smut,sheath_blight,tungro

st.set_page_config(
  page_title= "Rice Disease Detection", page_icon="../plant-disease-detection/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
  )

st.title("Rice Disease Detection")


def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()


lottie_farmer = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_sgn7zslb.json")

#---Use local CSS
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

selected = option_menu(
  menu_title=None,  #required
  options=["Home","Symptoms and Solutions","Growth Monitoring"],  # required
  icons=["house","lightbulb","graph-up-arrow"],  #optional
  menu_icon="cast",  #optional
  default_index=0, #optional
  orientation="horizontal",
  )

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.subheader("""
      Finding diseases in rice crops.Simplified.
    """)
    st.write("""
    Rice Disease Detection can be used to detect the disease on Rice Crop using Image Recognition. The results of Image Recognition and Rice Crops data will be analyzed by a Machine Learning model to predict whether the crop has a disease or not. Not only that, Rice Disease Detection will improve the crops' quality by its functionality such as how to cure guidance, the right treatment to have the best crops conditions, articles to improve their knowledge, and the progress recapitulation.
    """)

    st.write("""
    The application will detect their quality (health) status. If a disease is detected, the application will give information about the disease (this includes 7 diseases: Brown Spot, Gudi Rotten, Leaf Blast, Leaf Blight, Leaf Smut, Sheath Blight, and Tungro) and show how to cure the diseased crops. 
    """)
  with right_column:
    st_lottie(lottie_farmer, key="farmer", height= 400)


if selected == "Home":
  st.subheader("Please choose if you want to use a web camera or upload a file to detect the disease: ")
  col1, col2, col3 = st.columns([0.5,0.8,1])
  with col2:
    use_web_camera = st.button("Use Web Camera :camera_with_flash:") 
    if use_web_camera:
      switch_page("Web Camera")
  
  with col3:
    upload_file = st.button("Upload File :page_facing_up:")
    if upload_file:
      switch_page("Upload")
    

if selected == "Symptoms and Solutions":
  st.subheader("Please select the disease to view its symptoms and solutions: ")
  app = MultiPage()
  app.st = st

  #LOADING THE PAGES 
  # for app_name, app_function in pages.items():
  app.add_page("Brown Spot", brownspot.app)
  app.add_page("Gudi Rotten", gudi_rotten.app)
  app.add_page("Healthy", healthy.app)
  app.add_page("Leaf Blast",leaf_blast.app) 
  app.add_page("Leaf Blight",leaf_blight.app)
  app.add_page("Leaf Smut", leaf_smut.app)
  app.add_page("Sheath Blight", sheath_blight.app)
  app.add_page("Tungro", tungro.app)

  app.run()
  st.write("Made with :heart:")

if selected == "Growth Monitoring":
  switch_page("growth monitoring")
  

  