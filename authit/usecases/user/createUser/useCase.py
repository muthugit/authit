from authit.entities.config import Config
from authit.repositories.user import UserRepository
from authit.usecases.iUseCase import IUseCase

from .dto import CreateUserRequest, CreateUserResponse


class CreateUserUseCase(IUseCase):
    def __init__(self, request: CreateUserRequest, config: Config) -> None:
        self.request = request
        self.repository = UserRepository(config=config)

    def execute(self) -> CreateUserResponse:
        self.repository.createUser(self.request.user)
        return self.request.user