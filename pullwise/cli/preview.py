import os
import json
import typer
from rich.console import Console
from rich.table import Table
from pullwise.display.badge_renderer import add_footer

app = typer.Typer()

@app.command()
def preview(pr_number: int, with_code: bool = False, file: str = None):
    base_path = os.path.expanduser(f"~/.pullwise/reviews/org/repo/{pr_number}/ai")
    latest_file = sorted(os.listdir(base_path))[-1]
    with open(os.path.join(base_path, latest_file)) as f:
        review = json.load(f)

    console = Console()
    table = Table(title="PR Summary")
    table.add_column("Summary")
    table.add_row(review.get("summary", "No summary"))
    console.print(table)

    for comment in review.get("comments", []):
        if file and comment["file"] != file:
            continue
        console.print(f"[bold]{comment['file']}:{comment['line']}[/] - {add_footer(comment['comment'])}")
