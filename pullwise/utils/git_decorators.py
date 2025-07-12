from functools import wraps
from pullwise.adapters.vcs.local_git import LocalGitAdapter

def inject_repo_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "org" not in kwargs or "repo" not in kwargs:
            git = LocalGitAdapter()
            org, repo = git.get_org_repo()
            kwargs.setdefault("org", org)
            kwargs.setdefault("repo", repo)
        return func(*args, **kwargs)
    return wrapper
