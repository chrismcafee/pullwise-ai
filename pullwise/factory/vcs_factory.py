import subprocess
from pullwise.factory.base import BaseAdapterFactory
from pullwise.ports.vcs_port import VCSPort
from pullwise.adapters.vcs.bitbucket import BitbucketAdapter
from pullwise.adapters.vcs.codecommit import AWSCodeCommitAdapter
from pullwise.adapters.vcs.github import GitHubAdapter
from pullwise.adapters.vcs.gitlab import GitLabAdapter
from pullwise.adapters.vcs.local_git import LocalGitAdapter
from pullwise.adapters.vcs.local_svn import LocalSubversionAdapter
from pullwise.adapters.vcs.azure_devops import AzureDevOpsAdapter

class VCSFactory(BaseAdapterFactory):

    # TODO: inject remote_url from local git
    # TODO: parse vcs provider from url and return adapter
    @staticmethod
    def detect_from_local_git() -> VCSPort:
        try:
            # Step 1: Ensure we are inside a git work tree
            subprocess.check_output(("git rev-parse --is-inside-work-tree").split(" "), stderr=subprocess.DEVNULL)

            # TODO: use helper from local git adapter
            # Step 2: Get the remote origin URL
            output = subprocess.check_output(("git remote get-url origin").split(" "))
            url = output.decode().strip()

            # Step 3: Detect known VCS providers
            if "github.com" in url:
                # TODO: parse org and repo from git@github.com:org/repo.git and pass to GitHubAdapter(org, repo)
                return GitHubAdapter()
            elif "gitlab.com" in url:
                # TODO: parse org and repo from https://gitlab.com/org/repo.git and pass to GitLabAdapter(org, repo)
                return GitLabAdapter()
            elif "bitbucket.org" in url:
                # TODO: parse org and repo from ssh://git@bitbucket.org/org/repo.git and pass to BitbucketAdapter(org, repo)
                return BitbucketAdapter()
            elif "codecommit" in url:
                # TODO: parse org and repo from git@codecommit.com:org/repo.git and pass to AWSCodeCommitAdapter(org, repo)
                return AWSCodeCommitAdapter()
            elif "dev.azure.com" in url:
                # TODO: parse org and repo from https://dev.azure.com/org/repo.git and pass to AzureDevOpsAdapter(org, repo)
                return AzureDevOpsAdapter()
            else:
                raise ValueError(f"Unsupported VCS provider: {url}")

        except subprocess.CalledProcessError:
            # Not a Git repo or missing remote, display error message and exit
            raise ValueError("Not a Git repo or missing remote - run in a Git repo with a remote origin")
