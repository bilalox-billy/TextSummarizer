import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any
from  ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path to yaml file

    Raises:
        ValueError: If yaml file is empty
        e: Empty file

    Returns:
        ConfigBox: ConfigBox type object
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list[Path]): list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

