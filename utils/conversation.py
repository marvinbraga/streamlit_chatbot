from utils.messages import HumanMessage, BaseMessage, AIMessage


class Conversation:
    def __init__(self, key_id: str, key_secret: str, title: str, messages: list[BaseMessage] | None = None):
        self._messages = messages if messages else []
        self._title = title
        self._key_secret = key_secret
        self._key_id = key_id

    @property
    def messages(self):
        return self._messages

    @property
    def title(self):
        return self._title

    @property
    def key_id(self):
        return self._key_id

    @property
    def key_secret(self):
        return self._key_secret

    def add_human_message(self, content: str):
        message = HumanMessage(content)
        self._messages.append(message)
        return self

    def add_ai_message(self, content: str):
        message = AIMessage(content)
        self._messages.append(message)
        return self
