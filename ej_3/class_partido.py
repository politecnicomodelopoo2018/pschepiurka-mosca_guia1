class Partido(object):
    def __init__(self, dia, horario, equipos = []):
        self.dia = dia
        self.horario = horario
        self.lista_equipos = equipos

    def getDia(self):
        return self.dia

    def getHorario(self):
        return self.horario

    def getEquipos(self):
        return self.lista_equipos