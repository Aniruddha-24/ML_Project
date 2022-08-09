import imp
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig , \
    ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig
from housing.exception import HousingException
from housing.logger import logging
from housing.util.util import read_yaml_file
from housing.constant import *
import sys,os






class Configuration:

 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            self.config_info
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_data_model_trainer_config(self)-> ModelTrainerConfig:
        pass

    def get_data_model_evalution_config(self) -> ModelEvaluationConfig:
        pass

    def get_data_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_data_training_pipeline_config(self) -> TrainingPipelineConfig:
        pass
        

           