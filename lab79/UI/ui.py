import random

from lab79.books.book import Book
from lab79.clients.client import Client
from lab79.console.console import Console
from lab79.rentals.rental import Rental
from lab79.service.book_service import BookService
from lab79.service.client_service import ClientService


class Ui:
    def __init__(self, console: Console, client_service: ClientService, books_service: BookService, rentals_service):
        self.__console = console
        self.__client_service = client_service
        self.__books_service = books_service
        self.__rentals_service = rentals_service

        console.register_function(self.list_all_clients, 'list_clients', 'list all clients')
        console.register_function(self.add_client, 'add_client', 'register new client in application')
        console.register_function(self.delete_client_by_id, 'delete_client_by_id', 'delete a client by id')
        console.register_function(self.delete_client_by_cnp, 'delete_client_by_cnp', 'delete a client by cnp')
        console.register_function(self.find_client_by_name, 'find_client_by_name', 'search for clients with name x')

        console.register_function(self.list_all_books, 'list_books', 'list all books')
        console.register_function(self.add_a_book, 'add_book', 'add a book in list')
        console.register_function(self.delete_client_by_id, 'delete_book_by_id', 'delete a book by id')

        console.register_function(self.list_all_rentals, 'list_rentals', 'list all rentals')
        console.register_function(self.rent_a_book, 'rent_book', 'rent a book')
        console.register_function(self.return_a_book, 'return_book', 'return a book')

        console.register_function(self.generate_random_clients, 'random_clients')
        console.register_function(self.generate_random_books, 'random_books')
        console.register_function(self.generete_random_rentals, 'random_rentals')

        console.register_function(self.cele_mai_inchiriate_carti, 'best_books', 'Cele mai inchiriate cărți.')
        console.register_function(self.clienti_cu_cele_mai_multe_cati_inchiriate, 'active_clients', 'Clienți cu cărți închiriate ordonat dupa: nume, după numărul de cărți închiriate')
        console.register_function(self.primi_20_la_100_cei_mai_activi_clienti, 'active_clients_20', 'Primi 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)')

    def start(self):
        """
        start console application
        """
        self.__console.start()

    def list_all_clients(self, params: list):
        """
        Print all clients
        """
        for client in self.__client_service.get_clients():
            print(client)

    def add_client(self, params: list):
        """
        Add client to clist of clients
        """
        name = input('name = ')
        cnp = input('cnp = ')
        self.__client_service.add_client(name, cnp)
        print('client added')

    def find_client_by_name(self, params: list):
        client_name = input('client name = ')
        print(self.__client_service.get_client_by_name(client_name))

    def delete_client_by_id(self, params: list):
        """
        Delete client by name
        """
        client_id = int(input('client id = '))
        self.__client_service.delete_client_by_id(client_id)
        print('client deleted')

    def delete_client_by_cnp(self, params: list):
        """
        Delete client by cnp
        """
        cnp = input('cnp = ')
        self.__client_service.clients_list.delete_client(self.__client_service.clients_list.get_client_by_cnp(cnp))
        print('client deleted')

    def list_all_books(self, params: list):
        """
        Print all book from library
        """
        for book in self.__books_service.books_list.get_books():
            print(book)

    def add_a_book(self, params: list):
        """
        Add a book in list of books
        can raise Exception
        """
        title = input('title name = ')
        description = input('book description = ')
        author = input('book author = ')
        self.__books_service.create_book(title, description, author)

    def delete_book_by_id(self, params: list):
        """
        Delete a book by id
        can raise Exception
        """
        book_id = int(input('book id = '))
        self.__books_service.delete_book_by_id(book_id)
        print('book deleted')

    def rent_a_book(self, params: list):
        """
        Rent a book from library
        can raise Exception
        """
        client_id = int(input('client id = '))
        client = self.__client_service.clients_list.get_client_by_id(client_id)
        book_id = int(input('book id = '))
        book = self.__books_service.books_list.get_book_by_id(book_id)
        rental = Rental(client.id, book.id)
        self.__rentals_service.rentals_list.add_rental(rental)

    def return_a_book(self, params: list):
        """
        return a book to library
        can raise Exception
        """
        client_id = int(input('client id = '))
        client = self.__client_service.clients_list.get_client_by_id(client_id)
        book_id = int(input('book id = '))
        book = self.__books_service.books_list.get_book_by_id(book_id)

        for rental in self.__rentals_service.rentals_list.get_rentals():
            if rental.client_id == client_id and rental.book_id == book_id:
                self.__rentals_service.rentals_list.delete_rental(rental)
                print('Book returned')
                return

    def list_all_rentals(self, params: list):
        """
        Print all rentals
        """
        for rental in self.__rentals_service.rentals_list.get_rentals():
            print(rental)

    def generate_random_clients(self, params: list):
        n = int(input('clients number = '))
        self.__client_service.generate_n_random_clients(n)
        print('Random clients generated')

    def generate_random_books(self, params: list):
        n = int(input('books number = '))
        self.__books_service.generate_n_random_books(n)
        print('Random books generated')

    def generete_random_rentals(self, params: list):
        n = int(input('rentals number = '))
        for i in range(n):
            client_id = random.choice([client.id for client in self.__client_service.get_clients()])
            book_id = random.choice([book.id for book in self.__books_service.get_books()])
            self.__rentals_service.add_rental(Rental(client_id, book_id))
        print('Random rentals generated')

    def cele_mai_inchiriate_carti(self, params: list):
        for book_id, nr in self.__rentals_service.get_cele_mai_inchiriate_carti():
            print(self.__books_service.get_book_by_id(book_id).title + 'was rented ' + str(nr) + ' times')

    def clienti_cu_cele_mai_multe_cati_inchiriate(self, params: list):
        clients = self.__rentals_service.clienti_cu_cele_mai_multe_cati_inchiriate()
        clients = [(self.__client_service.get_client_by_id(client_id), nr) for client_id, nr in clients]
        clients = sorted(clients, key=lambda x: (-x[1], x[0].name))

        for client, nr in clients:
            print(client, ' rent ', nr, ' books')

    def primi_20_la_100_cei_mai_activi_clienti(self, params: list):
        clients = self.__rentals_service.clienti_cu_cele_mai_multe_cati_inchiriate()
        clients = [(self.__client_service.get_client_by_id(client_id), nr) for client_id, nr in clients]
        clients = sorted(clients, key=lambda x: (-x[1], x[0].name))

        l = len(clients)
        for i in range(l * 20 // 100 + 1):
            client, nr = clients[i]
            print(client.name, ' rent ', nr, ' books')
