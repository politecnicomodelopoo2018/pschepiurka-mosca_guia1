import datetime


class Pedido(object):
    fecha_creacion = None
    hora_entrega = None
    persona = None
    se_entrego = False

    def __init__(self):
        self.lista_platos = []

    def setFecha(self):
        self.fecha_creacion = datetime.date.today()

    def setPlato(self, plato):
        self.lista_platos.append(plato)

    def setHora(self, tiempo):
        self.hora_entrega = tiempo

    def entregar(self):
        self.se_entrego = True