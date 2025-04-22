# weather_app.py
import requests

API_KEY = "90e1fb816278ae6b2f91ff6bcca91728"
CITY = "HATFIELD"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Print current weather
temp = data['main']['temp']
desc = data['weather'][0]['description']
print(f"Current temp in {CITY}: {temp}°C, {desc}")


import pandas as pd
from datetime import datetime
import time

def log_weather():
    response = requests.get(URL)
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    timestamp = datetime.now()

    log = pd.DataFrame([[timestamp, temp, desc]], columns=['Time', 'Temp', 'Description'])
    
    # Append to CSV
    log.to_csv("data/weather_log.csv", mode='a', header=False, index=False)


if temp >= 11:
    print("🔥 Heat alert!")
elif temp < 11:
    print("❄️ Cold alert!")

# dashboard.py
import pandas as pd
import streamlit as st

st.title("Live Weather Dashboard")
df = pd.read_csv("weather_log.csv", names=['Time', 'Temp', 'Description'])

st.line_chart(df[['Time', 'Temp']])
st.write(df.tail(10))
