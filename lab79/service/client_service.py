from lab79.clients_list.clients_list import ClientsList


class ClientService:
    def __init__(self, client_repository):
        self.clients_list = client_repository
