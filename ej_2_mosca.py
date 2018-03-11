# -*- coding: utf-8 -*-

class materia(object):
    nombre = None

    def __init__(self):
        self.lista_notas = []

    def setNombre(self, name):
        self.nombre = name

    def agregarNota(self, nota):
        self.lista_notas.append(nota)

    def promNotas(self):
        prom = 0
        for n in self.lista_notas:
            prom += n

        return prom / len(self.lista_notas)

    def menorNota(self):
        men = self.lista_notas[0]
        for item in self.lista_notas:
            if item < men:
                men = item

        return men

    def mayorNota(self):
        may = self.lista_notas[0]
        for item in self.lista_notas:
            if item > may:
                may = item

        return may

class alumno(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self):
        self.materias = []

    def setNombre(self, name):
        self.nombre = name.title()

    def getNombre(self):
        return self.nombre

    def setApellido(self, lastname):
        self.apellido = lastname.title()

    def setNacimiento(self, date):
        self.fecha_nacimiento = date

    def agregarMateria(self, mater):
        self.lista_materias.append(mater)

    def promNotasTotal(self):
        prom = 0
        for mat in self.materias:
            prom += mat.promNotas()

        return prom / len(self.materias)

    def menorProm(self):
        men = None
        for mat in self.materias:
            mat_prom = mat.promNotas()
            if men == None or mat_prom < men:
                men = mat_prom

        return men

    def mayorProm(self):
        may = None
        for mat in self.materias:
            mat_prom = mat.promNotas()
            if may == None or mat_prom > may:
                may = mat_prom

        return may

alum = alumno()
alum.setNombre("Jorge")
alum.setApellido("Gonzalez")

mat = materia()
mat.setNombre("matematicas")

alum.agregarMateria(mat)