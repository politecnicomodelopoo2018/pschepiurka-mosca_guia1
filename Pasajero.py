from Persona import Persona


class Pasajero(Persona):
    __vip = None
    __necesidades_especiales = None

    def setVIP(self, vip):
        self.__vip = vip

    def setNecesidadesEspeciales(self, necesidades):
        self.__necesidades_especiales = necesidades

    def getVIP(self):
        return self.__vip

    def getNecesidadesEspeciales(self):
        return self.__necesidades_especiales