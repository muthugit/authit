from authit.entities.config import Config

from .role import RoleGateway
from .user import UserGateway


class ConnectionGateway(UserGateway, RoleGateway):
    def __init__(self, storageEngine: str = "fileSystem"):
        self.config = Config(storageEngine=storageEngine)
