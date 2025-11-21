import streamlit as st
from services.api import ask_bedrock
from utils.session import init_session_state
from components.sidebar import render_sidebar
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Agente Questar", layout="wide")

init_session_state()
render_sidebar()

st.title("Agente Questar")
st.markdown("> Seja bem-vindo ao agente de consulta veicular Questar")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sql_query"):
            st.markdown("**Consulta SQL utilizada:**")
            st.code(msg["sql_query"], language="sql")
        if msg.get("sql_table"):
            df = pd.DataFrame(msg["sql_table"])
            st.markdown("**Resultado da consulta:**")
            st.dataframe(df)

input_disabled = st.session_state.awaiting_response
user_input = st.chat_input("Pergunte algo...", disabled=input_disabled)

if user_input and not input_disabled:
    st.session_state.pending_question = user_input
    st.session_state.awaiting_response = True
    st.rerun()

if st.session_state.pending_question and st.session_state.awaiting_response:
    user_question = st.session_state.pending_question
    st.session_state.show_welcome = False
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )
    st.chat_message("user").markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            aswear = ask_bedrock(user_question, st.session_state.session_id)

            assistant_msg = {"role": "assistant", "content": aswear.response}
            if aswear.sql_query:
                assistant_msg["sql_query"] = aswear.sql_query
                assistant_msg["sql_table"] = aswear.sql_data

                st.markdown("**Consulta SQL utilizada:**")
                st.code(aswear.sql_query, language="sql")
                df = pd.DataFrame(aswear.sql_data)
                st.markdown("**Resultado da consulta:**")
                st.dataframe(df)

            st.session_state.messages.append(assistant_msg)

    st.session_state.pending_question = None
    st.session_state.awaiting_response = False
    st.rerun()
