import uuid
from abc import ABCMeta, abstractmethod

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


class AbstractButton(metaclass=ABCMeta):
    def __init__(self, key_secret: str, conversation_manager: ConversationManager):
        self._conversation_manager = conversation_manager
        self._key_secret = key_secret

    @abstractmethod
    def process(self):
        pass


class ButtonDeleteConversation(AbstractButton):
    def process(self):
        conversation = self._conversation_manager.get_conversation(key_secret=self._key_secret)
        if conversation:
            print(f"DELETE: {conversation.title}")
        return self


class ButtonRenameConversation(AbstractButton):
    def process(self):
        conversation = self._conversation_manager.get_conversation(key_secret=self._key_secret)
        if conversation:
            print(f"RENAME: {conversation.title}")
        return self


class ButtonLoadConversation(AbstractButton):
    def process(self):
        conversation = self._conversation_manager.get_conversation(key_secret=self._key_secret)
        if conversation:
            print(f"LOAD: {conversation.title}")
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
            col1, col2, col3 = st.sidebar.columns((6, 1, 1))
            # Cria um botão para cada conversa
            col1.button(
                conversation.title,
                key="load_" + conversation.key_secret,
                use_container_width=True,
                on_click=lambda cid=conversation.key_secret: ButtonLoadConversation(
                    cid, self._conversation_manager
                ).process()
            )
            # Cria um botão para excluir cada conversa
            col2.button(
                "✏️",
                key="rename_" + conversation.key_secret,
                use_container_width=True,
                on_click=lambda cid=conversation.key_secret: ButtonRenameConversation(
                    cid, self._conversation_manager
                ).process()
            )
            # Cria um botão para excluir cada conversa
            col3.button(
                "🗑️",
                key="delete_" + conversation.key_secret,
                use_container_width=True,
                on_click=lambda cid=conversation.key_secret: ButtonDeleteConversation(
                    cid, self._conversation_manager
                ).process()
            )

        return self
