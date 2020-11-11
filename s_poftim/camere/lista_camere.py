

class ListaCamere:
    def __init__(self):
        self._camere = []

    def adauga_camera(self, camera):
        if camera in self._camere:
            raise ValueError('Camera exista deja in lista')
        self._camere.append(camera)

    def sterge_camera(self, nr_camera):
        for camera in self._camere:
            if camera.get_numar() == nr_camera:
                self._camere.remove(camera)

    def toate_camerele(self):
        return self._camere


def test_lista_camere():
    pass
