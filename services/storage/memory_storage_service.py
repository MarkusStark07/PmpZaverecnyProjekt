from typing import override

from services.storage.abstract_storage_service import AbstractStorageService


class MemoryStorageService(AbstractStorageService):
    def __init__(self):
        if not hasattr(self, "data"):
            self.data = {}

    @override
    def save(self, key, value):
        self.data[key] = value

    @override
    def get(self, key):
        return self.data.get(key, "")