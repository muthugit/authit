from typing import TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class IUseCase(ABC):
    def __init__(self, request: T) -> None:
        self.request = request

    @abstractmethod
    def execute(self) -> T:
        ...

    