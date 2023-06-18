from typing import Optional
from dataclasses import dataclass
from authit.entities.role import Role
from .base import BaseEntity


@dataclass
class User(BaseEntity):
    userName: str
    passwordHash: str
    userRole: Optional[Role] = None
    _id: str = ""

    def __post_init__(self):
        self._id = self.userName
        super().__post_init__()

    

    