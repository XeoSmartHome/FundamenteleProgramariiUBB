from lab79.books.book import Book


class BooksList:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if book in self._books:
            raise ValueError('Book already in list')
        self._books.append(book)

    def delete_book(self, book_id):
        for book in self._books:
            if book.id == book_id:
                self._books.remove(book)

    def get_books(self):
        return self._books

    def get_book(self, book_id):
        for book in self._books:
            if book.id == book_id:
                return book
