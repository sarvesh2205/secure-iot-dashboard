import streamlit as st
import hashlib

PASSWORD_HASH = st.secrets["DASHBOARD_PASSWORD_HASH"]

def login_required():
    if "auth" not in st.session_state:
        st.session_state.auth = False

    if not st.session_state.auth:
        st.title("🔐 Secure IoT Dashboard Login")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            if hashlib.sha256(pwd.encode()).hexdigest() == PASSWORD_HASH:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Invalid password")

        return False

    return True
