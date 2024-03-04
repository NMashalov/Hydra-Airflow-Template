import typer
from dag_generator.config_store import load_model
import typing as tp 
from pathlib import Path
from enum import Enum

class Environment(str, Enum):
    dev = "dev"
    stage = "stage"
    prod = "prod"

app = typer.Typer()


@app.command('bulk_template')
def process(dir_path: 
    tp.Annotated[
        Path,
        typer.Option(
            exists=True,
            resolve_path=True,
        ),
    ],
    env: Environment,
    
    ):
    for path in dir_path.glob('*.yaml'):
        print(path)
        print(load_model(path))


@app.command('template')
def bulk_process(dir_path: 
    tp.Annotated[
        Path,
        typer.Option(
            exists=True,
            resolve_path=True,
        ),
    ],env: Environment):
    for path in dir_path.glob('*.yaml'):
        print(path)
        print(load_model(path))

app()

