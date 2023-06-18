from dataclasses import dataclass
from authit.entities.user import User


@dataclass
class LoadUserRequest:
    userName: str

@dataclass
class LoadUserResponse:
    user: User    