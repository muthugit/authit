from authit.entities.user import User
from .base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()


    def createUser(self, user: User):
        self.provider.create("user", user.userName)
        print("User created")