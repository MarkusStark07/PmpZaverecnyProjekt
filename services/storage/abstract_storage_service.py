from abc import abstractmethod, ABC

# Abstraktná trieda definujúca základné rozhranie
# pre operácie dátového úložiska
class AbstractStorageService(ABC):
    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass