from .llm import get_llm
from .tools import add_numbers

class SimpleAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, prompt: str) -> str:
        # simple tool logic
        if "add" in prompt.lower():
            parts = [int(x) for x in prompt.split() if x.isdigit()]
            if len(parts) >= 2:
                return str(add_numbers(parts[0], parts[1]))

        # fallback to LLM
        return self.llm(prompt)
