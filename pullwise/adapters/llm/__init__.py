from pullwise.adapters.llm.openai_llm import OpenAILLM
from pullwise.adapters.llm.llm_fallback import LLMFallbackWrapper
from pullwise.ports.llm_port import LLMPort
from pullwise.config.settings import Settings


def get_llm_adapter(settings: Settings) -> LLMPort:
    providers = []

    if settings.llm == "openai":
        providers.append(OpenAILLM(settings))

    # Extend for other providers (e.g., Cohere, Groq) here
    # if settings.llm == "cohere":
    #     providers.append(CohereLLM(settings))

    if settings.llm_fallback:
        return LLMFallbackWrapper(providers)

    return providers[0]
