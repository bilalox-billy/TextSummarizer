from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_date_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline


logger.info("Logging is implemented...")



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e