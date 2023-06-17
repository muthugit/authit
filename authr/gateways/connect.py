from .user import UserGateway

class ConnectionGateway:
    def __init__(self):
        self.user = UserGateway()
