from app.services.storage.memory_storage_service import MemoryStorageService
from app.services.singleton_service import SingletonService

# Singletonová implementácia config úložiska
class ConfigStorageService(SingletonService, MemoryStorageService):
    pass