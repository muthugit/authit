from .interface import StorageInterface

class FileSystemStorage(StorageInterface):
    def __init__(self, config):
        pass

    def create(self, obj: str) -> str:
        return "CREATED"
