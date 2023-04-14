import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Sheath Blight", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Sheath Blight")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../plant-disease-detection/images/disease/sheath_blight__0_23.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - The fungus affects the crop from tillering to heading stage.

        - Initial symptoms are noticed on leaf sheaths near water level.

        - On the leaf sheath oval or elliptical or irregular greenish grey spots are formed.

        - As the spots enlarge, the centre becomes greyish white with an irregular blackish brown or purple brown border.

        - Lesions on the upper parts of plants extend rapidly coalesing with each other to cover entire tillers from the water line to the flag leaf.
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
        - Control of sheath blight has been mainly through the use of foliar fungicides.

        - Carbendazim (1 g/lit), Propiconazole (1ml/lit) may be applied.

        - Spraying of infected plants with fungicides, such as Benomyl and Iprodione, and antibiotics, such as Validamycin and Polyoxin, is effective against the disease.

        - Spray Carbendazim 250 g or Chlorothalonil 1 kg or Edifenphos 1 lit/ha.

        - Apply FYM 12.5 t/ha or green manure 6.25 t/ha to promote antagonistic microflora
          """)
    
    with left_column:
      st.image("https://agritech.tnau.ac.in/expert_system/paddy/Images/Images/diseases/6.%20sheath%20blight/identification%20of%20pathogen/sheath%20blight-%20resized/chemical%20method/spray%20Iprodione.jpg",width=320)