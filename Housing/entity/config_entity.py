from collections import namedtuple

dataingestion_config = namedtuple("dataingestion_config",
["dataset_download_url", "tgz_download_dir","raw_data_dir",
"ingested_train_dir", "ingested_test_dir"])

datavalidation_config = namedtuple("datavalidation_config",[
"schema_file_path"])

datatransformation_config = namedtuple("datatransformation_config",
["add_bedroom_per_room","transformed_train_dir",
"transformed_test_dir","preprocessed_object_file_path"])

modeltrainer_config = namedtuple("modeltrainer_config",
["trained_model_file_path","base_accuracy"])

modelevaluation_config = namedtuple("modelevaluation_config",
["model_evaluation_file_path","time_stamp"])

modelpusher_config = namedtuple("modelpusher_config",
["export_dir_path"])

trainingpipeline_config = namedtuple("trainingpipeline_config",
["export_dir_path"])