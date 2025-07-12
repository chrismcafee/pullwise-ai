from pullwise.ports.issue_tracker_port import IssueTrackerPort

class Trello(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Trello
        return {'key': issue_key, 'summary': '', 'description': ''}
