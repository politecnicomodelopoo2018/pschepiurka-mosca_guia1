class Jugador(object):
    def __init__(self, nombre, fechanac, num_cam, es_cap = False):
        self.nombre = nombre
        self.fecha_nac = fechanac
        self.camiseta = num_cam
        self.capitan = es_cap

    def getNombre(self):
        return self.nombre

    def getCamiseta(self):
        return self.camiseta

    def esCapitan(self):
        return self.capitan