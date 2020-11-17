

class Book:
    counter = 1

    def __init__(self, title, description, author):
        """
        This function create a book
        :param title: str
        :param description: str
        :param author: str
        """
        self._id = Book.counter
        Book.counter += 1
        self.title = title
        self.description = description
        self.author = author

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Book must have a title')
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value == '':
            raise ValueError('Book must have a description')
        self._description = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if value == '':
            raise ValueError('Book must have an author')
        self._author = value

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'<ID: {self._id}, Title: {self._title}, Description: {self._description}, Author: {self._author}>'

