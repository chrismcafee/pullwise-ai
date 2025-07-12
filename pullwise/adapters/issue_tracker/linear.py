from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Linear(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Linear
        return {'key': issue_key, 'summary': '', 'description': ''}
