from authro.entities.user import User
from authro.providers.storage.fileSystem import FileSystemStorage


class BaseRepository:
    def __init__(self):
        self.provider = FileSystemStorage("fi")

    