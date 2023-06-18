from authit.usecases.createUser import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from authit.entities.user import User, Role

class UserGateway:
    def __init__(self) -> None:
        pass

    def createUser(
            self,
            userName: str,
            passwordHash: str,
            userRole: str
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