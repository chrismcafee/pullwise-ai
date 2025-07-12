from pullwise.factory.base import BaseAdapterFactory
from pullwise.adapters.issue_tracker.asana import AsanaAdapter
from pullwise.adapters.issue_tracker.azure_devops import AzureDevOpsAdapter
from pullwise.adapters.issue_tracker.bugzilla import BugzillaAdapter
from pullwise.adapters.issue_tracker.clickup import ClickupAdapter
from pullwise.adapters.issue_tracker.clubhouse import ClubhouseAdapter
from pullwise.adapters.issue_tracker.github_issues import GitHubIssuesAdapter
from pullwise.adapters.issue_tracker.gitlab_issues import GitlabIssuesAdapter
from pullwise.adapters.issue_tracker.jira import JiraAdapter
from pullwise.adapters.issue_tracker.linear import LinearAdapter
from pullwise.adapters.issue_tracker.monday import MondayAdapter
from pullwise.adapters.issue_tracker.notion import NotionAdapter
from pullwise.adapters.issue_tracker.redmine import RedmineAdapter
from pullwise.adapters.issue_tracker.trello import TrelloAdapter
from pullwise.adapters.issue_tracker.youtrack import YoutrackAdapter
from pullwise.ports.issue_tracker_port import IssueTrackerPort

class IssueTrackerFactory(BaseAdapterFactory):

    @classmethod
    def from_settings(cls, settings) -> IssueTrackerPort:
        provider = settings.issue_tracker.lower()

        if provider == "asana":
            return AsanaAdapter(settings)
        elif provider == "azure_devops":
            return AzureDevOpsAdapter(settings)
        elif provider == "bugzilla":
            return BugzillaAdapter(settings)
        elif provider == "clickup":
            return ClickupAdapter(settings)
        elif provider == "clubhouse":
            return ClubhouseAdapter(settings)
        elif provider == "github":
            return GitHubIssuesAdapter(settings)
        elif provider == "gitlab":
            return GitlabIssuesAdapter(settings)
        elif provider == "jira":
            return JiraAdapter(settings)
        elif provider == "linear":
            return LinearAdapter(settings)
        elif provider == "monday":
            return MondayAdapter(settings)
        elif provider == "notion":
            return NotionAdapter(settings)
        elif provider == "redmine":
            return RedmineAdapter(settings)
        elif provider == "trello":
            return TrelloAdapter(settings)
        elif provider == "youtrack":
            return YoutrackAdapter(settings)

        raise ValueError(f"Unsupported issue tracker: {provider}")
