from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import DataTransformationManager
from mlProject import logger


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = DataTransformationManager()
        data_validation_config = config.get_data_transformation_config()
        data_validation = DataTransformation(config=data_validation_config)
        data_validation.train_test_split()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e