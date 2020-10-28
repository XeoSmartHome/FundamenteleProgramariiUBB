'''
14. Generați cel mai mic număr perfect mai mare decât un număr dat. Un număr este perfect daca
este egal cu suma divizorilor proprii. Ex. 6 este un număr perfect (6=1+2+3).
'''


def genereaza_nr_perfect(n):
    while True:
        n += 1
        suma_divizori = 0
        for d in range(1, n):
            if n % d == 0:
                suma_divizori += d
        if n == suma_divizori:
            return n


x = int(input('x = '))

print('cel mai mic nr perfect mai mare decat', x, 'este', genereaza_nr_perfect(x))
