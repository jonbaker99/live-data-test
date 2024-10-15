import streamlit as st
import pandas as pd
import numpy as np
import os

# Function to generate random data
def generate_data():
    return pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100),
        'D': np.random.rand(100),
        'E': np.random.rand(100)
    })

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = generate_data()

# Streamlit app
st.title("Random Data Generator with Datawrapper Integration")

# Button to regenerate data
if st.button("Regenerate Data"):
    st.session_state.data = generate_data()
    st.success("Data regenerated!")

# Display the data
st.subheader("Generated Data")
st.dataframe(st.session_state.data)

# Button to save data to CSV
if st.button("Save Data to CSV"):
    csv = st.session_state.data.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='random_data.csv',
        mime='text/csv',
    )
    st.success("Data prepared for download!")

# Display Datawrapper chart
st.subheader("Datawrapper Chart")
st.markdown("Note: Replace this with your actual Datawrapper embed code")
datawrapper_embed_code = """
<iframe title="Random Data Visualization" aria-label="chart" id="datawrapper-chart-XXXXX" src="https://datawrapper.dwcdn.net/XXXXX/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe>
"""
st.components.v1.html(datawrapper_embed_code, height=400)