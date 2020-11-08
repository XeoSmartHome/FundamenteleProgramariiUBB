from sanziana.oaspete import Oaspete


lista_oaspeti = []


def adaugare_oaspete():
    nume = input("nume = ")
    prenume = input("prenume = ")
    oaspete_nou = Oaspete(nume, prenume)
    lista_oaspeti.append(oaspete_nou)


def actualizare_nume():
    nume = input("nume = ")
    prenume = input("prenume = ")

    for oaspete in lista_oaspeti:
        if oaspete.get_nume() == nume and oaspete.get_prenume() == prenume:
            nume_nou = input('nume nou = ')
            oaspete.set_nume(nume_nou)
            print('nume actualizat cu succes')
            return
    print('oaspetele nu a fost gasit')


def listare_oaspeti():
    for oaspete in lista_oaspeti:
        print(oaspete)


lista_funtionalitati = {
    "adaugare": adaugare_oaspete,
    "actualizare_nume": actualizare_nume,
    "listare_oaspeti": listare_oaspeti
}


while True:
    comanda = input('>')

    if comanda == 'exit':
        exit()
    elif comanda == "help":
        for func in lista_funtionalitati:
            print(func)
    elif comanda in lista_funtionalitati:
        lista_funtionalitati[comanda]()
    else:
        print('comanda invalida')


# bloc cod echivalent cu cel de mai sus
'''while True:
    comanda = input('>')

    if comanda == "adaugare":
        adaugare_oaspete()
    elif comanda == "actualizare_nume":
        actualizare_nume()
    elif comanda == "listare_oaspeti":
        listare_oaspeti()
    else:
        print('comanda invalida')'''
