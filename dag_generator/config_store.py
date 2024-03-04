from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
import typing as tp

from omegaconf import OmegaConf
from hydra import compose, initialize_config_dir
from pathlib import Path

'''
Preset in group format 
'''
@dataclass
class Preset:
    dag: dict[str,str]
    actions: list[dict[str,dict[str,dict[str,str]]]]


### Config store update

cs = ConfigStore.instance()
cs.store(name='preset',node=Preset)


def load_model(dir_path: Path):
    with initialize_config_dir(version_base=None,config_dir=str(dir_path.parent)):
        return OmegaConf.to_container(
            compose(config_name=dir_path.name),resolve=True
        )
