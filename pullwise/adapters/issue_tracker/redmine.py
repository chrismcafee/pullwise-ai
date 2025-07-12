from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Redmine(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Redmine
        return {'key': issue_key, 'summary': '', 'description': ''}
