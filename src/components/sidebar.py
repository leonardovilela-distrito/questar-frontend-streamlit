import streamlit as st
from utils.session import change_chat_session


def render_sidebar():
    with st.sidebar:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Resetar"):
                change_chat_session()

        with col2:
            if st.button("Sair"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.login_attempted = False
                st.rerun()
