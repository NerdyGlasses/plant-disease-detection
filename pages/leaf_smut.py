import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Leaf Smut", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )
def app():

  st.title("Leaf Smut")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../images/disease/smut-_0_3193.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Individual rice grain transformed into a mass of yellow fruiting bodies.

        - Growth of velvetty spores that enclose floral parts. Infected grain has greenish smut balls with a velvetty appearance.

        - The smut ball appears small at first and grows gradually up to the size of 1 cm. It is seen in between the hulls and encloses the floral parts.

        - Only few grains in a panicle are usually infected and the rest are normal.

        - As the fungi growth intensifies, the smut ball bursts and become orange then later yellowish-green or greenish-black in color.

        - Infection usually occurs during the reproductive and ripening stages, infecting a few grains in the panicle and leaving the rest healthy.
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
        - Seed treatment with carbendazim 2.0g/kg of seeds.

        - Spraying of copper oxychloride at 2.5 g/litre or Propiconazole at 1.0 ml/litre at boot leaf and milky stages will be more useful to prevent the fungal infection.

        - Seed treatment with carbendazim 2.0g/kg of seeds.

        - At tillering and preflowering stages, spray Hexaconazole @ 1ml/lit or Chlorothalonil 2g/lit.

        - In areas where the disease may cause yield loss, applying captan, captafol, fentin hydroxide, and mancozeb can be inhibited conidial germination.

        - At tillering and preflowering stages, spraying of carbendazim fungicide and copper base fungicide can effectively control the disease.
          """)
    
    with left_column:
      st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhISXGxOeKrTlGrZ6EOpBi2ulb6cg_OdzIRjW_4asYohNAh_t46JkcTh5jgkuXVCRgi9o&usqp=CAU",width=320)