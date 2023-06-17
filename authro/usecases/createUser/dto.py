from dataclasses import dataclass
from authro.entities.user import User


@dataclass
class CreateUserRequest:
    user: User

@dataclass
class CreateUserResponse:
    user: User    