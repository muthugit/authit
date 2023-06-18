import os
from uuid import uuid4
from .interface import StorageInterface
from authit.entities.base import BaseEntity
import pickle


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
        with open(filePath, 'rb') as file:
            return pickle.load(file=file)
