from typing import TypeVar
from abc import ABC, abstractmethod
from authit.entities.config import Config

T = TypeVar("T")


class IUseCase(ABC):
    def __init__(self, request: T, config: Config) -> None:
        self.request = request
        self.config = config

    @abstractmethod
    def execute(self) -> T:
        ...

    