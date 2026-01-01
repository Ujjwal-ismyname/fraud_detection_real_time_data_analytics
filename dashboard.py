import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Real-Time Fraud Detection", layout="wide")

st.title("💳 Real-Time Fraud Detection Dashboard")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("prediction_output.csv")

        with placeholder.container():
            st.metric("Fraud Prediction", int(df["fraud_prediction"][0]))
            st.metric("Fraud Probability", df["fraud_probability"][0])

            st.subheader("Live Transaction Data")
            st.dataframe(df)

        time.sleep(2)

    except Exception:
        st.warning("Waiting for live data...")
        time.sleep(2)