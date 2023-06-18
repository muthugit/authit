from .dto import LoadUserRequest, LoadUserResponse
from authit.usecases.iUseCase import IUseCase
from authit.repositories.user import UserRepository


class LoadUserUseCase(IUseCase):
    def __init__(self, request: LoadUserRequest) -> None:
        self.request = request
        self.repository = UserRepository()

    def execute(self) -> LoadUserResponse:
        user = self.repository.selectUser(self.request.userName)
        res = LoadUserResponse(user=user)
        return res