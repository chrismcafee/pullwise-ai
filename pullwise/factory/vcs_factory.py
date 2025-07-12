from pullwise.factory.base import BaseAdapterFactory
from pullwise.ports.vcs_port import VCSPort
from pullwise.adapters.vcs.bitbucket import BitbucketAdapter
from pullwise.adapters.vcs.codecommit import AWSCodeCommitAdapter
from pullwise.adapters.vcs.github import GitHubAdapter
from pullwise.adapters.vcs.gitlab import GitLabAdapter
from pullwise.adapters.vcs.local_git import LocalGitAdapter
from pullwise.adapters.vcs.local_svn import LocalSubversionAdapter

class VCSFactory(BaseAdapterFactory):

    @classmethod
    def from_settings(cls, settings) -> VCSPort:
        vcs = (settings.vcs or "").lower()

        if vcs == "bitbucket":
            return BitbucketAdapter(settings)
        elif vcs == "codecommit":
            return AWSCodeCommitAdapter(settings)
        elif vcs == "github":
            return GitHubAdapter(settings)
        elif vcs == "gitlab":
            return GitLabAdapter(settings)
        elif vcs == "local_git" or vcs == "":
            return LocalGitAdapter(settings)
        elif vcs == "svn":
            return LocalSubversionAdapter(settings)


        raise ValueError(f"Unsupported VCS provider: {vcs}")
