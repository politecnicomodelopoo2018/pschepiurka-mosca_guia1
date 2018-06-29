import datetime

class Persona(object):
    __nombre = None
    __apellido = None
    __fecha_nac = None
    __dni = None

    def setNombre(self, nom):
        self.__nombre = nom

    def setApellido(self, apell):
        self.__apellido = apell

    def setFechaNac(self, ano, mes, dia):
        self.__fecha_nac = datetime.date(ano, mes, dia)

    def setDNI(self, dni):
        self.__dni = dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getFechaNac(self):
        return self.__fecha_nac

    def getDNI(self):
        return self.__dni