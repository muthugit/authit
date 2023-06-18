from authit.entities.user import User
from authit.entities.config import Config
from .base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, config: Config):
        super().__init__(config=config)


    def createUser(self, user: User):
        self.provider.create("user", user)
        print("User created")

    def selectUser(self, userName: str) -> User:
        return self.provider.select("user", userName)