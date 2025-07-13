from .base import Iterator
import os
from river.stream import iter_csv


class KaggleIterator(Iterator):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.stream = self._set_stream()
        
    def _set_stream(self):
        return iter_csv(os.path.join(self.path))