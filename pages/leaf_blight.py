import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Leaf Blight", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Leaf Blight")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../images/disease/blight__0_70.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Water-soaked to yellowish stripes on leaf blades or starting at leaf tips with a wavy margin.

        - Leaves with undulated yellowish white or golden yellow marginal necrosis, drying of leaves back from tip and curling, leaving mid rib intact are the major symptoms.

        - Appearance of bacterial ooze that looks like a milky or opaque dewdrop on young lesions early in the morning.

        - Yellowish bacterial ooze may be seen coming out of the cut ends. The cut portion can be observed against the light to see the bacterial ooze streaming out from the cut ends into the water. After 1-2 hours, the water becomes turbid.
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
        - Seed treatment - seed soaking for 8 hours in Agrimycin (0.025%) and wettable ceresan (0.05%) followed by hot water treatment for 30 min at 52-54 ℃.

        - Spray neem oil 3% or NSKE 5%.

        - Application of bleaching powder @ 5 kg/ha in the irrigation water is recommended in the kresek stage.

        - Foliar spray with copper fungicides alternatively with Strepto-cyclin (250 ppm) to check secondary spread.

        - Spray Streptomycin sulphate + Tetracycline combination 300 g + Copper oxychloride 1.25kg/ha. If necessary repeat 15 days later.
          """)
    
    with left_column:
      st.image("https://cdn.shoplightspeed.com/shops/638365/files/24181818/1600x2048x2/dyna-gro-dyna-gro-pure-neem-oil-qt.jpg",width=320)