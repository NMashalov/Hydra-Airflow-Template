from jinja2 import Template
import typing as tp
from pathlib import Path
import datetime
import yaml


def joins_strings(l: tp.Optional[list[str]]):
    return '[' + ','.join(l) + ']' if l is not None else None

def template_dag(template: Path, output: Path, type: tp.Literal['dev','prod']):
    t = Template(source = template)
    # add useful operations for templating
    t.globals['now'] = datetime.datetime.now
    t.globals['yaml'] = yaml
    t.globals['join'] = joins_strings

    output.write_text(t.render({}))
