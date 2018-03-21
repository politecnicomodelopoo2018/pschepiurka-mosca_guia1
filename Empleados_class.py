import datetime, calendar

class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fecha_nacimiento = None

    def __init__(self):
        self.dias_asistencia = []
        self.lista_ingresos = []

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
        self.lista_ingresos.append([fecha, hora])

    def porcAsistencia(self, mes):
        if len(self.lista_ingresos) == 0:
            return 0
        if len(self.dias_asistencia) == 0:
            return False

        año = datetime.date.today().year

        dias_asistir = 0
        for dia in range(calendar.monthrange(año, mes)[1]):
            dia_semana = datetime.date(año, mes, dia + 1).weekday()
            if dia_semana < 5: # Considerar unicamente lunes a viernes
                if self.dias_asistencia[dia_semana]:
                    dias_asistir += 1

        dias_asistidos = 0
        for ingreso in self.lista_ingresos:
            if ingreso[0].month == mes:
                dias_asistidos += 1

        return dias_asistidos / dias_asistir * 100