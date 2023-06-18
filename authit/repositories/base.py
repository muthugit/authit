from authit.entities.user import User
from authit.entities.config import Config
from authit.providers.storage.fileSystem import FileSystemStorage


class BaseRepository:
    def __init__(self, config: Config):
        if config.storageEngine == "fileSystem":
            self.provider = FileSystemStorage("fi")
        else:
            raise Exception("Invalid storage engine")

    