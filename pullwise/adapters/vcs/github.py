from github import Github
from pullwise.ports.vcs_port import VCSPort, DiffFile

class GitHubVCSAdapter(VCSPort):
    def __init__(self, token: str, repo_name: str):
        self.client = Github(token)
        self.repo = self.client.get_repo(repo_name)

    def get_pr_diff(self, pr_number: int):
        pr = self.repo.get_pull(pr_number)
        files = pr.get_files()
        return [DiffFile(file.filename, file.patch or "") for file in files]

    def get_diff_position(self, file: str, line: int) -> int:
        # NOTE: GitHub API only returns diff positions during comment creation
        raise NotImplementedError("Position lookup must be done using GitHub diff metadata")

    def post_inline_comment(self, file: str, position: int, comment: str):
        raise NotImplementedError("This method should be implemented with full PR context")

    def get_local_repo_metadata(self) -> dict:
        return {
            "repo_root": self.get_repo_root(),
            "remote_url": self.get_remote_url(),
            "branch": self.get_current_branch(),
            "org_repo": self.get_org_repo(),  # tuple (org, repo)
    }

