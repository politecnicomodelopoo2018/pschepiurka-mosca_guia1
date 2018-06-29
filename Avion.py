class Avion(object):
    __modelo = None
    __cant_pers = None
    __cant_trip_min = None

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setCantidadPersonas(self, cant_pers):
        self.__cant_pers = cant_pers

    def setCantidadTripulacionMinima(self, cant_min):
        self.__cant_trip_min = cant_min

    def getModelo(self):
        return self.__modelo

    def getCantidadPersonas(self):
        return self.__cant_pers

    def getCantidadTripulacionMinima(self):
        return self.__cant_trip_min