import streamlit as st

# st.set_page_config(
#   page_title= "Healthy Leaf", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Healthy Leaf")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  # img_sym = Image.open("../RICE DETECTION/Train_Data/Disease_Train_Data/leaf_blight/blight__0_70.jpg")

      
  st.markdown("""
    No need to worry your plant is safe...
    """)
  
