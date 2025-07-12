from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Jira(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Jira
        return {'key': issue_key, 'summary': '', 'description': ''}
