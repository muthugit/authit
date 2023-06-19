import os
import unittest
from uuid import uuid4

from authit.entities.config import Config
from authit.entities.user import User
from authit.usecases.user.createUser import (CreateUserRequest,
                                             CreateUserUseCase)


class TestCreateUserUseCase(unittest.TestCase):
    """Create user"""

    def test01CreateValidUser(self):
        """Create valid user"""
        # Arrange
        userName = str(uuid4())
        user = User(
            userName=userName,
            password="dummy"
        )
        config = Config(
            storageEngine="fileSystem"
        )
        dto = CreateUserRequest(
            user=user
        )
        useCase = CreateUserUseCase(
            dto, config
        )

        # Act
        user = useCase.execute()

        # Assert
        self.assertEqual(True, os.path.exists(f"/tmp/user/{userName}.ait"))
