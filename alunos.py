import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample Data (replace with your actual DataFrame)
data = {
    'total_posts': np.random.randint(1, 100, 100),
    'helpful_post': np.random.randint(1, 100, 100),
    'nice_code_post': np.random.randint(1, 100, 100),
    'collaborative_post': np.random.randint(1, 100, 100),
    'confused_post': np.random.randint(1, 100, 100),
    'creative_post': np.random.randint(1, 100, 100),
    'bad_post': np.random.randint(1, 100, 100),
    'amazing_post': np.random.randint(1, 100, 100),
    'timeonline': np.random.rand(100) * 1000,
    'sk1_classroom': np.random.rand(100) * 50,
    'sk2_classroom': np.random.rand(100) * 50,
    'sk3_classroom': np.random.rand(100) * 50,
    'sk4_classroom': np.random.rand(100) * 50,
    'sk5_classroom': np.random.rand(100) * 50,
    'Approved': np.random.choice([True, False], size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Approved' and calculate mean for each column
mean_values = df.groupby('Approved').mean()

# Plotting the bar chart using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
mean_values.T.plot(kind='bar', ax=ax)

# Add labels and title
ax.set_title('Mean of Features Grouped by Approval Status')
ax.set_ylabel('Mean Value')
ax.set_xlabel('Features')

# Show the plot in Streamlit
st.pyplot(fig)