import streamlit as st
import requests
import pandas as pd
CHANNEL_ID = 2089276
API_KEY = 'NJ879R5WIU5VKMIW' #Read API

# Define the URL for retrieving the latest data from ThingSpeak
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}"

# # Make a GET request to the API endpoint
response = requests.get(url)
# Read the response into a DataFrame
data = response.json()
print(data.keys())
# print(data.keys())
# data = {'count': [], 'data': []}
# pd.set_option('display.max_columns', 100)
df = pd.DataFrame(data['feeds'])
df['field1']=df['field1'].astype(float)
df['field2']=df['field2'].astype(float)
df['field3']=df['field3'].astype(float)
df['field4']=df['field4'].astype(float)
df['created_at']=df['created_at'].astype('datetime64[ns]')
# # Display the DataFrame in the app
# df = pd.DataFrame({'count': data})
st.dataframe(df)

