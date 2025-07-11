from abc import ABC, abstractmethod
from typing import List

class VectorIndexPort(ABC):
    @abstractmethod
    def index_repo(self, repo_path: str, language_filter: str = None) -> None:
        """Index source files in the given repo path"""
        pass

    @abstractmethod
    def query(self, query: str, top_k: int = 5) -> List[dict]:
        """Query the vector index and return top-k matches"""
        pass
