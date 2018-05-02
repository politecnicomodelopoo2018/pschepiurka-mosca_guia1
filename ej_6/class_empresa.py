from ej_6.class_auto import Auto
from ej_6.class_camioneta import Camioneta


class Empresa(object):
    nombre = None

    def __init__(self):
        self.lista_camionetas = []
        self.lista_autos = []

    def agregarAuto(self, pat, cant_ruedas, año_fabric, es_descap):
        temp_auto = Auto

        temp_auto.setPatente(pat)
        temp_auto.setCantRuedas(cant_ruedas)
        temp_auto.setAñoFabric(año_fabric)
        temp_auto.setDescapot(es_descap)

        self.lista_autos.append(temp_auto)

    def agregarCamioneta(self, pat, cant_ruedas, año_fabric, cap_kg):
        temp_camion = Camioneta

        temp_camion.setPatente(pat)
        temp_camion.setCantRuedas(cant_ruedas)
        temp_camion.setAñoFabric(año_fabric)
        temp_camion.setCapacidad(cap_kg)

        self.lista_camionetas.append(temp_camion)