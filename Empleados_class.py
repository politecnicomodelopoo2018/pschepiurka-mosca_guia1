import datetime

class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nacimiento = None

    def __init__(self):
        self.dias_asistencia = []
        self.lista_asistencias = []

    def setNombre(self, n):
        self.nombre = n
    def getNombre(self):
        return self.nombre

    def setApellido(self, a):
        self.apellido = a
    def getApellido(self):
        return self.apellido

    def setTelefono(self, t):
        self.telefono = t
    def getTelefono(self):
        return self.telefono

    def setFechaNac(self, f):
        self.fecha_nacimiento = f
    def getFechaNac(self):
        return self.fecha_nacimiento

    def setAsistencia(self, lista_asist):
        self.dias_asistencia = lista_asist
    def getAsistencia(self):
        return self.dias_asistencia

    def ingresoEmpresa(self, fecha, hora):
        self.lista_asistencias.append([fecha, hora])

    def porcAsistencia(self, mes):
        if len(self.lista_asistencias) == 0 or len(self.dias_asistencia) == 0:
            return False

