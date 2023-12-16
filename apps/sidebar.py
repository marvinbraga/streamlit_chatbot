import streamlit as st

from utils.conversation import Conversation


class Sidebar:
    def __init__(self):
        if "conversations" not in st.session_state:
            st.session_state.conversations = []

    def add_conversation(self, conversation: Conversation):
        st.session_state.conversations.append(conversation)
        return self

    def add_tools(self):
        return self

    def update(self):
        st.sidebar.title("Chats")
        self.add_tools()
        st.sidebar.divider()
        for conversation in st.session_state.conversations:
            # Cria um botão para cada conversa
            st.sidebar.button(conversation.title, key=conversation.key_id, use_container_width=True)

        return self
