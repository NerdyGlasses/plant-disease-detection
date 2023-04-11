import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Tungro", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Tungro")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../RICE DETECTION/Train_Data/Disease_Train_Data/tungro/tungro__0_526.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Plants affected by tungro exhibit stunting and reduced tillering. Their leaves become yellow or orange-yellow, may also have rust-colored spots.

        - Discoloration begins from leaf tip and extends down to the blade or the lower leaf portion.

        - Delayed flowering, - panicles small and not completely exerted.

        - Most panicles sterile or partially filled grains.

        - Tungro virus disease affects all growth stages of the rice plant specifically the vegetative stage.
          """)
    
    with left_column:
      st.image(img_sym,width=320)



  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Solutions")
      st.markdown("""
        - Leaf yellowing can be minimized by spraying 2 % urea mixed with Mancozeb at 2.5 gm/lit.

        - Instead of urea foliar fertilizer like multi-K (potassium nitrate) can be sprayed at 1 per cent which impart resistance also because of high potassium content.

        - Fenthion 100 EC (40 ml/ha) may be sprayed 15 and 30 days after transplanting.

        - The vegetation on the bunds should also be sprayed with the insecticides. Maintain 2.5 cm of water in the nursery and broadcast anyone of the following in 20 cents Carbofuran 3 G 3.5 kg (or) Phorate 10 G 1.0 kg (or) Quinalphos 5 G 2.0 kg.

        - During pre-tillering to mid-tillering when one affected hill/m is observed apply Carbofuran granules @ 3.5kg/ha or spray Monocrotophos @ 1.6 to 2.2ml/lit to control insect vector.
          """)
    
    with left_column:
      st.image("https://www.glissando.ro/wp-content/uploads/2018/10/multi-k-13-0-46-600x600.jpg",width=320)