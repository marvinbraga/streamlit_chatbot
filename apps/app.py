import streamlit as st
import streamlit.components.v1 as st_components
from settings import *
from utils.components import ChatMessagesComponent, ChatInputMessageComponent
from utils.html import HtmlLoader, CssLoader
from utils.messages import HumanMessage, AIMessage


class ChatBot:
    def __init__(self):
        CssLoader().load()
        # Mock de mensagens.
        # st.session_state.messages = [
        #     # HumanMessage("Olá! Meu nome é Marcus. Como você pode me ajudar?"),
        #     # AIMessage("Olá Marcus! Por enquanto em nada, pois, ainda estou em desenvolvimento. :-)")
        # ]

    def run(self):
        # Apresenta o título
        title = "🤖 Marvin Conversation 🤖"
        st.markdown(
            f"<h1 class='page-title'>{title}</h1>", unsafe_allow_html=True
        )

        # Apresenta as mensagens.
        try:
            messages = st.session_state.messages
        except AttributeError:
            st.session_state.messages = messages = [
                HumanMessage("Olá! Meu nome é Marcus. Como você pode me ajudar?"),
                AIMessage("Olá Marcus! Por enquanto em nada, pois, ainda estou em desenvolvimento. :-)")
            ]

        ChatMessagesComponent(messages=messages).run()

        # Apresenta o input.
        ChatInputMessageComponent(
            caption="Digite sua mensagem",
            help_text="Digite aqui o texto que deseja.",
            label="Mensagem:"
        ).run()

        st_components.html(HtmlLoader(APP_HTML).load(), height=0, width=0)
        return self


ChatBot().run()
