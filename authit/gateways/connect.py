from .user import UserGateway
from .role import RoleGateway
from authit.entities.config import Config


class ConnectionGateway(UserGateway, RoleGateway):
    def __init__(self, storageEngine: str = "fileSystem"):
        self.config = Config(storageEngine=storageEngine)
