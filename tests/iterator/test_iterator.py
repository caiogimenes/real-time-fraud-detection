from frauddetect.simulator.downloader import KaggleDownloader
from frauddetect.simulator.iterator import KaggleIterator


def test__set_stream():
    downloader = KaggleDownloader()
    paths = downloader.get_avaiable_datasets()
    iterator = KaggleIterator(paths[0])
    assert next(iterator.stream) != next(iterator.stream)
    assert isinstance(next(iterator.stream), tuple)