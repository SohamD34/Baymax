import os
import sys
from dotenv import load_dotenv
import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from templates.index import index
from templates.auth import auth_ui

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


def chat_interface():
    st.subheader("Ask a healthcare question")
    msg=st.text_input("Your query")

    if st.button("Send"):
        if not msg.strip():
            st.warning("Please enter a query")
        
        res=requests.post(f"{API_URL}/chat",data={"message":msg},auth=get_auth())
        if res.status_code==200:
            reply=res.json()
            st.markdown('### Answer: ')
            st.success(reply["answer"])
            if reply.get("sources"):
                for src in reply["sources"]:
                    st.write(f"--{src}")
        else:
            st.error(res.json().get("detail","Something is wrong."))



def main_app():
    if not st.session_state.loggedin:
        auth_ui(API_URL)
    else:
        index()
        
        if st.sidebar.button("Logout"):
            st.session_state.loggedin = False
            st.session_state.username = None
            st.session_state.password = None
            st.session_state.role = None
            st.rerun()

        if st.session_state.role=="admin":
            upload_docs()
            st.divider()
            chat_interface()
        else:
            chat_interface()


if __name__ == "__main__":
    main_app()