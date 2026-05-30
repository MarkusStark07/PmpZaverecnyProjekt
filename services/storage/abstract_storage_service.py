from abc import abstractmethod, ABC


class AbstractStorageService(ABC):
    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass