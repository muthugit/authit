from .dto import CreateUserRequest, CreateUserResponse
from authro.usecases.iUseCase import IUseCase
from authro.repositories.user import UserRepository


class CreateUserUseCase(IUseCase):
    def __init__(self, request: CreateUserRequest) -> None:
        self.request = request
        self.repository = UserRepository()

    def execute(self) -> CreateUserResponse:
        self.repository.createUser(self.request.user)
        return self.request.user