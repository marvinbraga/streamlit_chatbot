import streamlit as st
from abc import ABCMeta, abstractmethod
from apps.settings import *
from utils.conversation import Conversation
from utils.html import ImageLoader
from utils.messages import BaseMessage, AI, HumanMessage, AIMessage


class AbstractChatComponent(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class ChatMessagesComponent(AbstractChatComponent):
    def __init__(self, conversation: Conversation):
        self._conversation = conversation

    def run(self):
        chat_placeholder = st.container()
        with chat_placeholder:
            for message in self._conversation.messages:
                icon_path = CHAT_ICON_PATH.format(AI_ICON if message.role == AI else USER_ICON)
                icon_base64 = ImageLoader(icon_path).load()
                div = f"""
                <div class="{CHAT_ROW} {'' if message.role == AI else ROW_REVERSE}">
                    <img class="{CHAT_ICON}" src="data:image/png;base64,{icon_base64}">
                    <div class="{CHAT_BUBBLE} {'ai-bubble' if message.role == AI else 'human-bubble'}">
                        &#8203;{message.content}
                    </div>
                </div>
                """
                st.markdown(div, unsafe_allow_html=True)

            for _ in range(3):
                st.markdown("")
        return self


class SubmitOnClickStrategy:
    def execute(self):
        human_prompt = st.session_state.human_prompt
        if not str(human_prompt).strip():
            return self
        # TODO: Faz o processamento para recuperar a resposta.
        # Atualiza as mensagens.
        st.session_state.conversation.add_human_message(human_prompt)
        count = (len(st.session_state.conversation.messages) + 1) // 2
        st.session_state.conversation.add_ai_message(f"Nova resposta - ({count})")
        return self


class OnClickStrategyFactory:
    @staticmethod
    def create_strategy(strategy="submit_message"):
        cls = {
            "submit_message": SubmitOnClickStrategy,
        }[strategy]
        return cls()


class ChatInputMessageComponent(AbstractChatComponent):
    def __init__(self, caption: str, help_text: str, label: str):
        self._label = label
        self._help_text = help_text
        self._caption = caption

    def run(self):
        prompt_placeholder = st.form("chat-form")
        with prompt_placeholder:
            st.markdown(f"**{self._caption}**")
            cols = st.columns((6, 1))
            cols[0].text_area(
                label=self._label,
                help=self._help_text,
                label_visibility="collapsed",
                key="human_prompt",
            )
            cols[1].form_submit_button(
                "Submit",
                type="primary",
                on_click=OnClickStrategyFactory.create_strategy().execute,
            )
        return self
