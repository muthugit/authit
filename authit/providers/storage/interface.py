from abc import ABC, abstractmethod
from typing import TypeVar

from authit.entities.base import BaseEntity

T = TypeVar("T")
R = TypeVar("R")


class StorageInterface(ABC):

    @abstractmethod
    def create(self, tbl: str, obj: BaseEntity) -> R:
        ...
