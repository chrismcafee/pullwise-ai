from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Asana(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Asana
        return {'key': issue_key, 'summary': '', 'description': ''}
