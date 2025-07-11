import typer
from pullwise.core.review_agent import ReviewAgent

app = typer.Typer()

@app.command()
def run(pr_number: int):
    """Run AI code review on the given PR number."""
    agent = ReviewAgent()
    agent.review(pr_number)
