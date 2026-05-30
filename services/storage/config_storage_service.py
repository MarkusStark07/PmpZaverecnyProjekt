from services.storage.memory_storage_service import MemoryStorageService
from services.singleton_service import SingletonService

# Singletonová implementácia config úložiska
class ConfigStorageService(SingletonService, MemoryStorageService):
    pass