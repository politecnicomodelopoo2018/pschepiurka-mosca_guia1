from class_vehiculo import Vehiculo

class Camioneta(Vehiculo):
    capacidad_kg = None

    def setCapacidad(self, cap_kg):
        self.capacidad_kg = cap_kg