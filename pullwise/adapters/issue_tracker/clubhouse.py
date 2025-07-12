from pullwise.ports.issue_tracker_port import IssueTrackerPort


class Clubhouse(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Clubhouse
        return {'key': issue_key, 'summary': '', 'description': ''}
