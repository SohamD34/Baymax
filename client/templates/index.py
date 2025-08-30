import streamlit as st
import time

PAGE_TITLE = "Baymax - AI Medical Assistant"

def index():
    st.title(PAGE_TITLE)
    
    if st.session_state.loggedin:
        success_msg = st.empty()
        success_msg.success(f"Welcome back, {st.session_state.username}! \nYou are now logged in to Baymax as a {st.session_state.role} . You can now access chat and other features.")
        time.sleep(3)
        success_msg.empty()

    if not st.session_state.loggedin:
        logout_msg = st.empty()
        logout_msg.info("You have been logged out. Please log in again to continue.")
        time.sleep(3)
        logout_msg.empty()
        
    else:
        st.write("Welcome to Baymax, your AI-powered medical assistant. Please log in or sign up to continue.")
