import typer
from .templater import template_dag

app = typer.Typer()

@app.command
def template():
    
    template_dag(
    )
    
app()

