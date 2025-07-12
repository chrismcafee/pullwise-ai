from pullwise.factory.base import BaseAdapterFactory
from pullwise.ports.llm_port import LLMPort
from pullwise.adapters.llm.codellama_llm import CodeLlamaLLMAdapter
from pullwise.adapters.llm.cohere_llm import CohereLLMAdapter
from pullwise.adapters.llm.fireworks_llm import FireworksLLMAdapter
from pullwise.adapters.llm.groq_llm import GroqLLMAdapter
from pullwise.adapters.llm.huggingface_llm import HuggingFaceLLMAdapter
from pullwise.adapters.llm.openai_llm import OpenAILLMAdapter
from pullwise.adapters.llm.together_llm import TogetherLLMAdapter

class LLMFactory(BaseAdapterFactory):

    @classmethod
    def from_settings(cls, settings) -> LLMPort:
        model = settings.llm.lower()

        if model == "codellama":
            return CodeLlamaLLMAdapter(settings)
        elif model == "cohere":
            return CohereLLMAdapter(settings)
        elif model == "fireworks":
            return FireworksLLMAdapter(settings)
        elif model == "groq":
            return GroqLLMAdapter(settings)
        elif model == "huggingface":
            return HuggingFaceLLMAdapter(settings)
        elif model == "openai":
            return OpenAILLMAdapter(settings)
        elif model == "together":
            return TogetherLLMAdapter(settings)

        raise ValueError(f"Unsupported LLM model: {model}")
