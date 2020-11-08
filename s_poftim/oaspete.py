

class Oaspete:
    def __init__(self, nume, prenume):
        """
        acesta functie este apelata cand este creat un obiect de tipul oaspete
        sintaxa:
        x = Oaspete("Vadim", "Tudor)
        """
        self.set_nume(nume)
        self.set_prenume(prenume)

    def get_nume(self):
        """
        Functie care returneaza numele unui oaspete
        """
        return self._nume

    def get_prenume(self):
        """
        Functie care returneaza prenumele unui oaspete
        """
        return self._prenume

    def set_nume(self, nume_nou):
        """
         Functie care seteaza numele unui oaspete
        """
        self._nume = nume_nou

    def set_prenume(self, prenume_nou):
        """
        Functie care seteaza prenumele unui oaspete
        """
        self._prenume = prenume_nou

    def __repr__(self):
        """
        Functie care returneaza reprezentarea unui obiect de tipul Oaspete,
        adica e e afisat de print(x), unde x e un oaspete,
        altfel e afisat ceva de genul "object ... at adress 0x12312de31"
        """
        return 'oaspete: ' + self._nume + ' ' + self._prenume



def test_oaspete():
    o = Oaspete('n', 'c')  # creaza oaspete de test
    assert o.get_nume() == 'n'  # verifica daca numele a fost setat ok
    assert o.get_prenume() == 'c'  # verifica daca prenumele a fost setat ok
    o.set_prenume('w')  # seteaza numele cu valoare 'w'
    assert o.get_prenume() == 'w'  # verifica daca numele a fost setat ok


test_oaspete()
