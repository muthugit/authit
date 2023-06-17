import os
from uuid import uuid4
from .interface import StorageInterface
import pickle


class FileSystemStorage(StorageInterface):
    def __init__(self, config):
        pass

    def create(self, tbl: str, obj: str) -> str:
        directory = os.path.join("/tmp", tbl)
        os.makedirs(directory, exist_ok=True)
        with open(f'/tmp/{tbl}/{str(uuid4())}.pkl', 'ab') as dbfile:
            pickle.dump(obj, dbfile)
        return f"/tmp/{tbl}"
