# st.write("Growth Monitoring from Thingspeak")
import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# lottie_plant = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_nmv5tjwu.json")

lottie_plant = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tjlyill3.json")

#---Use local CSS
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Define ThingSpeak channel ID and API key
CHANNEL_ID = 2082196
API_KEY = '7YA0K8TYZNV75DFD' #'PFGW8OODW23D08JQ'

# Define the URL for retrieving the latest data from ThingSpeak
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}"

st.header("Growth Monitoring")

# Define Streamlit app
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
  # Set Streamlit app title
    st.subheader("Real-time IoT Sensor Data")
    st.write("""
    We made an IoT Smart Plant Monitoring System. It demonstrates how to track parameters like moisture of the soil, sunlight, humidity, and temperature of the plant environment. It uploads the sensed
    information to the databases on Thingspeak Cloud.
    """)
    st.write("It gives values of real time data which is obtained from the sensors.")

    st.write("""
    The plant monitoring system is helpful for watering the plants and to monitor few parameters for growth of plants. This system is very used in few areas like nursery farms and in agriculture.
    """)
  
  with right_column:
    st_lottie(lottie_plant, key="plant", height= 330)


st.write("Values in tabular format")
# # Make a GET request to the API endpoint
response = requests.get(url)
# Read the response into a DataFrame
data = response.json()
# print(data.keys())
# print(data.keys())
# data = {'count': [], 'data': []}
# pd.set_option('display.max_columns', 100)
df = pd.DataFrame(data['feeds'])
df['field1']=df['field1'].astype(float)
df['field2']=df['field2'].astype(float)
df['field3']=df['field3'].astype(float)
df['field4']=df['field4'].astype(float)
df['created_at']=df['created_at'].astype('datetime64[ns]')
# Display the DataFrame in the app
# df = pd.DataFrame({'count': data})
st.dataframe(df)

# Define Streamlit widgets for selecting which sensor data to display
sensor = st.selectbox("Select Sensor", ["Soil Moisture", "LDR", "Temperature", "Humidity"])

# Define Streamlit widget for selecting how to display the data
chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart"])

# Define Streamlit widget for selecting the time range
# time_range = st.slider("Select Time Range (hours)", 1, 24, 6)

# Use Streamlit's caching mechanism to reduce the number of API requests
# @st.cache_resource
# def get_data():
  # Retrieve the latest data from ThingSpeak
  # response = requests.get(url)

  #  Parse the JSON response
  # data = response.json()
  # data.keys()
  # df = pd.DataFrame(data['feeds'])
  # # print(df)
  # df['field1']=df['field1'].astype(float)
  # df['field2']=df['field2'].astype(float)
  # df['field3']=df['field3'].astype(float)
  # df['field4']=df['field4'].astype(float)
  # df['created_at']=df['created_at'].astype('datetime64[ns]')
  # Return the selected sensor data
  # if sensor == "Soil Moisture":
  #   return df["field1"]
  # elif sensor == "LDR":
  #   return df["field2"]
  # elif sensor == "Temperature":
  #   return df["field3"]
  # elif sensor == "Humidity":
  #   return df["field4"]
  

# Get the data and display it based on the selected chart type
  
# data = get_data()
df = pd.DataFrame(data['feeds'])

if sensor == "Soil Moisture":
  data= df["field1"]
elif sensor == "LDR":
  data= df["field2"]
elif sensor == "Temperature":
  data= df["field3"]
elif sensor == "Humidity":
  data= df["field4"]
# # data = data.convert_dtypes()
if chart_type == "Line Chart":
  st.line_chart(data,height=450,width=300)
elif chart_type == "Bar Chart":
  st.bar_chart(data,height=450,width=300)

# Run the Streamlit app
# if __name__ == "__main__":
#   app()

if sensor == "Soil Moisture":
  components.iframe(width=450, height=260, src="https://thingspeak.com/channels/2082196/charts/1?api_key=7YA0K8TYZNV75DFD"
  )
elif sensor == "LDR":
  components.iframe(width=450, height=260, src="https://thingspeak.com/channels/2082196/charts/2?api_key=7YA0K8TYZNV75DFD"
  )
elif sensor == "Temperature":
  components.iframe(width=450, height=260, src="https://thingspeak.com/channels/2082196/charts/3?api_key=7YA0K8TYZNV75DFD"
  ) 
  # components.iframe(width=450, height=260,src="https://thingspeak.com/channels/2082196/widgets/620700"
  # )
elif sensor == "Humidity":
  components.iframe(width=450, height=260, src="https://thingspeak.com/channels/2082196/charts/4?api_key=7YA0K8TYZNV75DFD"
  )
