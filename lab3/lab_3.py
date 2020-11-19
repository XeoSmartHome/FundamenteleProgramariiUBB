'''
Lab 3 – Fundamentele programării
Se predă în săptămâna 3
Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
1 Citirea unei liste de numere intregi
2,3 Gasirea secventelor de lungime maxima care respectă o proprietatea dată. Fiecare student primeste 2 proprietati din lista
de mai jos.
4 Iesire din aplicatie.
Documentatia să contină:
 Scenarii de rulare pentru cele două cerinte primite (vezi curs 1 – scenarii de rulare)
 Cazuri de testare pentru cele doua cerinte în format tabelar (vezi curs 1 – cazuri de testare)
Se cauta secventa de lungime maximă cu proprietatea:
9. p=1 sau in oricare trei elemente consecutive exista o valoarea care se repeta.
13. suma elementelor este egal cu 5
8. au toate elementele in intervalul [0, 10] dat
'''

#muie la canguri
#mare muie la canguri
#muie la canguri

def read_list():
    global lista
    lista = []
    try:
        n = int(input('numar_elemente = '))

        for i in range(n):
            lista.append(int(input('lista[%d] = ' % i)))
    except ValueError:
        print('ValueError')
        return

    print('Lista citita')


def secventa_maxima_9():
    """
    9. p=1 sau in oricare trei elemente consecutive exista o valoarea care se repeta.
    """
    if len(lista) <= 2:
        return lista[0]
    anterior_1 = lista[0]
    anterior_2 = lista[1]

    l_max = 2
    l = 2
    temp_secv = [anterior_1, anterior_2]
    secx_max = temp_secv

    for nr in lista[2:]:
        if anterior_1 == anterior_2 or nr == anterior_1 or nr == anterior_2:
            l += 1
            temp_secv.append(nr)
            if l_max < l:
                l_max = l
                secx_max = temp_secv
        else:
            l = 2
            temp_secv = [anterior_2, nr]

        anterior_1 = anterior_2
        anterior_2 = nr
    if len(secx_max) < 3:
        return []
    return secx_max


def secventa_maxima_13():
    """
    13. suma elementelor este egal cu 5
    """
    lungime = len(lista)

    for lungime_curenta in range(lungime, 1, -1):
        for i in range(0, lungime - lungime_curenta + 1):
            if sum(lista[i:lungime_curenta + i]) == 5:
                return lista[i:lungime_curenta + i]


def test_secventa_maxima_13():
    pass


def secventa_maxima_8():
    """
    :return: secventa maxima cu toate elementele cuprinse in intervalul [0, 10]
    """
    lungime_secventa_curenta = 0
    lungime_maxima = 0
    raspuns = []

    for i in range(len(lista)):
        if 0 <= lista[i] <= 10:
            lungime_secventa_curenta += 1
            if lungime_secventa_curenta > lungime_maxima:
                lungime_maxima = lungime_secventa_curenta
                raspuns = [lista[i - lungime_secventa_curenta + 1: i + 1]]
            elif lungime_secventa_curenta == lungime_maxima:
                raspuns.append(lista[i - lungime_secventa_curenta + 1: i + 1])
        else:
            lungime_secventa_curenta = 0

    # return lista[sfarsit_secventa_maxima - lungime_maxima + 1: sfarsit_secventa_maxima + 1]
    return raspuns


def test_all():
    test_secventa_maxima_13()


def main():
    while True:
        aux = input('>>').split(' ')
        comanda = aux[0]
        optiuni = aux[1:]

        if comanda == 'exit':
            break

        elif comanda == 'read':
            read_list()

        elif comanda == 'smax':
            if len(optiuni) == 0:
                p = 0
            else:
                p = int(optiuni[0])
            if p == 9:
                print('Secventa maxima cu proprietatea 9 este:', secventa_maxima_9())
            elif p == 13:
                print('Secventa maxima cu proprietatea 13 este:', secventa_maxima_13())
            elif p == 8:
                print('Secventele maxime cu proprietatea 8 sunt:', secventa_maxima_8())
            else:
                print('Comanda incorecta')
                print('Folositi "smax <p>", unde <p> este:')
                print('8    toate elementele sunt in intervalul [0, 10]')
                print('9    oricare trei elemente consecutive exista o valoarea care se repeta')
                print('13   suma elementelor este egal cu 5')

        elif comanda == 'help' or comanda == 'h':
            print('Lista comenzi:')
            print('help         Lista comenzi')
            print('read         Citire lista de numere')
            print('smax <p>     Calculeaza secventa maxima cu proprietatea p')
            print('exit         Inchidere program')

        else:
            print('Comanda necunoscuta "%s"' % comanda)
            print('Folositi "help" pentru afisarea comenzilor disponibile')


test_all()
main()
