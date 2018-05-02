from ej_6.class_vehiculo import Vehiculo


class Auto(Vehiculo):
    es_descapotable = None

    def setDescapot(self, es_descap):
        self.es_descapotable = es_descap