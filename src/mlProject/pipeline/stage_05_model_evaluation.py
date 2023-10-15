from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ModelEvaluationManager
from mlProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ModelEvaluationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer = ModelEvaluation(config=model_trainer_config)
        model_trainer.log_into_mlflow()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationManager()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e