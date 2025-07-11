from pullwise.ports.llm_port import LLMPort
import logging

logger = logging.getLogger(__name__)

class LLMFallbackWrapper(LLMPort):
    def __init__(self, llms: list[LLMPort]):
        self.llms = llms

    def generate(self, prompt: str) -> str:
        for llm in self.llms:
            try:
                return llm.generate(prompt)
            except Exception as e:
                logger.warning(f"LLM failed: {type(llm).__name__} - {e}")
        raise RuntimeError("All LLMs failed to generate a response.")

    def get_token_count(self, text: str) -> int:
        return self.llms[0].get_token_count(text)
