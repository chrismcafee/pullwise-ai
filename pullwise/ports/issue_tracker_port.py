from abc import ABC, abstractmethod
from pullwise.context.context_model import IssueMetadata

class IssueTrackerPort(ABC):
    @abstractmethod
    def get_issue(self, issue_key: str) -> IssueMetadata:
        """
        Fetch the issue data by key.
        Returns:
            IssueMetadata
        """
        pass
