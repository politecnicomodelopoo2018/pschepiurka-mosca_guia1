from db import DB


class Materia(object):
    idMateria = None
    nombre = None

    def setMateria(self, id, nom):
        self.idMateria = id
        self.nombre = nom