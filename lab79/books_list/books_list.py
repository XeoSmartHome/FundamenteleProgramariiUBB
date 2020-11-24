from lab79.books.book import Book


class BooksList:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """
        Adauga o carte in lista
        arunca eroare daca cartea deja exista
        """
        if book in self._books:
            raise ValueError('Book already in list')
        self._books.append(book)

    def delete_book(self, book_id):
        """
        sterge o carte, cautata dupa id
        """
        for book in self._books:
            if book.id == book_id:
                self._books.remove(book)

    def get_books(self):
        """
        returneaza toate cartiile din lista
        """
        return self._books

    def get_book_by_id(self, book_id):
        """
        cauta o carte dupa id
        arunca Exception daca nu gaseste cartea
        """
        for book in self._books:
            if book.id == book_id:
                return book
        raise Exception('Book not found')
