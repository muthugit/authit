from authit.usecases.user.createUser import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from authit.usecases.user.loadUser import LoadUserRequest, LoadUserUseCase
from authit.entities.user import User, Role


class UserGateway:
    def __init__(self) -> None:
        pass

    def createUser(
        self,
        userName: str,
        passwordHash: str,
        userRole: str | None = None
    ) -> User:
        user = User(
            userName=userName,
            passwordHash=passwordHash,
            userRole=Role(
                userRole
            )
        )
        dto = CreateUserRequest(user=user)
        useCase = CreateUserUseCase(dto)
        return useCase.execute()
    
    def selectUser(
            self,
            userName: str
    ) -> User:
        dto = LoadUserRequest(
            userName=userName
        )
        useCase = LoadUserUseCase(dto)
        return useCase.execute().user
