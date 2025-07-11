from abc import ABC, abstractmethod
from typing import List

class MemoryStorePort(ABC):
    @abstractmethod
    def save_memory(self, pr_id: str, context, ai_output: str) -> None:
        pass

    @abstractmethod
    def recall(self, prompt: str, tags: List[str]) -> List[str]:
        pass
