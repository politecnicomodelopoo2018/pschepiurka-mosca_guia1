class Jugador(object):
    def __init__(self, nombre, fechanac, num_cam):
        self.nombre = nombre
        self.fecha_nac = fechanac
        self.camiseta = num_cam

    def getNombre(self):
        return self.nombre

    def getCamiseta(self):
        return self.camiseta