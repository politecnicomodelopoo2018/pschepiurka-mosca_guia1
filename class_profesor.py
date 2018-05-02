from class_persona import Persona


class Profesor(Persona):
    descuento = None

    def setDescuento(self, desc):
        self.descuento = desc