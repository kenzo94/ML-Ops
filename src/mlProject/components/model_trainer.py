import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib
from mlProject.entity.config_entry import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config
        
    def train(self) -> bool:
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
        logger.info("Train the model....")
        
        path=os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(lr, path)
        logger.info(f"Training was successful. Dump the model in [{path}]")