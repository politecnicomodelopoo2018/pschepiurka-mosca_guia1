from class_persona import Persona
from class_comida import Comida
import datetime

class Familia:
    apellido = None

    def __init__(self):
        self.miembros = []

    def ingresarMiembro(self, nombre, fecha_nac):
        temp_pers = Persona()

        temp_pers.nombre = nombre
        temp_pers.fecha_nacimiento = fecha_nac

        self.miembros.append(temp_pers)

    def getPromCaloriasPers(self, nombre):
        for persona in self.miembros:
            if persona.nombre == nombre:
                return persona.promTotalCalorias()

    def promTotalFam(self):
        prom_total = 0
        for persona in self.miembros:
            prom_total += persona.promTotalCalorias()
        return prom_total/len(self.miembros)
