from abc import abstractmethod, ABC


class Downloader(ABC):
    @abstractmethod
    def _download_dataset(): ...
