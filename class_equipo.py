class Equipo(object):
    def __init__(self, nombre, barrio):
        self.nombre = nombre
        self.barrio = barrio

        self.lista_jugadores = []
        self.capitan = 0

        self.disp_horaria = []

    def set_jugadores(self, jugadores, cap):
        self.lista_jugadores = jugadores
        self.capitan = cap