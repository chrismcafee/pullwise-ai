from pullwise.ports.vcs_port import LocalVCSPort
from git import Repo
from urllib.parse import urlparse

class LocalGitAdapter(LocalVCSPort):
    def detect_github_repo() -> tuple[str, str]:
        """
        Detects org and repo name from the local git configuration.
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
            raise RuntimeError(f"Unable to detect org and repo from git remote: {e}")
