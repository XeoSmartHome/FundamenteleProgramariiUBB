from s_poftim.oaspeti.oaspete import Oaspete
lista_oaspeti = []


def adauga_oaspete(lista, oaspete):
    lista_oaspeti.append(oaspete)
    return lista


def adauga_oaspete_interfata():
    nume = input("nume = ")
    prenume = input("prenume = ")
    o = Oaspete(nume, prenume)
    global lista_oaspeti
    lista_oaspeti = adauga_oaspete(lista_oaspeti, o)


def test_adauga_oaspete():
    l = []
    o = Oaspete('n', 'c')
    o2 = Oaspete('x', 'y')
    l = adauga_oaspete(l, o)
    l = adauga_oaspete(l, o2)
    assert l[0] == o
    assert l[1] == o2


lista_funtionalitati = {
    "adaugare": adauga_oaspete_interfata,
}

