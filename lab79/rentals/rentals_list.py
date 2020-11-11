

class RentalsList:
    def __init__(self):
        self._rentals = []

    def add_rental(self, rental):
        """
        Add a rental ad the end of the list
        :param rental: Rental
        """
        if rental in self._rentals:
            raise ValueError('Rental already in list')
        self._rentals.append(rental)

    def delete_rental(self, client):
        if client in self._rentals:
            self._rentals.remove(client)

    def get_rentals(self):
        return self._rentals


def test_rental():
    pass


test_rental()
