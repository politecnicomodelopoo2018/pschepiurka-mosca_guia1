from class_persona import Persona


class Autor(Persona):
    nacionalidad = None

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad