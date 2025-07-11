from typing import List, Dict

class VCSPort:
    def get_pr_diff(self, pr_number: int) -> List[Dict]:
        '''Get the diff for the given PR number'''
        raise NotImplementedError

    def get_diff_position(self, file: str, line: int) -> int:
        '''Get the position of the given line in the diff'''
        raise NotImplementedError

    def post_inline_comment(self, file: str, position: int, comment: str):
        '''Post an inline comment to the given file at the given position'''
        raise NotImplementedError
