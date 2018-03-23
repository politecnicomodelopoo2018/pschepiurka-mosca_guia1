from class_equipo import Equipo
from class_partido import Partido

class Torneo(object):
    def __init__(self, nombre):
        self.nombre = nombre

        self.lista_partidos = []
        self.lista_equipos = []

    def getNombre(self):
        return self.nombre

    def agregarEquipo(self, equipo):
        self.lista_equipos.append(equipo)

    def crearPartido(self, dia, horario, equipos):
        p = Partido(dia, horario, equipos)