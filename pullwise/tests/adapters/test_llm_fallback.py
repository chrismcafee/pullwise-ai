import pytest
from pullwise.adapters.llm.llm_fallback import LLMFallbackWrapper

class MockLLM:
    def __init__(self, should_fail=False):
        self.should_fail = should_fail

    def generate(self, prompt: str) -> str:
        if self.should_fail:
            raise Exception("Simulated failure")
        return "fallback result"

    def get_token_count(self, text: str) -> int:
        if self.should_fail:
            raise Exception("Simulated failure")
        return len(text.split())

def test_fallback_success_after_failure():
    llm1 = MockLLM(should_fail=True)
    llm2 = MockLLM()
    wrapper = LLMFallbackWrapper([llm1, llm2])
    result = wrapper.generate("hello")
    assert result == "fallback result"

def test_all_failures_raise():
    llm1 = MockLLM(should_fail=True)
    llm2 = MockLLM(should_fail=True)
    wrapper = LLMFallbackWrapper([llm1, llm2])
    with pytest.raises(RuntimeError):
        wrapper.generate("will fail")
