from dataclasses import dataclass
from authro.entities.role import Role


@dataclass
class User:
    userName: str
    passwordHash: str
    userRole: Role
    