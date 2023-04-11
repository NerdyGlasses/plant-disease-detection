import streamlit as st
from PIL import Image

# st.set_page_config(
#   page_title= "Brown Spots", page_icon="../RICE DETECTION/images/icons/favicon.ico", layout="wide",initial_sidebar_state="collapsed"
# )

def app():
  st.title("Brown Spots")

  def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  local_css("style/style.css")

  img_sym = Image.open("../images/disease/Brownspot__0_375.jpg")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
      st.subheader("Symptoms")
      
      st.markdown("""
        - Brown Spot is called as sesame leaf spot or Helminthosporiose or fungal blight The fungus attacks the crop from seedling in nursery to milk stage in main field.

        - The disease appears first as minute brown dots, later becoming cylindrical or oval to circular.(resemble sesame seed).

        - Spots measures 0.5 to 2.0mm in breadth - coalesce to form large patches.

        - Infection also occurs on panicle, neck with brown colour appearance.

        - Seeds also infected (black or brown spots on glumes spots are covered by olivaceous velvety growth).

        - The infection of the seed causes failure of seed germination, seedling mortality and reduces the grain quality and weight.
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
        - Seed soak / seed treatment with Captan or Thiram at 2.0g /kg of seed.

        - Spray Mancozeb (2.0g/lit) or Edifenphos (1ml/lit) - 2 to 3 times at 10 - 15 day intervals. Spray preferably during early hours or afternoon at flowering and post - flowering stages.

        - Seed treatment with Agrosan or Ceresan 2.5 g/kg seed to ward off seedling blight stage; Spraying copper fungicides to control secondary spread.

        - Seed treatment with Pseudomonas fluorescens @ 10g/kg of seed followed by seedling dip @ of 2.5 kg or products/ha dissolved in 100 litres and dipping for 30 minutes.

        - Grisepfulvin, nystatin, aureofungin, and similar antibiotics have been found effective in preventing primary seedling infection.
          """)
    
    with left_column:
      st.image("https://m.media-amazon.com/images/I/51eEsgwdqOL._SL1000_.jpg",width=320)