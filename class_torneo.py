from class_equipo import Equipo
from class_partido import Partido
from itertools import combinations

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

    def crearFixture(self):
        if len(self.lista_equipos) == 0:
            return False

        partidos_disp = []
        partidos_coinciden = []
        for dia in range(6):
            for hor in range(3):
                equipos = []
                for eq in self.lista_equipos:
                    if eq.disponible_en(dia, hor):
                        equipos.append(eq)

                for comb in list(combinations(equipos, 2)):
                    part = Partido(dia, hor, comb)
                    partidos_disp.append(part)

        partidos_comb = []
        for comb in list(combinations(partidos_disp, 2)):
            contador_comb = 0
            for i in range(2):
                for j in range(2):
                    if comb[0].getEquipos()[i].getNombre() == comb[1].getEquipos()[j].getNombre():
                        contador_comb += 1

            if contador_comb >= 2:
                añadio = False
                for c in partidos_comb:
                    if comb[0].getEquipos() == c[0]:
                        c[1] += 1
                        añadio = True

                if not añadio:
                    partidos_comb.append([comb[0].getEquipos(), 1])

        lista_fixture = []
        for p in partidos_comb:
            print(p[0][0].getNombre() + ' vs ' + p[0][1].getNombre() + ' x ' + str(p[1]))