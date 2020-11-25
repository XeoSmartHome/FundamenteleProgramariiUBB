

class RentalService:
    def __init__(self, rental_repository):
        self.rentals_list = rental_repository

    def get_cele_mai_inchiriate_carti(self):
        """
        Functia returneaza o lista de tupluri
        Primul element din tuplu e id-ul cartii
        Al doilea element din tuplu este un nr ce reprezinta de cate ori a fost inchiriata cartea
        Tuplurile sunt ordonate descrescator dupa al doilea element al lor
        """
        books_dict = {}
        for rental in self.rentals_list.get_rentals():
            if rental.book_id in books_dict:
                books_dict[rental.book_id] += 1
            else:
                books_dict[rental.book_id] = 1

        return sorted(books_dict.items(), key=lambda x: x[1], reverse=True)

    def clienti_cu_cele_mai_multe_cati_inchiriate(self):
        """
        Functia returneaza o lista de tupluri
        Primul element din tuplu e id-ul clientului
        Al doilea element din tuplu este un nr ce reprezinta de cate cati a inchiriat clientul
        Tuplurile sunt ordonate descrescator dupa al doilea element al lor
        """
        clients_dict = {}
        for rental in self.rentals_list.get_rentals():
            if rental.client_id in clients_dict:
                clients_dict[rental.client_id] += 1
            else:
                clients_dict[rental.client_id] = 1

        return sorted(clients_dict.items(), key=lambda x: x[1], reverse=True)

    def clienti_cu_inchirieri_in_interval(self, minim, maxim):
        clients = self.clienti_cu_cele_mai_multe_cati_inchiriate()
        return list(filter(lambda x: minim <= x[1] <= maxim, clients))

    def add_rental(self, rental):
        """
        Adauga o inchiriere in lista de inchirieri
        """
        return self.rentals_list.add_rental(rental)
