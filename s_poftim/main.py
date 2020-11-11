"""
Un hotel dorește o aplicație, astfel încât să poată monitoriza mai bine comportamentul oaspeților.
Fiecare oaspete are un nume, prenume și o listă de rezervări.
Fiecare rezervare are unul sau mai mulți oaspeți, o cameră și o perioadă/ un interval de timp.
Fiecare cameră are un număr, numarul de oaspeți posibili, un preț, o culoare
și poate avea sau nu o priveliste. De asemenea, puteți vedea când este gratuit.
Un oaspete poate veni la hotel de mai multe ori și există posibili oaspeți care încă nu au facut rezervare.

Aplicația ar trebui să aibă următoarele funcționalități:

Meniu oaspeti:
• Adăugați un oaspete nou
• Actualizați numele de familie al unui oaspete
• Ștergerea unui oaspete
• Afișați lista de oaspeti

Camere meniu:
• Adăugați o cameră
• Actualizați prețul unei camere
• Ștergerea unei camere
• Afișați lista camerelor

Meniu comun:
• Fă o rezervare
• Vizualizați lista de oaspeți care au rezervări curente
• Afișați toate camerele filtrate cu criterii de preț și vedere la mare (de exemplu, o cameră mai ieftină de 100 de euro, cu vedere la mare)
• Afișați toate camerele care sunt libere astăzi


Vedere tehnică:
• Aplicația ar trebui să fie o aplicație consolă cu un meniu (de exemplu opțiunea 1: Adăugați oaspete; opțiunea 2: Modificați numele de familie; etc);
• Aplicația trebuie sa aiba o listă de oaspeți și o listă de camere înainte de inceputul aplicației;
• Trebuie să distribuiți funcționalitatea in functie de scop în module. (de exemplu, un modul pentru
oaspeti, un modul pentru camere, un modul pentru funcționalitate comună);
• Fiecare metodă trebuie să aibă comentarii;
• Codul trebuie să fie clar și ușor de înțeles;
• Fiecare funcționalitate trebuie să aibă propriul test

"""
from s_poftim.camere.lista_camere import ListaCamere
from s_poftim.oaspeti.lista_oaspeti import ListaOaspeti
from s_poftim.oaspeti.oaspete import Oaspete


lista_oapeti = ListaOaspeti()
lista_camere = ListaCamere()



lista_oapeti.adauga_oaspete(Oaspete('a', 'b'))


class Rezervare:
    def __init__(self, lista_oaspeti, numar_camera, data_inceput, data_sfarsit):
        self._lista_oaspeti = lista_oaspeti
        self._numar_camera = numar_camera
        self._data_inceput = data_inceput
        self._data_sfarsit = data_sfarsit


def fa_o_rezervare():
    nr_oaspeti = int(input('nr oaspeti = '))
    oaspeti = []

    for i in range(nr_oaspeti):
        nume = input('nume = ')
        prenume = input('prenume = ')
        oaspeti.append(
            lista_oapeti.cauta_oaspete(nume, prenume)
        )

    nr_camera = int(input('numar camera = '))
    data_inceput = input('data inceput = ')
    data_sfarsit = input('data sfarsit = ')

    rezervare = Rezervare(lista_oapeti, nr_camera, data_inceput, data_sfarsit)


fa_o_rezervare()
