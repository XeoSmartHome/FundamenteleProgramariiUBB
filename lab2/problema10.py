'''
10. Pentru un număr natural n dat găsiți numărul natural minim m format cu
 aceleași cifre. Ex. n=3658, m=3568.
'''

frecventa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = input("n = ")

for cifra in n:
    frecventa[int(cifra)] += 1

m = 0

cifra = 1
while cifra < 10:
    if frecventa[cifra] != 0:
        m = m * 10 + cifra
        frecventa[cifra] -= 1
        cifra = 11
    cifra += 1

for cifra in range(0, 10):
    for i in range(frecventa[cifra]):
        m = m * 10 + cifra


print("m =", m)
