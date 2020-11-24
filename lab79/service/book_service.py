import random
import string

from lab79.books.book import Book
from lab79.books_list.books_list import BooksList


class BookService:
    def __init__(self, book_repository):
        self.books_list = book_repository

    def create_book(self, title, description, author):
        """
        Register a book
        :param title: str
        :param description: str
        :param author: str
        :return: None
        """
        self.books_list.add_book(Book(title, description, author))

    def delete_book_by_id(self, book_id):
        """
        This function delete a book by id
        :param book_id: int
        :return: None
        """
        for book in self.books_list.get_books():
            if book.id == book_id:
                self.books_list.delete_book(book)

    def get_book_by_id(self, id):
        """
        Cauta o carte dupa id si o
        """
        return self.books_list.get_book_by_id(id)

    def generate_random_book(self):
        """
        Genereaza o carte random si o adauga in lista de carti
        """
        title = ''.join(random.choice(string.ascii_uppercase))
        title += ''.join((random.choice(string.ascii_lowercase) for i in range(random.randint(3, 11))))

        description = ''.join(random.choice(string.ascii_uppercase))
        description += ' '.join(
            (
                ''.join((random.choice(string.ascii_lowercase) for i in range(random.randint(3, 11))))
                for i in range(random.randint(1, 6))
             )
        )

        author = ''.join(random.choice(string.ascii_uppercase))
        author += ''.join((random.choice(string.ascii_lowercase) for i in range(random.randint(3, 11))))
        author += ' '
        author += ''.join(random.choice(string.ascii_uppercase))
        author += ''.join((random.choice(string.ascii_lowercase) for i in range(random.randint(3, 11))))

        self.create_book(title, description, author)

    def generate_n_random_books(self, nr):
        """
        Functia adauga in lista de cartii <nr> cati generate random
        """
        for i in range(nr):
            self.generate_random_book()

    def get_books(self):
        """
        Returneaza toate cartiile existente
        """
        return self.books_list.get_books()
