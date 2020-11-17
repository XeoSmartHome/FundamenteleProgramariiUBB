from lab79.TEste.tests import Tests
from lab79.UI.ui import Ui
from lab79.books.book import Book
from lab79.books_list.books_list import BooksList
from lab79.clients.client import Client
from lab79.clients_list.clients_list import ClientsList
from lab79.console.console import Console
from lab79.rentals.rentals_list import RentalsList
from lab79.rentals.rental import Rental
from lab79.service.book_service import BookService
from lab79.service.client_service import ClientService
from lab79.service.rental_service import RentalService


tests = Tests()


def main():

    clients_repository = ClientsList()

    clients_service = ClientService(clients_repository)

    books_repository = BooksList()

    books_service = BookService(books_repository)

    console = Console()

    rentals_repo = RentalsList()

    rentals_srv = RentalService(rentals_repo)

    ui = Ui(console, clients_service, books_service, rentals_srv)

    ui.start()


tests.test_all()
main()
