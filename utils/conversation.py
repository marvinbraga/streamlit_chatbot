from utils.messages import HumanMessage, BaseMessage, AIMessage


class Conversation:
    def __init__(self, username: str, key_id: str, key_secret: str, title: str,
                 messages: list[BaseMessage] | None = None):
        self._messages = messages if messages else []
        self._title = title
        self._key_secret = key_secret
        self._key_id = key_id
        self._username = username

    @property
    def username(self):
        return self._username

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


class ConversationManager:
    def __init__(self, username: str | None = None):
        self._username = username
        self._conversations: list[Conversation] = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def conversations(self):
        if not self._username:
            return []
        return [conversation for conversation in self._conversations if conversation.username == self._username]

    def get_conversation(self, **kwargs) -> Conversation | None:
        for conversation in self.conversations:
            if conversation.key_id == kwargs.get("key_id") or conversation.key_secret == kwargs.get("key_secret"):
                return conversation
        return None

    def add_conversation(self, conversation: Conversation):
        self._conversations.append(conversation)
        return self

    def new_conversation(self, username: str, key_id: str, key_secret: str, title: str):
        conversation = Conversation(
            username=username,
            key_id=key_id,
            key_secret=key_secret,
            title=title,
        )
        self.add_conversation(conversation)
        return conversation
