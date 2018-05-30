from ej_7.class_persona import Persona


class Alumno(Persona):
    division = None

    def setDivision(self, div):
        self.division = div
