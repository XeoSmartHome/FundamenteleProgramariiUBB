

class RentalsList:
    def __init__(self):
        self._rentals = []

    def add_rental(self, rental):
        """
        Add a rental at the end of the list
        :param rental: Rental
        """
        if rental in self._rentals:
            raise ValueError('Rental already in list')
        self._rentals.append(rental)

    def delete_rental(self, rental):
        """
        delete rental
        """
        if rental in self._rentals:
            self._rentals.remove(rental)

    def get_rentals(self):
        """
        REturneaza toate inchirierile existente
        """
        return self._rentals
