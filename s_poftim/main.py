from s_poftim.oaspete import Oaspete


lista_oaspeti = []  # inilializare lista cu oaspeti


def adaugare_oaspete():
    nume = input("nume = ")
    prenume = input("prenume = ")
    oaspete_nou = Oaspete(nume, prenume)  # creare obiect de tip oaspete
    lista_oaspeti.append(oaspete_nou)  # adaugare obiect in lista cu oaspeti


def actualizare_nume():
    nume = input("nume = ")
    prenume = input("prenume = ")

    for oaspete in lista_oaspeti:
        if oaspete.get_nume() == nume and oaspete.get_prenume() == prenume:  # cauta daca oaspetele exista
            nume_nou = input('nume nou = ')
            oaspete.set_nume(nume_nou)  # daca exista, actualizeaza numele
            print('nume actualizat cu succes')
            return  # daca numele a fost executat iesi din functie
    print('oaspetele nu a fost gasit')


def listare_oaspeti():
    for oaspete in lista_oaspeti:  # afiseaza fiecare oaspete din lista de oaspeti
        print(oaspete)


lista_funtionalitati = {  # lista_funtionalitati este o variabila de tip dictionar
    "adaugare": adaugare_oaspete,
    "actualizare_nume": actualizare_nume,
    "listare_oaspeti": listare_oaspeti
}


while True:
    comanda = input('>')  # citeste o comanda de la utilizator

    if comanda == 'exit':
        exit()  # functie care termina executia programului
    elif comanda == "help":
        for func in lista_funtionalitati:  # afisarea tuturor functionalitatiilor aplicatiei
            print(func)
    elif comanda in lista_funtionalitati:  # verifica daca comanda este in dinctionarul de functionalitati
        lista_funtionalitati[comanda]()  # daca comanda exista, executa functionalitatea corespunzatoare comenzii
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
