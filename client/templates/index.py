import streamlit as st
import time

def index():

    st.title("Baymax - AI Medical Assistant")

    if st.session_state.loggedin and not st.session_state.get("welcome_displayed", False):
        success_msg = st.empty()
        success_msg.success(f"Welcome back, {st.session_state.username}! \nYou are now logged in to Baymax as a {st.session_state.role} . You can now access chat and other features.")
        time.sleep(3)
        success_msg.empty()
        st.session_state.welcome_displayed = True

    if not st.session_state.loggedin:
        logout_msg = st.empty()
        logout_msg.info("You have been logged out. Please log in again to continue.")
        time.sleep(3)
        logout_msg.empty()
