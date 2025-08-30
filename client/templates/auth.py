import streamlit as st
from requests.auth import HTTPBasicAuth
import requests

def auth_ui(API_URL):
    st.title("Baymax - AI Medical Assistant")

    st.subheader("Login or Sign Up")
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # Login
    with tab1:
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            res = requests.post(f'{API_URL}/login', auth=HTTPBasicAuth(username, password))

            if res.status_code == 200:
                user_data = res.json()
                st.session_state.username = username
                st.session_state.password = password
                st.session_state.role = user_data.get("role", "user")
                st.session_state.loggedin = True
                st.session_state.mode = "chat"
                st.success(f"Logged in successfully! Welcome {username}")
                st.rerun()
            else:
                st.error(res.json().get("detail", "Login failed"))

    # Sign Up
    with tab2:
        new_user = st.text_input("New Username", key="signup_username")
        new_password = st.text_input("New Password", type="password", key="signup_password")
        new_role = st.selectbox("Choose Role", ["admin", "doctor", "nurse", "patient", "other"])

        if st.button("Sign Up"):
            payload = {
                "username": new_user,
                "password": new_password,
                "role": new_role
            }
            res = requests.post(f'{API_URL}/signup', json=payload)

            if res.status_code == 200:
                user_data = res.json()
                st.success(f"Sign up successful! You can now log in as {new_user}")
            else:
                st.error(res.json().get("detail", "Sign Up failed"))