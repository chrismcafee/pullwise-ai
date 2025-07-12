from abc import ABC, abstractmethod
from typing import List, Dict

class VCSPort(ABC):
    @abstractmethod
    def get_pr_diff(self, pr_number: int) -> List[Dict]:
        '''Get the diff for the given PR number'''
        pass

    @abstractmethod
    def get_diff_position(self, file: str, line: int) -> int:
        '''Get the position of the given line in the diff'''
        pass

    @abstractmethod
    def post_inline_comment(self, file: str, position: int, comment: str):
        '''Post an inline comment to the given file at the given position'''
        pass

    @abstractmethod
    def get_local_repo_metadata(self) -> dict:
        """Returns metadata like org, repo name, current branch, remote URL, etc."""
        pass
