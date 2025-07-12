import os
import json
import typer
from pullwise.adapters.vcs.factory import VCSAdapterFactory

app = typer.Typer()

@app.command()
def post(pr_number: int, file: str = None):
    base_path = os.path.expanduser(f"~/.pullwise/reviews/org/repo/{pr_number}/edited")
    if not file:
        file = sorted(os.listdir(base_path))[-1]
    path = os.path.join(base_path, file)

    with open(path) as f:
        review = json.load(f)

    vcs_adapter = VCSAdapterFactory.from_env()
    for comment in review.get("comments", []):
        vcs_adapter.post_inline_comment(comment["file"], comment["line"], comment["comment"])
        print(f"🦉 Posted comment to {comment['file']}:{comment['line']} - {comment['comment']}")
