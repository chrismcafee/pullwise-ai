from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Bugzilla(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Bugzilla
        return {'key': issue_key, 'summary': '', 'description': ''}
