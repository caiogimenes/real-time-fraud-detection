from .base import Iterator
import os
from river.stream import iter_csv


class KaggleIterator(Iterator):
    def __init__(self):
        super().__init__()

    def read_dataset(self, path: str, filename: str):
        self.stream = iter_csv(os.path.join(path, filename))
        return iter_csv(os.path.join(path, filename))

    def get_new_instance(self):
        for instance in self.read_dataset(self.stream):
            yield instance
