

class Consola:
    def __init__(self):
        self._lista_functionalitati = {}

    def start(self):
        comanda = input('>')
        if comanda in self._lista_functionalitati:
            self._lista_functionalitati[comanda]()
        else:
            print('comanda invalida')

