import streamlit as st
import pandas as pd


# ===============================
# Threshold values (CONFIG)
# ===============================
TEMP_FEVER = 38.0
TEMP_WARNING = 37.5
HUM_HIGH = 70




def show_table(df):
    st.subheader("📄 Latest Decrypted Data")
    st.dataframe(df.tail(20), use_container_width=True)

def show_graphs(df):
    st.subheader("📈 Sensor Trends")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    st.line_chart(df.set_index("timestamp")[["temp", "hum"]])



def show_threshold_alerts(df):
    st.subheader("🚨 Threshold-Based Alerts")

    latest = df.iloc[-1]

    # Temperature alerts
    if latest["temp"] >= TEMP_FEVER:
        st.error("🔥 High temperature detected (Fever)")
    elif latest["temp"] >= TEMP_WARNING:
        st.warning("⚠️ Elevated temperature")

    # Humidity alerts
    if latest["hum"] >= HUM_HIGH:
        st.warning("💧 High humidity detected")

def show_risk_score(df):
    st.subheader("🧠 Device Health Risk Score")

    # Rule-based risk score
    df["risk_score"] = (
        (df["temp"] > TEMP_FEVER).astype(int) * 2 +
        (df["hum"] > HUM_HIGH).astype(int)
    )

    latest_score = df["risk_score"].iloc[-1]

    st.metric("Current Risk Score", latest_score)

    if latest_score == 0:
        st.success("🟢 Normal condition")
    elif latest_score <= 2:
        st.warning("🟠 Moderate risk detected")
    else:
        st.error("🔴 High risk – immediate attention required")



def show_analysis(df):
    st.subheader("🚨 Anomaly Detection")

    high_temp = df[df["temp"] > 39]
    st.metric("High Temperature Events", len(high_temp))

    if not high_temp.empty:
        st.warning("⚠️ High temperature detected")
