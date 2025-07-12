from abc import abstractmethod, ABC


class Iterator(ABC):
    @abstractmethod
    def read_dataset():...
    
    @abstractmethod
    def get_new_instance(): ...


class Instance(ABC): ...
