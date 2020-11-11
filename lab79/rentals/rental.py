

class Rental:
    counter = 0

    def __init__(self, client_id, book_id):
        """
        This function create a Rental
        :param client_id: int
        :param book_id: int
        """
        self._client_id = client_id
        self._book_id = book_id

    @property
    def client_id(self):
        """
        User id getter
        :return: user id
        """
        return self._client_id

    @property
    def book_id(self):
        """
        Boot id getter
        :return: book id
        """
        return self._book_id

    def __repr__(self):
        return f'<Client id: {self._client_id}, Book id: {self._book_id}>'


def test_rental():
    client_id = 3
    book_id = 5
    rental = Rental(3, 5)
    assert rental._client_id == client_id
    assert rental.book_id == book_id


test_rental()
