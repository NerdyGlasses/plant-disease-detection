import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Leaf Blast", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Leaf Blast")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../RICE DETECTION/Train_Data/Disease_Train_Data/leaf_blast/blast__0_653.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Disease can infect paddy at all growth stages and all aerial parts of plant (Leaf, neck and node).

        - Small specks originate on leaves - subsequently enlarge into spindle shaped spots(0.5 to 1.5cm length, 0.3 to 0.5cm width) with ashy center.

        - Several spots coalesce -> big irregular patches

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
        - Seed Treatment with TNAU Pf 1liquid formulation @ 10 ml/kg of seeds

        - Seedling root dipping with TNAU Pf 1liquid formulation (500 ml for one hectare seedlings). Soil application with TNAU Pf1 liquid formulation (500ml/ha)

        - Spray after observing initial infection of the disease with Carbendazim 50WP @ 500g/ha (or) Tricyclozole 75 WP @ 500g/ha (or)

        - Treat the seed with Captan

          """)
    
    with left_column:
      st.image("https://azelisaes-us.com/wp-content/uploads/Captan_Fungicide.png",width=320)