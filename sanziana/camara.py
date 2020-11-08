
class Camera:
    def __init__(self, numar, numar_oaspeti, pret, culoare, priveliste=''):
        self.set_numar(numar)
        self.set_numar_oaspeti(numar_oaspeti)
        self.set_pret(pret)
        self.set_culoare(culoare)
        self.set_priveliste(priveliste)

    def set_numar(self, value):
        self._numar = value

    def get_numar(self):
        return self._numar

    def set_numar_oaspeti(self, value):
        self._numar_oaspeti = value

    def get_numar_oaspeti(self):
        return self._numar_oaspeti

    def set_pret(self, value):
        self._pret = value

    def get_pret(self):
        return self._pret

    def set_culoare(self, value):
        self._culoare = value

    def get_culoare(self):
        return self._culoare

    def set_priveliste(self, value):
        self._priveliste = value

    def get_priveliste(self):
        return self._priveliste

