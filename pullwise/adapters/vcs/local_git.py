from pullwise.ports.vcs_port import VCSPort, DiffFile
import subprocess

class LocalGitAdapter(VCSPort):
    def get_pr_diff(self, pr_number: int):
        output = subprocess.check_output(["git", "diff", "origin/main...HEAD"], text=True)
        return [DiffFile("local", output)]

    def get_diff_position(self, file: str, line: int) -> int:
        return line  # Placeholder

    def post_inline_comment(self, file: str, position: int, comment: str):
        print(f"[Local] Would post to {file} at line {position}: {comment}")
