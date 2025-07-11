import typer
app = typer.Typer()

@app.command(hidden=True)
def smoke():
    print("Running smoke test...")
    return "OK"
