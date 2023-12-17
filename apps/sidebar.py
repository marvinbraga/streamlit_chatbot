import uuid

import streamlit as st
from slugify import slugify

from utils.conversation import ConversationManager


class CreateConversation:
    def __init__(self, conversation_manager: ConversationManager):
        self._conversation_manager = conversation_manager

    def process(self):
        if st.sidebar.button("Criar Conversa", use_container_width=True):
            title = "Nova Conversa"
            key_id = f"{st.session_state.username}-{slugify(title)}"
            conversation = self._conversation_manager.new_conversation(
                key_id=key_id,
                key_secret=str(uuid.uuid4()),
                title=title,
            )
            st.session_state.conversation = conversation
            st.sidebar.success("Nova conversa criada.")
        return self


class Sidebar:
    def __init__(self, conversation_manager: ConversationManager):
        self._conversation_manager = conversation_manager

    def add_tools(self):
        CreateConversation(self._conversation_manager).process()
        return self

    def update(self):
        # Título
        st.sidebar.title("Chats")
        # Nome do usuário.
        username = st.sidebar.text_input("Digite seu nome:")
        st.session_state.username = username

        self.add_tools()
        st.sidebar.divider()
        for conversation in self._conversation_manager.conversations:
            # Cria um botão para cada conversa
            st.sidebar.button(conversation.title, key=conversation.key_id, use_container_width=True)

        return self
