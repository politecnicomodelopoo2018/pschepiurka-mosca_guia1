from Tripulacion import Tripulacion


class Servicio(Tripulacion):

    def __init__(self):
        Tripulacion.__init__(self)
        self.__idiomas = []


    def setIdiomas(self, lenguaje):
        self.__idiomas.append(lenguaje)

    def getIdiomas(self):
        return self.__idiomas