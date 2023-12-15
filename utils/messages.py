# roles
HUMAN = "human"
AI = "ai"
SYSTEM = "system"


class BaseMessage:
    def __init__(self, content: str, role: str):
        self._content = content
        self._role = role

    @property
    def role(self):
        return self._role

    @property
    def content(self):
        return self._content

    def to_dict(self) -> dict:
        return {"role": self._role, "content": self._content}


class SystemMessage(BaseMessage):
    def __init__(self, content: str):
        super().__init__(content, role="system")


class HumanMessage(BaseMessage):
    def __init__(self, content: str):
        super().__init__(content, role="human")


class AIMessage(BaseMessage):
    def __init__(self, content: str):
        super().__init__(content, role="ai")
