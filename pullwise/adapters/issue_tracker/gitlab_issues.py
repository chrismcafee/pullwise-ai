from pullwise.ports.issue_tracker_port import IssueTrackerPort

class GitlabIssuesAdapter(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Gitlab Issues
        return {'key': issue_key, 'summary': '', 'description': ''}
