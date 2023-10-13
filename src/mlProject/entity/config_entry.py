from dataclasses import dataclass
from pathlib import Path

# class to save configurations for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path