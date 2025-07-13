import kagglehub
from .base import Downloader
import os
from typing import List


class KaggleDownloader(Downloader):
    def __init__(self, dataset: str = "mlg-ulb/creditcardfraud"):
        super().__init__()
        self.dataset = dataset
        self.handler = KaggleFileHandler()
        self.downloaded = None
    
    def _download_dataset(self):
        self.downloaded = kagglehub.dataset_download(self.dataset)
        return self.downloaded
    
    def get_avaiable_datasets(self) -> List:
        if not self.downloaded:
            self._download_dataset()
        return self.handler.list_paths(self.downloaded)
    
class KaggleFileHandler():
    @staticmethod
    def list_paths(path: str):
        return [os.path.join(path, file) for file in os.listdir(path)]