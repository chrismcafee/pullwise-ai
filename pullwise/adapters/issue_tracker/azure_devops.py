from pullwise.ports.issue_tracker_port import IssueTrackerPort


class AzureDevops(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Azure Devops
        return {'key': issue_key, 'summary': '', 'description': ''}
