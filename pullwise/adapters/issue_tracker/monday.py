from pullwise.ports.issue_tracker_port import IssueTrackerPort


class Monday(IssueTrackerPort):
    def get_issue(self, issue_key: str):
        # TODO: Implement integration with Monday
        return {'key': issue_key, 'summary': '', 'description': ''}
