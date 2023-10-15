import os
from pathlib import Path
from mlProject import logger
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from urllib.parse import urlparse
from mlProject.entity.config_entry import ModelEvaluationConfig
from mlProject.utils.common import save_json 

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run(experiment_id=1):
            logger.info("Eval the model....")
            predicted_qualitites = model.predict(test_x)
            
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualitites)
            
            #saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            logger.info(f"Model Eval params logged to {Path(self.config.metric_file_name)}")
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            #Model registry does not work with file store
            if tracking_url_type_store != "file":
                
                #register the model
                #there are other ways to use the model registry, which depends on the use case
                #please refer to the docs
                
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")

            else:
                mlflow.sklearn.log_model(model, "model")
            
            logger.info("Model Eval logged to mlflow repo!")