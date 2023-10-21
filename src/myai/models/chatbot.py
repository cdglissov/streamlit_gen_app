from langchain.chat_models import ChatOpenAI

from .model import ModelSettings


class OpenAIChatter:
    def __init__(self, model_settings: ModelSettings, model: ChatOpenAI) -> None:
        pass

    def get_reply_no_context(self, user_prompt):
        return None

    def get_reply_with_context(self, user_prompt):
        pass
