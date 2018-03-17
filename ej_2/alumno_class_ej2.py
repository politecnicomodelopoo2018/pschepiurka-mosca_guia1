import datetime
from ej_2.materia_class import Materia


class Alumno(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self):
        self.lista_materias = []

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
        edad = datetime.date.today().year - self.fecha_nacimiento.year
        if datetime.date.today().month >= self.fecha_nacimiento.month:
            if datetime.date.today().day >= self.fecha_nacimiento.day:
                return edad
        return edad - 1

    def encontrarMat(self, nombre_mat):
        for item in self.lista_materias:
            if item.getNombre() == nombre_mat:
                return item
        return False

    def agregarMateria(self, nombre_mat):
        if not self.encontrarMat(nombre_mat) == False:
            return False

        temp_mat = Materia()
        temp_mat.setNombre(nombre_mat)
        self.lista_materias.append(temp_mat)

    def agregarNota(self, nombre_mat, nota):
        mat = self.encontrarMat(nombre_mat)
        if mat == False:
            return False
        mat.agregarNota(nota)

    def promMat(self, nombre_mat):
        mat = self.encontrarMat(nombre_mat)
        if not mat == False:
            return mat.promNota()

    def getMenorNota(self, nombre_mat):
        mat = self.encontrarMat(nombre_mat)
        if not mat == False:
            return mat.menorNota()

    def promedioMats(self):
        suma = 0
        for item in self.lista_materias:
            suma += item.promNota()
        return suma/len(self.lista_materias)

    def mayProm(self):
        if len(self.lista_materias) == 0:
            return False
        may = self.lista_materias[0].promNota()
        for item in self.lista_materias:
            if item.promNota() > may:
                may = item
        return may

    def menProm(self):
        if len(self.lista_materias) == 0:
            return False
        men = self.lista_materias[0].promNota()
        for item in self.lista_materias:
            if item.promNota() < men:
                men = item
        return men
