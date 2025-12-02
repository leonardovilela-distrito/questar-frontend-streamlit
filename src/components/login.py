import streamlit as st
from services.auth import authenticate_user
import uuid


def login_screen():
    st.title("Login")

    if "login_attempted" not in st.session_state:
        st.session_state.login_attempted = False

    with st.form("login_form"):
        user = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")

        if submit:
            if authenticate_user(user, password):
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.messages = []
                st.session_state.session_id = str(uuid.uuid4())
                st.rerun()
            else:
                st.session_state.login_attempted = True

    if st.session_state.login_attempted and not st.session_state.get(
        "logged_in", False
    ):
        st.error("Usuário ou senha inválidos.")
