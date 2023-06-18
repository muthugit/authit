from .dto import CreateUserRequest, CreateUserResponse
from authit.usecases.iUseCase import IUseCase
from authit.repositories.user import UserRepository
from authit.entities.config import Config


class CreateUserUseCase(IUseCase):
    def __init__(self, request: CreateUserRequest, config: Config) -> None:
        self.request = request
        self.repository = UserRepository()
        self.config = config

    def execute(self) -> CreateUserResponse:
        self.repository.createUser(self.request.user)
        return self.request.user