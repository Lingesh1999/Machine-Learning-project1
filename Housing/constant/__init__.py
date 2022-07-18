
from datetime import datetime
import os

Root_dir = os.getcwd()

config_dir = "config"
config_yaml_file = "config.yaml"
config_file_path = os.path.join(Root_dir, config_dir, config_yaml_file)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
