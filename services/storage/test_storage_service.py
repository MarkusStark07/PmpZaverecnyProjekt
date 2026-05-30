from services.storage.memory_storage_service import MemoryStorageService
from services.singleton_service import SingletonService

# Singletonová implementácia testovacieho úložiska
class TestStorageService(SingletonService, MemoryStorageService):
    pass