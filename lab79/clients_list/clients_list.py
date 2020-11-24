from lab79.clients.client import Client


class ClientsList:
    def __init__(self):
        self._clients = []

    def add_client(self, client):
        """
        Add a client ad the end of the list
        :raise ValueError: if client already exist
        :param client: Client
        """
        # if client in self._clients:
        #    raise ValueError('Client already in list')
        self._clients.append(client)

    def delete_client(self, client):
        """
        sterge un client din lista
        daca clientul nu exista nu arunca eroare
        """
        if client in self._clients:
            self._clients.remove(client)

    def get_clients(self):
        """
        returneaza toti clientii din lista
        """
        return self._clients

    def get_client_by_id(self, client_id):
        """
        cauta un client dupa id si il returneza daca il gaseste
        altfel arunca Exception
        """
        for client in self._clients:
            if client.id == client_id:
                return client
        raise Exception('Client not found')

    # def get_clients_by_name(self, name):
    #    return list(filter(lambda client: client.name == name, self._clients))

    def get_client_by_cnp(self, cnp):
        """
        cauta un client dupa CNP si il returneza daca il gaseste
        altfel arunca Exception
        """
        for client in self._clients:
            if client.cnp == cnp:
                return client

