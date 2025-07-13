import os
from frauddetect.simulator.downloader import KaggleDownloader


def test_download_dataset():
    downloader = KaggleDownloader()
    path = downloader._download_dataset()
    assert os.listdir(path) == ["creditcard.csv"]

def test_get_avaiable_datasets():
    downloader = KaggleDownloader()
    assert isinstance(downloader.get_avaiable_datasets(), list)