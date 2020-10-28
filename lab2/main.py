'''
Cerințe:
 Rezolvați in timpul laboratorului următoarele probleme:
• Calculați suma a n numere naturale
• Verificați daca un număr citit de la tastatura este prim
• Calculați cel mai mare divizor comun a doua numere
'''


def suma_a_n_numere():
    n = int(input("n= "))
    suma = 0
    for i in range(n):
        suma += int(input('a[' + str(i) + ']= '))
    print("suma este:", suma)


def este_prim(nr):
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def cmmdc(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


program = int(input("selectare program (1/2/3): "))


if program == 1:
    print("suma a n numere")
    suma_a_n_numere()

elif program == 2:
    print("este prim?")
    n = int(input("n= "))
    print(este_prim(n))

elif program == 3:
    print("CMMDC")
    x = int(input("a= "))
    y = int(input("b= "))

    print("cmmdc= ", cmmdc(x, y))

# tema: problema 10
