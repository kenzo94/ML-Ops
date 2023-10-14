import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entry import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        
    def train_test_split(self) -> bool:
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Train-Test-Split was successful!")
        logger.info(f"Train-shape{train.shape}")
        logger.info(f"Test-shape{test.shape}")