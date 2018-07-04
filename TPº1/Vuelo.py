import datetime

class Vuelo(object):
    __avion = None
    __fecha_salida = None
    __hora_salida = None
    __origen = None
    __destino = None

    def __init__(self):
        self.__lista_pasajeros = []
        self.__lista_tripulacion = []

    # SETS
    def setAvion(self, avion_object):
        self.__avion = avion_object

    def setListaPasajeros(self, pasaj):
        self.__lista_pasajeros.append(pasaj)

    def setListaTripulacion(self, trip):
        self.__lista_tripulacion.append(trip)

    def setFechaSalida(self, ano, mes, dia):
        self.__fecha_salida = datetime.date(ano, mes, dia)

    def setHoraSalida(self, hora, minuto):
        self.__hora_salida = datetime.time(hora, minuto)

    def setOrigen(self, origen):
        self.__origen = origen

    def setDestino(self, destino):
        self.__destino = destino

    # GETS
    def getAvion(self):
        return self.__avion

    def getListaPasajeros(self):
        return self.__lista_pasajeros

    def getListaTripulacion(self):
        return self.__lista_tripulacion

    def getFechaSalida(self):
        return self.__fecha_salida

    def getHoraSalida(self):
        return self.__hora_salida

    def getOrigen(self):
        return self.__origen

    def getDestino(self):
        return self.__destino