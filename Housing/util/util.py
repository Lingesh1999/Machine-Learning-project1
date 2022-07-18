import yaml
import os,sys
from Housing.exception import housingexception


def read_yaml_file(file_path : str) -> dict:
    """
    This function will help to read the yaml file.
    """
    try:
        with open(file_path, "rb") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise housingexception(e, sys) from e