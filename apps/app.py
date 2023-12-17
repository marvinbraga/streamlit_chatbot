import streamlit as st
import streamlit.components.v1 as st_components

from apps.settings import APP_HTML
from apps.sidebar import Sidebar
from utils.components import ChatMessagesComponent, ChatInputMessageComponent, HeaderComponent
from utils.conversation import ConversationManager
from utils.html import HtmlLoader, CssLoader


class ChatBot:
    def __init__(self):
        CssLoader().load()
        if "conversation_manager" not in st.session_state:
            conversation_manager = ConversationManager()
            st.session_state.conversation_manager = conversation_manager

            if "sidebar" not in st.session_state:
                st.session_state.sidebar = Sidebar(conversation_manager=conversation_manager)

    def run(self):
        # Exibe a sidebar.
        st.session_state.sidebar.update()
        # Apresenta as mensagens.
        if "conversation" in st.session_state:
            # Apresenta o título
            HeaderComponent(
                title="🤖 Marvin Conversation 🤖",
                conversation=st.session_state.conversation
            ).run()

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
