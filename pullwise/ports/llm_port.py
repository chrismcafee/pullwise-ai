from abc import ABC, abstractmethod

class LLMPort(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_token_count(self, text: str) -> int:
        pass
