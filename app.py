import streamlit as st

import time

from auth import login_required
from data_service import fetch_data
from analysis import show_table, show_graphs, show_analysis, show_threshold_alerts, show_risk_score

st.set_page_config(page_title="Secure IoT Dashboard", layout="wide")

if login_required():
    st.title("📊 Secure IoT Data Dashboard")

    df = fetch_data()

    if df.empty:
        st.info("Waiting for IoT data...")
    else:

        show_risk_score(df)
        show_threshold_alerts(df)
        show_table(df)
        show_graphs(df)
        show_analysis(df)

    time.sleep(5)
    st.rerun()