from abc import ABC, abstractmethod

class LLMPort(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        '''Generate a response using the LLM adapter'''
        pass

    @abstractmethod
    def get_token_count(self, text: str) -> int:
        '''Get the token count for the given text using the LLM adapter'''
        pass
