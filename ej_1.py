# -*- coding: utf-8 -*-

class alumno(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    lista_notas = []

    def __init__(self):
        self.lista_notas = []

    def setNombre(self, name):
        self.nombre = name.title()

    def getNombre(self):
        return self.nombre

    def setApellido(self, lastname):
        self.apellido = lastname.title()

    def setNacimiento(self, date):
        self.fecha_nacimiento = date

    def agregarNota(self, note):
        self.lista_notas.append(note)

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

    def promNota(self):
        nota_total = 0
        for item in self.lista_notas:
            nota_total += item
        return nota_total / len(self.lista_notas)


julio = alumno()

n = input("Ingrese su nombre: ")
julio.setNombre(n)

a = input("Ingrese su apellido: ")
julio.setApellido(a)


