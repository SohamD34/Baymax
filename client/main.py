import os
import sys
from dotenv import load_dotenv
import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from templates.index import index
from templates.auth import auth_ui
from templates.sidebar import sidebar

load_dotenv()
API_URL = os.getenv("API_URL")


st.set_page_config(
    page_title="Baymax - AI Medical Assistant",
    layout="centered"
)

if "username" not in st.session_state:
    st.session_state.username = None
    st.session_state.password = None
    st.session_state.role = None
    st.session_state.loggedin = False
    st.session_state.mode = "auth"
    st.session_state.chat_history = []


def get_auth():
    return HTTPBasicAuth(st.session_state.username, st.session_state.password)


def upload_docs():
    st.subheader("Upload PDF for specific Role")
    uploaded_file=st.file_uploader("Choose a PDF file",type=["pdf"])
    role_for_doc=st.selectbox("Target Role dor docs",["doctor","nurse","patient","other"])

    if st.button("Upload Document"):
        if uploaded_file:
            files={"file":(uploaded_file.name,uploaded_file.getvalue(),"application/pdf")}
            data={"role":role_for_doc}
            res=requests.post(f"{API_URL}/upload_docs",files=files,data=data,auth=get_auth())
            if res.status_code==200:
                doc_info=res.json()
                st.success(f"Uploaded: {uploaded_file.name}")
                st.info(f"Doc Id : {doc_info['doc_id']},Access:{doc_info['accessible_to']}")
            else:
                st.error(res.json().get("detail","Upload failed"))
        else:
            st.warning("Please upload a file")


st.markdown("""
    <style>
        .welcome-header {
            text-align: center;
            color: #2E86C1;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .welcome-text {
            text-align: center;
            color: #5D6D7E;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .query-response-container {
            border: 1px solid #D5D8DC;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem auto;
            max-width: 600px;
            background-color: #F8F9FA;
        }

        .query-response-container .query {
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .query-response-container .response {
            margin-top: 0.5rem;
            color: #2E4053;
        }
    </style>
""", unsafe_allow_html=True)



if "welcome_displayed" not in st.session_state:
    st.session_state.welcome_displayed = False

if not st.session_state.welcome_displayed:
    st.markdown('<div class="welcome-header">Welcome to Baymax</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-text">Your AI Medical Assistant</div>', unsafe_allow_html=True)
    st.session_state.welcome_displayed = True


def show_history():
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            st.markdown(f'<div class="query" style="color: yellow;">{chat["user"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="response">{chat["bot"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="timestamp" style="font-size: 0.8rem; color: gray;">{chat.get("timestamp", "")}</div>', unsafe_allow_html=True)
        st.markdown('---', unsafe_allow_html=True)



def chat_interface():

    msg = st.text_input("Enter your query:", key="chat_input")

    if st.button("Send"):
        if not msg.strip():
            st.warning("Please enter a query")
        else:
            res = requests.post(f"{API_URL}/chat", data={"message": msg}, auth=get_auth())
            
            if res.status_code == 200:
                reply = res.json()
                st.markdown(f'<div class="query" style="color: yellow;">{msg}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="response">{reply["answer"]}</div>', unsafe_allow_html=True)
                st.session_state.chat_history.append({"user": msg, "bot": reply["answer"], "timestamp": reply.get("timestamp", "")})

            else:
                st.error(res.json().get("detail", "Something is wrong."))

    st.markdown('</div>', unsafe_allow_html=True)




def main_app():
    if not st.session_state.loggedin:
        auth_ui(API_URL)
    else:
        index()
        show_history()

        with st.sidebar:
            st.header("Profile")
            sidebar()

        if st.session_state.role=="admin":
            upload_docs()
            st.divider()
            chat_interface()
        else:
            chat_interface()

    


st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86C1;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }

    .stButton > button {
        background-color: #2E86C1;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s;
    }

    .stButton > button:hover {
        background-color: #1B4F72;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .sidebar-section {
        background-color: #F8F9FA;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .sidebar-section h3 {
        color: #2E86C1;
        margin-bottom: 0.5rem;
    }

    .sidebar-section p {
        color: #5D6D7E;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)





if __name__ == "__main__":
    main_app()