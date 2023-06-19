from dataclasses import dataclass
from authit.entities.user import User


@dataclass
class AuthenticateUserRequest:
    userName: str
    password: str

@dataclass
class AuthenticateUserResponse:
    user: User    