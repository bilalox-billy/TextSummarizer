from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_date_ingestion_pipeline import DataIngestionTrainingPipeline


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


