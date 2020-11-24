from lab79.clients.client import Client
from lab79.clients_list.clients_list import ClientsList
import random
import string


class ClientService:
    def __init__(self, client_repository):
        self.clients_list = client_repository

    def add_client(self, name, cnp):
        """
        Add client in clients list
        :param name: str, client name
        :param cnp: str, client cnp
        :return:
        """
        self.clients_list.add_client(Client(name, cnp))

    def get_clients(self):
        """
        :return: list of all clients
        """
        return self.clients_list.get_clients()

    def get_client_by_name(self, client_name):
        """
        Get client by name
        :param client_name: str
        :return: client
        :raises ValueError if client not found
        """
        return self.clients_list.get_clients_by_name(client_name)[0]

    def delete_client_by_id(self, client_id):
        """
        This function delete a client by id, can raise Value error if client not found
        :type client_id: int
        :return: None
        """
        self.clients_list.delete_client(self.clients_list.get_client_by_id(client_id))

    def generate_random_client(self):
        name = ''.join(random.choice(string.ascii_uppercase))
        name += ''.join((random.choice(string.ascii_lowercase) for i in range(random.randint(3, 11))))
        cnp = ''.join((random.choice(string.digits) for i in range(13)))
        self.add_client(name, cnp)

    def generate_n_random_clients(self, nr):
        for i in range(nr):
            self.generate_random_client()

    def get_client_by_id(self, id):
        return self.clients_list.get_client_by_id(id)
