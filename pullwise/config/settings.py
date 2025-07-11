import os
import json
from typing import Optional

class Settings:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self):
        config = {}

        # 1. Load from environment variables
        config["llm"] = os.getenv("PULLWISE_LLM", "openai")
        config["llm_fallback"] = os.getenv("PULLWISE_LLM_FALLBACK", "true").lower() == "true"
        config["use_langchain"] = os.getenv("PULLWISE_USE_LANGCHAIN", "true").lower() == "true"
        config["langchain_tracing"] = os.getenv("PULLWISE_LANGCHAIN_TRACING", "false").lower() == "true"
        config["memory_recall_enabled"] = os.getenv("PULLWISE_MEMORY_RECALL_ENABLED", "true").lower() == "true"

        # 2. Load from ~/.pullwise/config if it exists
        config_path = os.path.expanduser("~/.pullwise/config")
        if os.path.exists(config_path):
            try:
                with open(config_path, "r") as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except Exception as e:
                print(f"Warning: Failed to load config file: {e}")

        return config

    def get(self, key: str, default: Optional[str] = None):
        return self.config.get(key, default)

    @property
    def llm(self):
        return self.config["llm"]

    @property
    def llm_fallback(self):
        return self.config["llm_fallback"]

    @property
    def use_langchain(self):
        return self.config["use_langchain"]

    @property
    def langchain_tracing(self):
        return self.config["langchain_tracing"]

    @property
    def memory_recall_enabled(self):
        return self.config["memory_recall_enabled"]
