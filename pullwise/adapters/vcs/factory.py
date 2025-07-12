import os
from pullwise.adapters.vcs.github import GitHubVCSAdapter
from pullwise.adapters.vcs.local_git import LocalGitAdapter
from pullwise.adapters.vcs.bitbucket import BitbucketVCSAdapter
from pullwise.adapters.vcs.codecommit import CodeCommitVCSAdapter
from pullwise.adapters.vcs.gitlab import GitLabVCSAdapter
from pullwise.adapters.vcs.local_svn import LocalSVNVCSAdapter

def get_vcs_adapter():
    if os.getenv("GITHUB_TOKEN") and LocalGitAdapter.detect_github_repo():
        return GitHubVCSAdapter(os.getenv("GITHUB_TOKEN"), LocalGitAdapter.detect_github_repo())
    elif os.getenv("BITBUCKET_TOKEN") and LocalGitAdapter.detect_bitbucket_repo():
        return BitbucketVCSAdapter(os.getenv("BITBUCKET_TOKEN"), LocalGitAdapter.detect_bitbucket_repo())
    elif os.getenv("CODECOMMIT_TOKEN") and LocalGitAdapter.detect_codecommit_repo():
        return CodeCommitVCSAdapter(os.getenv("CODECOMMIT_TOKEN"), LocalGitAdapter.detect_codecommit_repo())
    elif os.getenv("GITLAB_TOKEN") and LocalGitAdapter.detect_gitlab_repo():
        return GitLabVCSAdapter(os.getenv("GITLAB_TOKEN"), LocalGitAdapter.detect_gitlab_repo())
    elif os.getenv("LOCAL_SVN_REPO"):
        return LocalSVNVCSAdapter(os.getenv("LOCAL_SVN_REPO"))
    return LocalGitAdapter()
