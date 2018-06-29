from Persona import Persona


class Tripulacion(Persona):

    def __init__(self):
        self.aviones_habilitados = []

    def setAviones(self, avion):
        self.aviones_habilitados.append(avion)

    def getAviones(self):
        return self.aviones_habilitados