from lab79.books.book import Book
from lab79.books.books_list import BooksList
from lab79.clients.client import Client
from lab79.clients.clients_list import ClientsList
from lab79.console import Console
from lab79.rentals.rentals_list import RentalsList
from lab79.rentals.rental import Rental


clients_list = ClientsList()
books_list = BooksList()
rentals_list = RentalsList()
console = Console()


client_1 = Client('abc', '1234567901112')
client_2 = Client('qwe', '1234567901122')

clients_list.add_client(client_1)
clients_list.add_client(client_2)


book_1 = Book('Title1', 'description1', 'author1')
book_2 = Book('Title2', 'description2', 'author2')
book_3 = Book('Title3', 'description3', 'author3')

books_list.add_book(book_1)
books_list.add_book(book_2)
books_list.add_book(book_3)


rentals_list.add_rental(Rental(client_1.id, book_1.id))
rentals_list.add_rental(Rental(client_1.id, book_2.id))


def list_all_clients(params: list):
    for client in clients_list.get_clients():
        print(client)


def add_client(params: list):
    name = input('name = ')
    cnp = input('cnp = ')
    clients_list.add_client(Client(name, cnp))
    print('client added')


def find_client_by_name(params: list):
    client_name = input('client name = ')
    print(clients_list.get_clients_by_name(client_name)[0])


def delete_client_by_id(params: list):
    client_id = int(input('client id = '))
    clients_list.delete_client(clients_list.get_client_by_id(client_id))
    print('client deleted')


def delete_client_by_cnp(params: list):
    cnp = input('cnp = ')
    clients_list.delete_client(clients_list.get_client_by_cnp(cnp))
    print('client deleted')


def list_all_books(params: list):
    for book in books_list.get_books():
        print(book)


def add_a_book(params: list):
    title = input('title name = ')
    description = input('book description = ')
    author = input('book author = ')
    books_list.add_book(Book(title, description, author))


def delete_book_by_id(params: list):
    book_id = int(input('book id = '))
    for book in books_list.get_books():
        if book.id == book_id:
            books_list.delete_book(book)
    print('book deleted')


def rent_a_book(params: list):
    client_id = input('client id = ')
    book_id = input('book id = ')
    rental = Rental(client_id, book_id)
    rentals_list.add_rental(rental)


def return_a_book(params: list):
    client_id = input('client id = ')
    book_id = input('book id = ')

    for rental in rentals_list.get_rentals():
        if rental.client_id == client_id and rental.book_id == book_id:
            rentals_list.delete_rental(rental)


def list_all_rentals(params: list):
    for rental in rentals_list.get_rentals():
        print(rental)


console.register_function(list_all_clients, 'list_clients', 'list all clients')
console.register_function(add_client, 'add_client', 'register new client in application')
console.register_function(delete_client_by_id, 'delete_client_by_id', 'delete a client by id')
console.register_function(delete_client_by_cnp, 'delete_client_by_cnp', 'delete a client by cnp')
console.register_function(find_client_by_name, 'find_client_by_name', 'search for clients with name x')

console.register_function(list_all_books, 'list_books', 'list all books')
console.register_function(add_a_book, 'add_book', 'add a book in list')
console.register_function(delete_client_by_id, 'delete_book_by_id', 'delete a book by id')

console.register_function(list_all_rentals, 'list_rentals', 'list all rentals')
console.register_function(rent_a_book, 'rent_book', 'rent a book')
console.register_function(return_a_book, 'return_book', 'return a book')

console.start()
