import streamlit as st
import streamlit.components.v1 as st_components

from apps.settings import *
from apps.sidebar import Sidebar
from utils.components import ChatMessagesComponent, ChatInputMessageComponent, HeaderComponent
from utils.conversation import Conversation
from utils.html import HtmlLoader, CssLoader


class ChatBot:
    def __init__(self):
        CssLoader().load()
        # Mock de mensagens.
        if 'conversation' not in st.session_state:
            conversation = Conversation(
                key_id="username-001",
                key_secret="uuid_str",
                title="Minha Conversa",
            )
            conversation.add_human_message("Olá! Meu nome é Marcus. Como você pode me ajudar?")
            conversation.add_ai_message("Olá Marcus! Por enquanto em nada, pois, ainda estou em desenvolvimento. :-)")
            st.session_state.conversation = conversation

    def run(self):
        # Exibe a sidebar.
        Sidebar().update()

        # Apresenta o título
        HeaderComponent(
            title="🤖 Marvin Conversation 🤖",
            conversation=st.session_state.conversation
        ).run()

        # Apresenta as mensagens.
        conversation = st.session_state.conversation
        ChatMessagesComponent(conversation=conversation).run()

        # Apresenta o input.
        ChatInputMessageComponent(
            caption="Digite sua mensagem",
            help_text="Digite aqui o texto que deseja.",
            label="Mensagem:"
        ).run()

        st_components.html(HtmlLoader(APP_HTML).load(), height=0, width=0)
        return self


ChatBot().run()
