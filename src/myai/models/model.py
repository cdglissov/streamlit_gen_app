from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.llms.openai import OpenAI
from pydantic.dataclasses import dataclass

load_dotenv()


@dataclass
class ModelSettings:
    type: str
    temperature: int = 0
    max_tokens: int = 20
    max_retries: int = 1


def get_openai_chat_model(settings: ModelSettings) -> ChatOpenAI:
    chat_llm = ChatOpenAI(
        temperature=settings.temperature,
        model=settings.type,
        max_tokens=settings.max_tokens,
        max_retries=settings.max_retries,
    )
    return chat_llm


def get_openai_model(settings: ModelSettings) -> OpenAI:
    llm = OpenAI(
        temperature=settings.temperature,
        model=settings.type,
        max_tokens=settings.max_tokens,
        max_retries=settings.max_retries,
    )
    return llm
