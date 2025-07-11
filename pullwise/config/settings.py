import os
import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "llm": "openai",
    "llm_fallback": True,
    "use_langchain": True,
    "langchain_tracing": False,
    "memory_recall_enabled": True,
}

CONFIG_PATH = Path.home() / ".pullwise" / "config"

class Settings:
    def __init__(self):
        self.config = DEFAULT_CONFIG.copy()

        # Load ~/.pullwise/config if exists
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, "r") as f:
                file_config = json.load(f)
                self.config.update(file_config)

        # Override with environment variables
        for key in self.config:
            env_key = f"PULLWISE_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if val.lower() in ("true", "false"):
                    val = val.lower() == "true"
                self.config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def llm(self) -> str:
        return self.get("llm")

    @property
    def llm_fallback(self) -> bool:
        return self.get("llm_fallback")

    @property
    def use_langchain(self) -> bool:
        return self.get("use_langchain")

    @property
    def langchain_tracing(self) -> bool:
        return self.get("langchain_tracing")

    @property
    def memory_recall_enabled(self) -> bool:
        return self.get("memory_recall_enabled")
