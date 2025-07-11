import os
from pullwise.adapters.vcs.github import GitHubVCSAdapter
from pullwise.adapters.vcs.local_git import LocalGitAdapter

def get_vcs_adapter():
    if os.getenv("GITHUB_TOKEN") and os.getenv("GITHUB_REPO"):
        return GitHubVCSAdapter(os.getenv("GITHUB_TOKEN"), os.getenv("GITHUB_REPO"))
    return LocalGitAdapter()
