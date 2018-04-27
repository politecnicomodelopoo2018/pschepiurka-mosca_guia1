import datetime


class Persona(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFechaNac(self, año, mes, dia):
        self.fecha_nacimiento = datetime.date(año, mes, dia)