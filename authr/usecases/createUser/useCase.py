from .dto import CreateUserRequest, CreateUserResponse
from authr.usecases.iUseCase import IUseCase


class CreateUserUseCase(IUseCase):
    def __init__(self, request: CreateUserRequest) -> None:
        self.request = request

    def execute(self) -> CreateUserResponse:
        return self.request.user