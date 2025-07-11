import typer
from pullwise.cli import review

app = typer.Typer()
app.add_typer(review.app, name="review")

@app.callback()
def main():
    """Pullwise - AI-powered code review CLI"""
    pass

if __name__ == "__main__":
    app()
