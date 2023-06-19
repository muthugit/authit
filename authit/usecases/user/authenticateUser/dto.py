from dataclasses import dataclass
from authit.entities.user import User


@dataclass
class AuthenticateUserRequest:
    userName: str
    password: str

@dataclass
class AuthenticateUserResponse:
    user: User    

    def __post_init__(self):
        self.user.hashKey = "***"
        self.user.passwordHash = "***"