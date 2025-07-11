import os
import typer
from rich import print
from rich.console import Console

app = typer.Typer()

@app.command()
def index(repo_path: str = ".", language: str = "python"):
    console = Console()
    console.print(f"[bold green]Indexing repo:[/] {repo_path} for language: {language}")
    # Simulate Chroma + FAISS indexing
    chroma_path = os.path.expanduser("~/.pullwise/.cache/chroma")
    faiss_path = os.path.expanduser("~/.pullwise/.cache/faiss")
    os.makedirs(chroma_path, exist_ok=True)
    os.makedirs(faiss_path, exist_ok=True)
    console.print(f"[blue]Indexed code to:[/] {chroma_path}")
    console.print(f"[blue]Indexed docs to:[/] {faiss_path}")
