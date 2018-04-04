import datetime


class Persona(object):
    nombre = None
    fecha_nacimiento = None

    def __init__(self):
        self.comida_consumida = []

    def personaComer(self, comida):
        self.comida_consumida.append(comida)


    def promTotalCalorias(self):
        sum_calorias = 0

        for comida in self.comida_consumida:
            sum_calorias += comida.calorias
        return sum_calorias/len(self.comida_consumida)

