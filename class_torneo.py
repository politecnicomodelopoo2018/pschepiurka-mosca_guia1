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

                print(combinations(equipos, 2))

        #for part in partidos_disp:
        #    for part_comp in partidos_disp:
        #        if part == part_comp: continue

         #       contador_coinciden = 0
         #       for i in range(2):
         #           for j in range(2):
         #               if part.getEquipos[i] == part_comp.getEquipos[j]:
         #                   contador_coinciden += 1

          #      if contador_coinciden >= 2:


