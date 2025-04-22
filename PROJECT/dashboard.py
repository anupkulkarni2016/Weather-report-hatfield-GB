# dashboard.py
import pandas as pd
import streamlit as st

st.title("Live Weather Dashboard")
df = pd.read_csv("weather_log.csv", names=['Time', 'Temp', 'Description'])

st.line_chart(df[['Time', 'Temp']])
st.write(df.tail(10))
