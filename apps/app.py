import streamlit as st
import streamlit.components.v1 as st_components

from settings import *
from utils.components import ChatMessagesComponent, ChatInputMessageComponent
from utils.conversation import Conversation
from utils.html import HtmlLoader, CssLoader
from apps.sidebar import Sidebar


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
        title = "🤖 Marvin Conversation 🤖"
        st.markdown(
            f"<h1 class='page-title'>{title}</h1>", unsafe_allow_html=True
        )

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
