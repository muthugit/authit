from dataclasses import dataclass
from authr.entities.role import Role


@dataclass
class User:
    userName: str
    passwordHash: str
    userRole: Role
    