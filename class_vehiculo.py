class Vehiculo(object):
    patente = None
    cant_ruedas = None
    año_fabric = None

    def setPatente(self, num_pat):
        self.patente = num_pat

    def setCantRuedas(self, num_ruedas):
        self.cant_ruedas = num_ruedas

    def setAñoFabric(self, año):
        self.año_fabric = año