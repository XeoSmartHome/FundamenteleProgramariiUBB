from lab79.books.book import Book
from lab79.books_list.books_list import BooksList
from lab79.clients.client import Client
from lab79.clients.cnp_validator import is_valid_cnp
from lab79.clients_list.clients_list import ClientsList
from lab79.rentals.rental import Rental
from lab79.rentals.rentals_list import RentalsList
from lab79.service.book_service import BookService


class Tests:
    def __init__(self):
        pass

    def test_client(self):
        name = 'john'
        cnp = '1234567890123'
        client = Client(name, cnp)
        assert client.name == name
        assert client.cnp == cnp

    def test_book(self):
        book = Book('a', 'b', 'c')

        assert book.title == 'a'
        assert book.description == 'b'
        assert book.author == 'c'

    def test_rental(self):
        client_id = 3
        book_id = 5
        rental = Rental(3, 5)
        assert rental._client_id == client_id
        assert rental.book_id == book_id

    def test_clients_list(self):
        clients = ClientsList()
        client = Client('Vadim', '1234567890123')
        clients.add_client(client)

        assert clients.get_client_by_id(client.id).name == client.name
        assert clients.get_client_by_id(client.id).cnp == client.cnp

        clients.delete_client(client)

        assert len(clients.get_clients()) == 0

    def test_books_list(self):
        books = BooksList()
        book = Book('Carte', 'descriere', 'Becali')

        books.add_book(book)

        assert books.get_book_by_id(book.id) == book
        assert books.get_books() == [book]

        books.delete_book(book.id)

        assert len(books.get_books()) == 0

    def test_rental_list(self):
        client_id = 2

        rentals = RentalsList()
        rental = Rental(client_id, 4)

        rentals.add_rental(rental)

        assert rentals.get_rentals() == [rental]

        rentals.delete_rental(rental)

        assert len(rentals.get_rentals()) == 0

    def test_book_service(self):
        repository = BooksList()

        service = BookService(repository)

        assert service.books_list == repository

    def test_srv_add_book(self):
        repository = BooksList()
        service = BookService(repository)
        assert service.books_list == repository

    def srv_sterge_carte(self):
        repository = BooksList()
        service = BookService(repository)
        book = Book('a', 'b', 'c')
        service.books_list.add_book(book)
        assert service.get_books() == [book]

    def test_cnp_validator(self):
        assert is_valid_cnp('asdasd') == False
        assert is_valid_cnp('213123123') == False
        assert is_valid_cnp('1234567890123') == True

    def test_all(self):
        self.test_cnp_validator()
        self.test_client()
        self.test_book()
        self.test_rental()
        self.test_clients_list()
        self.test_books_list()
        self.test_rental_list()
        self.test_book_service()
        self.srv_sterge_carte()
