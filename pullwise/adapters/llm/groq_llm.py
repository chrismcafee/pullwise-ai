from pullwise.ports.llm_port import LLMPort

class GroqLLMAdapter(LLMPort):
    def generate(self, prompt: str) -> str:
        return "This is a stubbed response."

    def get_token_count(self, text: str) -> int:
        return len(text.split())
