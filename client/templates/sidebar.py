import streamlit as st

def sidebar():
    """Enhanced sidebar with navigation and user info"""

    if "page" not in st.session_state:
        st.session_state.page = "chat"
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem; text-align: center;">
            <h2 style="color: white; margin: 0;">👤 {username}</h2>
            <p style="color: #E8F4FD; margin: 0; font-size: 1rem;">{role}</p>
        </div>
        """.format(username=st.session_state.get("username", "Guest"),
                   role=st.session_state.get("role", "N/A").title()),
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

    nav_buttons = {
        "Chat": "chat",
        "Profile": "profile",
        "Upload Docs": "upload" if st.session_state.role == "admin" else None,
        "Help": "help"
    }

    for label, page in nav_buttons.items():
        if page:
            if st.button(label, use_container_width=True, 
                         type="primary" if st.session_state.page == page else "secondary"):
                st.session_state.page = page
                st.rerun()

    st.markdown("---")

    st.markdown("### Your Stats")
    st.metric("Chat Messages", len(st.session_state.chat_history) if st.session_state.chat_history else 0)

    st.markdown("---")

    st.markdown('<div style="margin-top:400px;"></div>', unsafe_allow_html=True)

    with st.container():
        if st.button("Logout", use_container_width=True, type="secondary"):
            st.session_state.username = None
            st.session_state.password = None
            st.session_state.role = None
            st.session_state.loggedin = False
            st.session_state.page = "chat"
            st.session_state.chat_history = []
            st.rerun()

        st.markdown(
            """
            <div style="text-align: center; margin-top: 2rem; color: #7B68EE; font-size: 0.8rem;">
                    <p>Baymax v1.0<br>Your AI Medical Assistant</p>
            </div>
            """,
            unsafe_allow_html=True
        )