from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class PullRequestMetadata:
    number: int
    title: str
    description: str
    author: str
    base_branch: str
    head_branch: str

@dataclass
class DiffFile:
    filename: str
    diff: str

@dataclass
class IssueMetadata:
    key: str
    summary: str
    description: Optional[str] = None

@dataclass
class CodeContext:
    filename: str
    snippet: str

@dataclass
class ReviewContext:
    pr: PullRequestMetadata
    diff_files: List[DiffFile]
    linked_issue: Optional[IssueMetadata] = None
    chroma_context: List[CodeContext] = field(default_factory=list)
    voyage_context: List[str] = field(default_factory=list)
    prior_comments: List[Dict] = field(default_factory=list)
