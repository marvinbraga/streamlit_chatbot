import streamlit as st


class Sidebar:
    def __init__(self):
        if "conversations" not in st.session_state:
            st.session_state.conversations = []

    def update(self):
        st.sidebar.title("Chats")
        return self
