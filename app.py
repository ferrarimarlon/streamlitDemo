import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('ibov_data.csv')

# Filter for the year 2019
df = df[df['year'] == 2019]

# Select relevant columns: 'date' and 'close'
df = df[['date', 'close']]
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

df = df.set_index('date')

st.line_chart(df['close'])
