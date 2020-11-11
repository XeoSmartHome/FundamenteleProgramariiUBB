import json


class ListaOaspeti:
    def __init__(self):
        self._oaspeti = []

    def adauga_oaspete(self, oaspete):
        self._oaspeti.append(oaspete)

    def sterge_oaspete(self, oaspete):
        if oaspete in self._oaspeti:
            self._oaspeti.remove(oaspete)

    def toti_oaspeti(self):
        return self._oaspeti

    def incarca_oaspeti_din_fisier(self, nume_fisier):
        with open(nume_fisier, 'r+') as fisier:
            pass
            # self._oaspeti = json.loads(fisier.read())

    def salveaza_oaspeti_in_fisier(self, nume_fisier):
        lista_oaspeti = []
        for oaspete in self._oaspeti:
            lista_oaspeti.append({
                'nume': oaspete.get_nume(),
                'prenume': oaspete.get_prenume()
            })
        with open(nume_fisier, 'w+') as fisier:
            fisier.write(json.dumps(lista_oaspeti))

    def cauta_oaspete(self, nume, prenume):
        for oaspete in self._oaspeti:
            if oaspete.get_nume() == nume and oaspete.get_prenume() == prenume:
                return oaspete
        raise ValueError('Oaspetele nu a fost gasit')


def test_lista_oaspeti():
    pass
