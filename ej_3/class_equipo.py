from ej_3.class_jugador import Jugador

class Equipo(object):
    def __init__(self, nombre, barrio):
        self.nombre = nombre
        self.barrio = barrio

        self.lista_jugadores = []
        self.cant_jugadores = 0

        self.disp_horaria = []

    def getNombre(self):
        return self.nombre

    def getBarrio(self):
        return self.barrio

    def getDispHoraria(self):
        return self.disp_horaria
    def setDispHoraria(self, disph):
        self.disp_horaria = disph

    def disponible_en(self, dia, horario):
        return self.disp_horaria[dia][horario]

    def agregarJugador(self, nom, fechanac, es_capitan):
        if self.cant_jugadores >= 10: # Equipo lleno
            return None

        jug = Jugador(nom, fechanac, self.cant_jugadores, es_capitan)
        self.cant_jugadores += 1

        self.lista_jugadores.append(jug)

    def getJugadores(self):
        return self.lista_jugadores