from abc import abstractmethod, ABC


class Simulator(ABC):
    @abstractmethod
    def set_data_source(): ...

    @abstractmethod
    def set_data_format(): ...
