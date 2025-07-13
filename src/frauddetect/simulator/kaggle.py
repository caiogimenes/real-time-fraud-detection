from .iterator import KaggleIterator
from .downloader import KaggleDownloader
from .base import Simulator


class KaggleSimulator(Simulator):
    def __init__(self, source: str = None):
        super().__init__()
        if source:
            self.downloader = KaggleDownloader(source)
        else:
            self.downloader = KaggleDownloader()
            
        self.iterator = None
        self.selected_data = None

    def show_avaiable_data(self):
        self.avaiable_data = self.downloader.get_avaiable_datasets()
        for i, file in enumerate(self.avaiable_data):
            print(i,'--->\t', file)

    def select_data(self, index: int):
        path = self.avaiable_data[index]
        self.selected_data = path
        self.iterator = KaggleIterator(path)
    
    @property
    def stream(self):
        return self.iterator.stream