import os
import pickle
from uuid import uuid4

from authit.entities.base import BaseEntity
from authit.providers.errors import AuthenticationException

from .interface import StorageInterface


class FileSystemStorage(StorageInterface):
    def __init__(self, config):
        pass

    def create(self, tbl: str, obj: BaseEntity) -> str:
        directory = os.path.join("/tmp", tbl)
        os.makedirs(directory, exist_ok=True)
        filePath = os.path.join(directory, f"{obj._id}.pkl")
        if os.path.exists(filePath):
            raise ValueError("Data exists")
        with open(filePath, 'ab') as dbfile:
            pickle.dump(obj, dbfile)
        return f"/tmp/{tbl}"

    def select(self, tbl: str, key: str):
        directory = os.path.join("/tmp", tbl)
        filePath = os.path.join(directory, f"{key}.pkl")
        if not os.path.exists(filePath):
            raise AuthenticationException("Invalid username.")
        with open(filePath, 'rb') as file:
            return pickle.load(file=file)
