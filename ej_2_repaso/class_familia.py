from ej_2_repaso.class_persona import Persona

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
        return False

    def promTotalFam(self):
        prom_total = 0
        for persona in self.miembros:
            prom_total += persona.promTotalCalorias()
        return prom_total/len(self.miembros)

    def menCaloriasFam(self):
        men_calorias = self.miembros[0].promTotalCalorias()

        for persona in self.miembros:
            if persona.promTotalCalorias() < men_calorias:
                men_calorias = persona.promTotalCalorias()
        return men_calorias

    def mayCaloriasFam(self):
        may_calorias = self.miembros[0]

        for persona in self.miembros:
            if persona.promTotalCalorias() > may_calorias.promTotalCalorias():
                may_calorias = persona
        return may_calorias
