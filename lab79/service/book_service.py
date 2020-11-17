from lab79.books_list.books_list import BooksList


class BookService:
    def __init__(self, book_repository):
        self.books_list = book_repository

