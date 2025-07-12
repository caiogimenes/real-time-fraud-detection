from kagglehub import dataset_download
from .base import Downloader
import os
from typing import List


class KaggleDownloader(Downloader):
    def __init__(self, dataset: str = "mlg-ulb/creditcardfraud"):
        super().__init__()
        self.dataset = dataset
        self.handler = KaggleFileHandler()
    
    def download_dataset(self):
        return dataset_download(self.dataset)
    
    def get_avaiable_datasets(self) -> List:
        return self.handler.list_paths(self.download_dataset())
    
class KaggleFileHandler():
    @staticmethod
    def list_paths(path: str):
        return [os.path.join(path, file) for file in os.listdir(path)]