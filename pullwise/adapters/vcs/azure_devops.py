from pullwise.ports.vcs_port import VCSPort, DiffFile

class AzureDevOpsAdapter(VCSPort):
    def get_pr_diff(self, pr_number: int):
        raise NotImplementedError("Azure DevOps PR diff fetch not implemented yet")

    def get_diff_position(self, file: str, line: int):
        raise NotImplementedError("Azure DevOps diff position resolution not implemented yet")

    def post_inline_comment(self, file: str, position: int, comment: str):
        raise NotImplementedError("Azure DevOps comment posting not implemented yet")
