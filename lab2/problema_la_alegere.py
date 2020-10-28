'''
11. Numerele n1 si n2 au proprietatea P daca scrierile lor in baza 10 conțin
 aceleași cifre (ex. 2113 si 323121). Determinați daca doua numere naturale
 au proprietatea P
'''


n1 = input('n1 = ')
n2 = input('n2 = ')

f1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
f2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for cifra in n1:
    f1[int(cifra)] = 1

for cifra in n2:
    f2[int(cifra)] = 1


if f1 == f2:
    print(n1 + ' si ' + n2 + ' au proprietatea P')
else:
    print(n1 + ' si ' + n2 + ' nu au proprietatea P')
