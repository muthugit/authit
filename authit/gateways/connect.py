from .user import UserGateway
from .role import RoleGateway


class ConnectionGateway(UserGateway, RoleGateway):
    def __init__(self):
        ...
