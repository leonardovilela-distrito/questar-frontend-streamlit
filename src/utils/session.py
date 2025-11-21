import streamlit as st
import uuid

def init_session_state() -> None:
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "awaiting_response" not in st.session_state:
        st.session_state.awaiting_response = False

    if "pending_question" not in st.session_state:
        st.session_state.pending_question = None

def change_chat_session() -> None:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
