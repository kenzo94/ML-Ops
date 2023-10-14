from mlProject.entity.config_entry import DataValidationConfig
import pandas as pd
from mlProject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema_keys = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False 
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                        logger.info(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                        logger.info(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e