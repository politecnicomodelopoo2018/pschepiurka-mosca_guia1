from class_jugador import Jugador

class Equipo(object):
    def __init__(self, nombre, barrio):
        self.nombre = nombre
        self.barrio = barrio

        self.lista_jugadores = []
        self.capitan = 0
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

    def getCapitan(self):
        return self.capitan

    def agregarJugador(self, nom, fechanac, es_capitan):
        if self.cant_jugadores >= 9: # Equipo lleno
            return None

        jug = Jugador(nom, fechanac, self.cant_jugadores)
        if es_capitan:
            self.capitan = self.cant_jugadores
        self.cant_jugadores += 1

        self.lista_jugadores.append(jug)

    def getJugadores(self):
        return self.lista_jugadores