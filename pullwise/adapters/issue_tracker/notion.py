from pullwise.ports.issue_tracker_port import IssueTrackerPort


class Notion(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Notion
        return {'key': issue_key, 'summary': '', 'description': ''}
