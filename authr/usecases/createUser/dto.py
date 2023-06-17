from dataclasses import dataclass
from authr.entities.user import User


@dataclass
class CreateUserRequest:
    user: User

@dataclass
class CreateUserResponse:
    user: User    