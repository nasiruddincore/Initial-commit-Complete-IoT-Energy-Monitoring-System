import streamlit as st
import pandas as pd
import os
import time

file_path = os.path.join('data', 'energy_logs.csv')

st.title("⚡ Smart Home Energy Monitor")

def load_data():
    if os.path.exists(file_path):
        return pd.read_csv(file_path, names=['Timestamp', 'Current', 'Power'])
    return None

while True:
    df = load_data()
    if df is not None and not df.empty:
        st.metric("Real-Time Power", f"{df.iloc[-1]['Power']:.2f} W")
        st.line_chart(df.set_index('Timestamp')['Power'])
        break # Display data and refresh
    else:
        st.write("Waiting for data... Ensure simulation is running.")
        time.sleep(2)
        st.rerun()