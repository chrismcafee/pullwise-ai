from pullwise.ports.issue_tracker_port import IssueTrackerPort

class GitHubIssuesAdapter(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Github Issues
        return {'key': issue_key, 'summary': '', 'description': ''}
