from authit.entities.config import Config
from authit.repositories.user import UserRepository
from authit.usecases.iUseCase import IUseCase

from .dto import LoadUserRequest, LoadUserResponse


class LoadUserUseCase(IUseCase):
    def __init__(self, request: LoadUserRequest, config: Config) -> None:
        self.request = request
        self.repository = UserRepository(config=config)

    def execute(self) -> LoadUserResponse:
        user = self.repository.selectUser(self.request.userName)
        res = LoadUserResponse(user=user)
        return res
