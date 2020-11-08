

class Oaspete:
    def __init__(self, nume, prenume):
        self.set_nume(nume)
        self.set_prenume(prenume)

    def get_nume(self):
        return self._nume

    def get_prenume(self):
        return self._prenume

    def set_nume(self, nume_nou):
        self._nume = nume_nou

    def set_prenume(self, prenume_nou):
        self._prenume = prenume_nou

    def __repr__(self):
        return 'oaspete: ' + self._nume + ' ' + self._prenume



def test_oaspete():
    o = Oaspete('n', 'c')
    assert o.get_nume() == 'n'
    assert o.get_prenume() == 'c'
    o.set_prenume('w')
    assert o.get_prenume() == 'w'


test_oaspete()
