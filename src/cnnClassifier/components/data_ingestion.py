import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    # constructor containg config variable with class name DataIngestionConfig
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # function download_file will download the file from url
    def download_file(self):
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok =True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            output = "Chest-CT-Scan-data.zip"
            gdown.download(url=dataset_url, output=zip_download_dir, fuzzy=True)
            logger.info(f"Data Downloaded from {dataset_url} into file {zip_download_dir}")
            
        except Exception as e:
            raise e

    # function extract_zip_file will extract zip file into directory
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(file=self.config.local_data_file, mode='r') as zip_ref:
            zip_ref.extractall(unzip_path)