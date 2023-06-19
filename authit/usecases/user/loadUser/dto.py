from dataclasses import dataclass
from authit.entities.user import User


@dataclass
class LoadUserRequest:
    userName: str

@dataclass
class LoadUserResponse:
    user: User    

    def __post_init__(self):
        self.user.hashKey = "***"
        self.user.passwordHash = "***"