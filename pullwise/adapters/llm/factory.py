from pullwise.adapters.llm.openai_llm import OpenAILLM
from pullwise.adapters.llm.together_llm import TogetherLLM
from pullwise.adapters.llm.groq_llm import GroqLLM
from pullwise.adapters.llm.fireworks_llm import FireworksLLM
from pullwise.adapters.llm.cohere_llm import CohereLLM
from pullwise.adapters.llm.huggingface_llm import HuggingFaceLLM
from pullwise.adapters.llm.codellama_llm import CodeLlamaLLM
from pullwise.ports.llm_port import LLMPort
from pullwise.config.settings import Settings

def get_llm_adapter(settings: Settings) -> LLMPort:
    model = settings.llm.lower()

    if model == "openai":
        return OpenAILLM(settings)
    elif model == "together":
        return TogetherLLM(settings)
    elif model == "groq":
        return GroqLLM(settings)
    elif model == "fireworks":
        return FireworksLLM(settings)
    elif model == "cohere":
        return CohereLLM(settings)
    elif model == "huggingface":
        return HuggingFaceLLM(settings)
    elif model == "codellama":
        return CodeLlamaLLM(settings)
    else:
        raise ValueError(f"Unsupported LLM provider: {model}")
