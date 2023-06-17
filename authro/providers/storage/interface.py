from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")



class StorageInterface(ABC):
    
    @abstractmethod
    def create(self, obj: T) -> R:
        ...
    
