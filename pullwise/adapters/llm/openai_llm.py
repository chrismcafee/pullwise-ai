import openai
from tenacity import retry, wait_exponential, stop_after_attempt
from pullwise.ports.llm_port import LLMPort
import logging

logger = logging.getLogger(__name__)

class OpenAILLMAdapter(LLMPort):
    def __init__(self, settings):
        self.api_key = settings.openai_api_key
        self.model = settings.openai_model or "gpt-4"
        openai.api_key = self.api_key

    @retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(5))
    def generate(self, prompt: str) -> str:
        logger.info("Calling OpenAI API...")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"]

    def get_token_count(self, text: str) -> int:
        import tiktoken
        enc = tiktoken.encoding_for_model(self.model)
        return len(enc.encode(text))
