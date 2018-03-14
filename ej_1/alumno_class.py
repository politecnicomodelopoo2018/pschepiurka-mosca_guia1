import datetime

class Alumno(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self):
        self.lista_notas = []

    def setNombre(self, name):
        self.nombre = name.title()

    def getNombre(self):
        return self.nombre

    def setApellido(self, lastname):
        self.apellido = lastname.title()

    def getApellido(self):
        return self.apellido

    def setNacimiento(self, date):
        self.fecha_nacimiento = date

    def getNacimiento(self):
        return self.fecha_nacimiento

    def calcularEdad(self):
        edad = datetime.date.today().year-self.fecha_nacimiento.year
        if datetime.date.today().month >= self.fecha_nacimiento.month:
            if datetime.date.today().day >= self.fecha_nacimiento.day:
                return edad
        return edad-1

    def agregarNota(self, note):
        self.lista_notas.append(note)

    def getNotas(self):
        return self.lista_notas

    def menorNota(self):
        return min(self.lista_notas)

    def mayorNota(self):
        return max(self.lista_notas)

    def promNota(self):
        return sum(self.lista_notas)/len(self.lista_notas)
