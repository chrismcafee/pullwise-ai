# pullwise/adapters/issue_tracker/factory.py

from pullwise.config.settings import Settings
from pullwise.ports.issue_tracker_port import IssueTrackerPort

from pullwise.adapters.issue_tracker.github_issues import GitHubIssueTracker
from pullwise.adapters.issue_tracker.gitlab_issues import GitLabIssueTracker
from pullwise.adapters.issue_tracker.jira import JiraIssueTracker
from pullwise.adapters.issue_tracker.asana import AsanaIssueTracker
from pullwise.adapters.issue_tracker.trello import TrelloIssueTracker
from pullwise.adapters.issue_tracker.linear import LinearIssueTracker
from pullwise.adapters.issue_tracker.notion import NotionIssueTracker
# ...add other imports as they are implemented

def get_issue_tracker_adapter(settings: Settings) -> IssueTrackerPort:
    tracker = settings.issue_tracker.lower()

    if tracker == "github":
        return GitHubIssueTracker(settings.github_token)
    elif tracker == "gitlab":
        return GitLabIssueTracker(settings.gitlab_token)
    elif tracker == "jira":
        return JiraIssueTracker(settings.jira_url, settings.jira_token)
    elif tracker == "asana":
        return AsanaIssueTracker(settings.asana_token)
    elif tracker == "trello":
        return TrelloIssueTracker(settings.trello_token)
    elif tracker == "linear":
        return LinearIssueTracker(settings.linear_token)
    elif tracker == "notion":
        return NotionIssueTracker(settings.notion_token)
    # ...handle others as needed
    else:
        raise ValueError(f"Unsupported issue tracker: {tracker}")
