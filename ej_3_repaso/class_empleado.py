class Empleado(object):
    nombre = None
    apellido = None
    DNI = None
    pais_residente = None
    telefono = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setDNI(self, dni):
        self.DNI = dni

    def setPaisResidente(self, pais):
        self.pais_residente = pais

    def setTelefono(self, telefono):
        self.telefono = telefono


