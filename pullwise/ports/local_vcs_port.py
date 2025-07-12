from typing import tuple

class LocalVCSPort:
    def detect_github_repo() -> tuple[str, str]:
        """Detects GitHub org and repo name from the local Git configuration."""
        pass

    def detect_bitbucket_repo() -> tuple[str, str]:
        """Detects Bitbucket org and repo name from the local Git configuration."""
        pass

    def detect_codecommit_repo() -> tuple[str, str]:
        """Detects CodeCommit org and repo name from the local Git configuration."""
        pass

    def detect_gitlab_repo() -> tuple[str, str]:
        """Detects GitLab org and repo name from the local Git configuration."""
        pass

    def detect_svn_repo() -> tuple[str, str]:
        """Detects SVN org and repo name from the local Git configuration."""
        pass

