from pullwise.ports.vcs_port import VCSPort, DiffFile

class BitbucketAdapter(VCSPort):
    def get_pr_diff(self, pr_number: int):
        raise NotImplementedError("Bitbucket PR diff fetch not implemented yet")

    def get_diff_position(self, file: str, line: int):
        raise NotImplementedError("Bitbucket diff position resolution not implemented yet")

    def post_inline_comment(self, file: str, position: int, comment: str):
        raise NotImplementedError("Bitbucket comment posting not implemented yet")
