import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Gudi Rotten", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Sheath Rot/Gudi Rotten")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../plant-disease-detection/images/disease/IMG20201109102709_00.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Rotting occurs on the leaf sheath that encloses the young panicles.

        - Irregular spots or lesions, with dark reddish brown margins and gray center.

        - lesions enlarge and often coalesce and may cover the entire leaf sheath.

        - Severe infection causes entire or parts of young panicles to remain within the sheath. Unemerged panicles rot and florets turn red-brown to dark brown.

        - whitish powdery growth inside the affected sheaths and young panicles.

        - Infected panicles and grains are sterile, shriveled, partially or unfilled, and discolored.
          """)
    
    with left_column:
      st.image(img_sym,width=320)
      # st_lottie(lottie_coding, key="coding", height= 300)


  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Solutions")
      st.markdown("""
        - For control of sheath rot, spray the fungicides at the time of panicle emergence.

        - Application of a systemic pesticide,Tridemorph (a fungicide) and phosphamidon (an insecticide) in combination protected the plants from sheath rot.

        - Seed treatment with fungicides such as Mancozeb and Benomyl effectively eliminate seedborne inoculum.

        - Spray Carbendazim 250 g or Chlorothalonil 1 kg or Edifenphos 1 lit/ha.

        - Foliar spraying with Benomyl and copper oxychloride were also found to be effective.
          """)
    
    with left_column:
      st.image("https://5.imimg.com/data5/VZ/BU/RL/GLADMIN-68815/chlorothalonil-500x500.png",width=320)