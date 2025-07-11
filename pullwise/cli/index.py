import typer
from pullwise.adapters.vector_store.chroma import ChromaIndexer
from pullwise.utils.file_scanner import scan_codebase
from pullwise.display.index_summary import print_index_summary

app = typer.Typer()

@app.command()
def index(
    path: str = typer.Argument(".", help="Path to the Git repo"),
    language: str = typer.Option(None, help="Optional language filter, e.g., python")
):
    """Indexes the repo source files using Chroma."""
    files = scan_codebase(path, language=language)
    indexer = ChromaIndexer()
    index_result = indexer.index_repo(files)
    print_index_summary(index_result)
