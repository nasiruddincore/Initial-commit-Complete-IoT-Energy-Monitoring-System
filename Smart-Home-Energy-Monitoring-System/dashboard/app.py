import streamlit as st
import pandas as pd
import time
import os

st.title("⚡ Smart Home Energy Monitor")

def load_data():
    if os.path.exists('data/energy_logs.csv'):
        return pd.read_csv('data/energy_logs.csv', names=['Timestamp', 'Current', 'Power'])
    return pd.DataFrame(columns=['Timestamp', 'Current', 'Power'])

# Refresh dashboard
placeholder = st.empty()

while True:
    df = load_data()
    if not df.empty:
        with placeholder.container():
            st.metric("Real-Time Power", f"{df.iloc[-1]['Power']:.2f} W")
            st.line_chart(df.set_index('Timestamp')['Power'])
    else:
        st.write("Waiting for simulation data...")
    time.sleep(2)
