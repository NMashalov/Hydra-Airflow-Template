from dataclasses import dataclass
import typing as tp

@dataclass
class Notification:
    channel: str

@dataclass
class Dag:
    name: str
    tags: list[str]
    templates: tp.Optional[str]


'''
Preset in group format 
'''

@dataclass
class Preset:
    dag: Dag
    actions: list[dict[str,str]]

Preset