from .dto import AuthenticateUserRequest, AuthenticateUserResponse
from authit.entities.config import Config
from authit.usecases.iUseCase import IUseCase
from authit.repositories.user import UserRepository
import bcrypt 

class AuthenticateUserUseCase(IUseCase):
    def __init__(self, request: AuthenticateUserRequest, config: Config) -> None:
        self.request = request
        self.repository = UserRepository(config=config)

    def execute(self) -> AuthenticateUserResponse:
        user = self.repository.selectUser(self.request.userName)
        self.request.password = self.request.password.encode('utf-8')
        passwordHash = bcrypt.hashpw(self.request.password, user.hashKey)
        if passwordHash == user.passwordHash:    
            res = AuthenticateUserResponse(user=user)
            return res
        else:
            raise Exception("Authentication failed")