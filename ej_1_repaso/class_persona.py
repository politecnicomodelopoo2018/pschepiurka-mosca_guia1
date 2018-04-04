from ej_1_repaso.class_medicion import Medicion

class Persona(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self):
        self.revisiones = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setFechaNac(self, date):
        self.fecha_nacimiento = date

    def getFechaNac(self):
        return self.fecha_nacimiento

    def setMedicion(self, peso, altura, fecha):
        temp_class = Medicion()

        temp_class.peso = peso
        temp_class.altura = altura
        temp_class.fecha_check = fecha

        self.revisiones.append(temp_class)

    def getMedicion(self, fecha):
        for item in self.revisiones:
            if item.fecha_check == fecha:
                return item
        return False

    def getPromMedicionPeso(self, año):
        sum_peso = 0
        cont_año = 0
        for item in self.revisiones:
            if item.fecha_check.year == año:
               sum_peso += item.peso
               cont_año += 1
        if cont_año == 0:
            return False
        return sum_peso/cont_año

    def getPromMedicionAltura(self, año):
        sum_altura = 0
        cont_año = 0
        for item in self.revisiones:
            if item.fecha_check.year == año:
               sum_altura += item.altura
               cont_año += 1
        if cont_año == 0:
            return False
        return sum_altura/cont_año

    def getProgresoAltura(self, año, año2):
        prog_1 = self.getPromMedicionAltura(año)
        prog_2 = self.getPromMedicionAltura(año2)

        return (1 - (prog_1/prog_2)) * 100

    def getProgresoPeso(self, año, año2):
        prog_1 = self.getPromMedicionPeso(año)
        prog_2 = self.getPromMedicionPeso(año2)

        return (1 - (prog_1 / prog_2)) * 100