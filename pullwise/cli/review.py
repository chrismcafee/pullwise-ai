import typer
from pullwise.core.review_agent import ReviewAgent

app = typer.Typer()

@app.command()
@inject_repo_info
def run(pr_number: int, org: str = None, repo: str = None):
    """Run AI code review on the given PR number."""
    agent = ReviewAgent()
    agent.review(org, repo, pr_number)
