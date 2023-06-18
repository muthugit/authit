from dataclasses import dataclass
from authit.entities.role import Role


@dataclass
class User:
    userName: str
    passwordHash: str
    userRole: Role
    