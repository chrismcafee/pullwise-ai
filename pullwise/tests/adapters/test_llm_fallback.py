import pytest
from pullwise.adapters.llm.llm_fallback import LLMFallbackWrapper
from pullwise.ports.llm_port import LLMPort


class FailingLLM(LLMPort):
    def generate(self, prompt: str) -> str:
        raise RuntimeError("Simulated failure")

    def get_token_count(self, text: str) -> int:
        return 1


class DummyLLM(LLMPort):
    def generate(self, prompt: str) -> str:
        return "Success!"

    def get_token_count(self, text: str) -> int:
        return 42


def test_llm_fallback_success():
    fallback = LLMFallbackWrapper([FailingLLM(), DummyLLM()])
    result = fallback.generate("Hello")
    assert result == "Success!"
