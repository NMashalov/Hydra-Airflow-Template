import yaml
from pathlib import Path
from dag_generator import YamlPresetDir


def test_YamlDir():
    YamlPresetDir(Path('test.yaml'),Path('./ocr')).init_dir()

if __name__ == '__main__':
    test_YamlDir()
