class Comida(object):

    def __init__(self):
        self.nombre = None
        self.calorias = None

    def crearComida(self, nombre, calorias):
        self.nombre = nombre
        self.calorias = calorias