import uuid

import streamlit as st
from slugify import slugify

from utils.conversation import ConversationManager


class ButtonCreateConversation:
    def __init__(self, conversation_manager: ConversationManager):
        self._conversation_manager = conversation_manager

    def _make(self):
        title = "Nova Conversa"
        self._conversation_manager.username = st.session_state.username
        conversation = self._conversation_manager.new_conversation(
            username=st.session_state.username,
            key_id=slugify(title),
            key_secret=str(uuid.uuid4()),
            title=title,
        )
        st.session_state.conversation = conversation
        return self

    def process(self):
        if st.sidebar.button("Criar Conversa", use_container_width=True):
            if not st.session_state.username:
                st.sidebar.error("Por favor, insira um nome de usuário válido.")
            else:
                self._make()
                st.sidebar.success("Nova conversa criada.")
        return self


class Sidebar:
    def __init__(self, conversation_manager: ConversationManager):
        self._conversation_manager = conversation_manager

    def add_tools(self):
        ButtonCreateConversation(self._conversation_manager).process()
        return self

    def update(self):
        # Título
        st.sidebar.title("Chats")
        # Nome do usuário.
        username = st.sidebar.text_input("Digite seu nome:")
        st.session_state.username = username

        self.add_tools()

        # Cria um botão para cada conversa
        st.sidebar.divider()
        for conversation in self._conversation_manager.conversations:
            st.sidebar.button(conversation.title, key=conversation.key_id, use_container_width=True)

        return self
