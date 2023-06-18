from authit.entities.user import User
from authit.providers.storage.fileSystem import FileSystemStorage


class BaseRepository:
    def __init__(self):
        self.provider = FileSystemStorage("fi")

    