import os
import typer
import subprocess
import datetime
from pullwise.utils.git_decorators import inject_repo_info

app = typer.Typer()

@app.command()
@inject_repo_info
def edit(pr_number: int, last_ai: bool = True, file: str = None, org: str = None, repo: str = None):
    base_path = os.path.expanduser(f"~/.pullwise/reviews/{org}/{repo}/{pr_number}")
    ai_dir = os.path.join(base_path, "ai")
    edited_dir = os.path.join(base_path, "edited")
    os.makedirs(edited_dir, exist_ok=True)

    if last_ai:
        file_to_edit = sorted(os.listdir(ai_dir))[-1]
        path = os.path.join(ai_dir, file_to_edit)
    elif file:
        path = file
    else:
        typer.echo("Must specify --last-ai or --file")
        raise typer.Exit(1)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    edited_path = os.path.join(edited_dir, f"review-{timestamp}.json")
    subprocess.call([os.environ.get("EDITOR", "vi"), path])
    os.rename(path, edited_path)
    typer.echo(f"Saved edited file to {edited_path}")
