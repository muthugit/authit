from typing import Optional
from dataclasses import dataclass
from authit.entities.role import Role
from .base import BaseEntity
import bcrypt


@dataclass
class User(BaseEntity):
    userName: str
    password: str = ""
    passwordHash: str = ""
    userRole: Optional[Role] = None
    hashKey: str = ""
    _id: str = ""
    isHashed: bool = False

    def __post_init__(self):
        self._id = self.userName
        super().__post_init__()
        if not self.isHashed:
            self.password = self.password.encode('utf-8')
            self.hashKey = bcrypt.gensalt()
            self.passwordHash = bcrypt.hashpw(self.password, self.hashKey)
            self.isHashed = True
            self.password = "***"
