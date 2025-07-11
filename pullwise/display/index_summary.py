from rich.console import Console
from rich.table import Table

def print_index_summary(index_result: dict):
    console = Console()
    table = Table(title="📦 Indexing Summary")
    table.add_column("Collection", style="cyan")
    table.add_column("Files Indexed", style="green")
    table.add_row(index_result["collection_name"], str(index_result["files_indexed"]))
    console.print(table)
