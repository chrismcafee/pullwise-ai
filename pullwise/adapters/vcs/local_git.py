from pullwise.ports.vcs_port import LocalVCSPort
from git import Repo
from urllib.parse import urlparse

class LocalGitAdapter(LocalVCSPort):
    # todo: implement single method to detect (remote) org and repo name from local Git config
    def detect_github_repo() -> tuple[str, str]:
        """
        Detects GitHub org and repo name from the local Git configuration.
        Returns: (org, repo)
        Raises: RuntimeError if detection fails
        """
        try:
            repo = Repo(".", search_parent_directories=True)
            remote_url = repo.remotes.origin.url

            # SSH format: git@github.com:org/repo.git
            # HTTPS format: https://github.com/org/repo.git
            if remote_url.startswith("git@"):
                path = remote_url.split(":", 1)[1]
            else:
                path = urlparse(remote_url).path.lstrip("/")

            org, repo_name = path.replace(".git", "").split("/", 1)
            return org, repo_name

        except Exception as e:
            raise RuntimeError(f"Unable to detect GitHub repo from Git remote: {e}")

    def detect_bitbucket_repo() -> tuple[str, str]:
        """
        Detects Bitbucket org and repo name from the local Git configuration.
        Returns: (org, repo)
        Raises: RuntimeError if detection fails
        """
        try:
            repo = Repo(".", search_parent_directories=True)
            remote_url = repo.remotes.origin.url

            # SSH format: git@bitbucket.org:org/repo.git
            # HTTPS format: https://bitbucket.org/org/repo.git
            if remote_url.startswith("git@"):
                path = remote_url.split(":", 1)[1]
            else:
                path = urlparse(remote_url).path.lstrip("/")

            org, repo_name = path.replace(".git", "").split("/", 1)
            return org, repo_name

        except Exception as e:
            raise RuntimeError(f"Unable to detect Bitbucket repo from Git remote: {e}")

    def detect_codecommit_repo() -> tuple[str, str]:
        """
        Detects CodeCommit org and repo name from the local Git configuration.
        Returns: (org, repo)
        Raises: RuntimeError if detection fails
        """
        try:
            repo = Repo(".", search_parent_directories=True)
            remote_url = repo.remotes.origin.url

            # SSH format: git@codecommit.com:org/repo.git
            # HTTPS format: https://codecommit.com/org/repo.git
            if remote_url.startswith("git@"):
                path = remote_url.split(":", 1)[1]
            else:
                path = urlparse(remote_url).path.lstrip("/")

            org, repo_name = path.replace(".git", "").split("/", 1)
            return org, repo_name

        except Exception as e:
            raise RuntimeError(f"Unable to detect CodeCommit repo from Git remote: {e}")

    def detect_gitlab_repo() -> tuple[str, str]:
        """
        Detects GitLab org and repo name from the local Git configuration.
        Returns: (org, repo)
        Raises: RuntimeError if detection fails
        """
        try:
            repo = Repo(".", search_parent_directories=True)
            remote_url = repo.remotes.origin.url

            # SSH format: git@gitlab.com:org/repo.git
            # HTTPS format: https://gitlab.com/org/repo.git
            if remote_url.startswith("git@"):
                path = remote_url.split(":", 1)[1]
            else:
                path = urlparse(remote_url).path.lstrip("/")

            org, repo_name = path.replace(".git", "").split("/", 1)
            return org, repo_name

        except Exception as e:
            raise RuntimeError(f"Unable to detect GitLab repo from Git remote: {e}")
