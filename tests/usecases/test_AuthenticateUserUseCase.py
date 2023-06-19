import os
import unittest
from uuid import uuid4

from authit.entities.config import Config
from authit.entities.user import User
from authit.usecases.user.createUser import (CreateUserRequest,
                                             CreateUserUseCase)
from authit.usecases.user.authenticateUser import (
    AuthenticateUserRequest, AuthenticateUserUseCase
)


class TestAuthenticateUserUseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.userName = "dummy"
        self.config = Config(
            storageEngine="fileSystem"
        )

    def test01_CreateValidUser(self):
        # Arrange
        if os.path.exists(f"/tmp/user/{self.userName}.ait"):
            os.remove(f"/tmp/user/{self.userName}.ait")
        userName = self.userName
        user = User(
            userName=userName,
            password="dummy"
        )

        dto = CreateUserRequest(
            user=user
        )
        useCase = CreateUserUseCase(
            dto, self.config
        )

        # Act
        user = useCase.execute()

        # Assert
        self.assertEqual(True, os.path.exists(f"/tmp/user/{userName}.ait"))

    def test02_Authenticate(self):
        # Arrange
        dto = AuthenticateUserRequest(
            self.userName,
            "dummy"
        )
        useCase = AuthenticateUserUseCase(
            dto, self.config
        )

        # Act
        user = useCase.execute()

        # Assert
        self.assertEqual(
            user.user.userName, self.userName
        )
