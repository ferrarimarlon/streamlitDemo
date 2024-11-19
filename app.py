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

# Get the max and min close values and the date of the max value
max_value = df['close'].max()
min_value = df['close'].min()
max_date = df['close'].idxmax()  # Get the date of the maximum value
min_date = df['close'].idxmin()  # Get the date of the minimum value

# Display the scorecard with max, min values, and the date of the max value
st.subheader("Scorecard")

# Display max and min values using st.metric()
st.metric(label="Max Close", value=f"R$ {max_value:,.2f}", delta=f"on {max_date.strftime('%d/%m/%Y')}")
st.metric(delta_color='inverse', label="Min Close", value=f"R$ {min_value:,.2f}", delta=f"on {min_date.strftime('%d/%m/%Y')}")