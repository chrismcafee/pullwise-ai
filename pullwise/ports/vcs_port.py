from typing import List, Dict

class VCSPort:
    def get_pr_diff(self, pr_number: int) -> List[Dict]:
        raise NotImplementedError

    def get_diff_position(self, file: str, line: int) -> int:
        raise NotImplementedError

    def post_inline_comment(self, file: str, position: int, comment: str):
        raise NotImplementedError
