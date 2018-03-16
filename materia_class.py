class Materia(object):
    nombre = None

    def __init__(self):
        self.lista_notas = []

    def setNombre(self, name):
        self.nombre = name.title()

    def getNombre(self):
        return self.nombre

    def agregarNota(self, note):
        self.lista_notas.append(note)

    def getNotas(self):
        return self.lista_notas

    def menorNota(self):
        return min(self.lista_notas)

    def mayorNota(self):
        return max(self.lista_notas)

    def promNota(self):
        return sum(self.lista_notas) / len(self.lista_notas)