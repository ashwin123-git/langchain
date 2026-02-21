from langchain_community.llms import Ollama
from .config import settings

def get_llm():
    return Ollama(model=settings.MODEL_NAME, temperature=settings.TEMPERATURE)
