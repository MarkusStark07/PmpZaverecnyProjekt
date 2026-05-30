from services.storage.memory_storage_service import MemoryStorageService
from services.singleton_service import SingletonService


class TestStorageService(SingletonService, MemoryStorageService):
    pass