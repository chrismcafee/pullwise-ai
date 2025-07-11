from typing import List
from pullwise.ports.llm_port import LLMPort
import logging

logger = logging.getLogger(__name__)

class LLMFallbackWrapper(LLMPort):
    def __init__(self, adapters: List[LLMPort]):
        self.adapters = adapters

    def generate(self, prompt: str) -> str:
        '''Generate a response using the first available LLM adapter'''
        for adapter in self.adapters:
            try:
                return adapter.generate(prompt)
            except Exception as e:
                logger.warning(f"LLM fallback: {adapter.__class__.__name__} failed with error: {e}")
                continue
        raise RuntimeError("All LLMs failed to generate a response")

    def get_token_count(self, text: str) -> int:
        '''Get the token count for the given text using the first available LLM adapter'''
        for adapter in self.adapters:
            try:
                return adapter.get_token_count(text)
            except Exception as e:
                logger.warning(f"Token count fallback: {adapter.__class__.__name__} failed with error: {e}")
                continue
        raise RuntimeError("All LLMs failed to count tokens")
