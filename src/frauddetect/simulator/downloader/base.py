from abc import abstractmethod, ABC


class Downloader(ABC):
    @abstractmethod
    def download_dataset(): ...
