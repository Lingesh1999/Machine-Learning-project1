from Housing.entity.config_entity import *
from Housing.util.util import read_yaml_file
import os

from Housing.constant import *

class Configuration:

    def __init__(self, Config_file_path : str = config_file_path,
                current_time_stamp : str = CURRENT_TIME_STAMP) -> None:
        
        self.config_info = read_yaml_file(file_path = Config_file_path)

    def get_data_ingestion_config(self) -> dataingestion_config:
        pass

    def get_data_validation_config(self) -> datavalidation_config:
        pass

    def get_data_transformation_config(self) -> datatransformation_config:
        pass

    def get_model_trainer_config(self) -> modeltrainer_config:
        pass
    
    def get_model_evaluation_config(self) -> modelevaluation_config:
        pass

    def get_model_pusher_config(self) -> modelpusher_config:
        pass

    def get_training_pipeline_config(self) -> trainingpipeline_config:
        pass
