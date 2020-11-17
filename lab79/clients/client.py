from lab79.clients.cnp_validator import is_valid_cnp


class Client:
    counter = 1

    def __init__(self, name, cnp):
        """
        This function create a client
        :raise ValueError if cnp is invalid, or is already in used
        :param name: str
        :param cnp: str
        """
        self._id = Client.counter
        Client.counter += 1
        self.name = name
        self.cnp = cnp

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Client must have a name')
        self._name = value

    @property
    def cnp(self):
        return self._cnp

    @cnp.setter
    def cnp(self, value):
        if not is_valid_cnp(value):
            raise ValueError('Invalid CNP')
        self._cnp = value

    def __repr__(self):
        return f'<ID:{self._id}, Name: {self._name}, CNP: {self._cnp}>'

    def __eq__(self, other):
        return self.id == other.id

