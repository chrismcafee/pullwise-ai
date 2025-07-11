from rich.console import Console
from rich.table import Table

def render_review(review):
    console = Console()
    table = Table(title="AI Review Summary")
    table.add_column("Summary")
    table.add_row(review.get("summary", "No summary"))
    console.print(table)

    for comment in review.get("comments", []):
        console.print(f"[bold]{comment['file']}:{comment['line']}[/] - {comment['comment']}")
