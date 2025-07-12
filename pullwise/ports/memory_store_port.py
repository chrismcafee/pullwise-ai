from abc import ABC, abstractmethod
from typing import List

from pullwise.context.context_model import ReviewContext

class MemoryStorePort(ABC):
    @abstractmethod
    def save_memory(self, pr_id: str, context: ReviewContext, ai_output: str) -> None:
        '''Save memory to a file in the format {pr_id}.json'''
        pass

    @abstractmethod
    def recall(self, prompt: str, tags: List[str]) -> List[str]:
        '''Recall memory from a file in the format {pr_id}.json'''
        pass
