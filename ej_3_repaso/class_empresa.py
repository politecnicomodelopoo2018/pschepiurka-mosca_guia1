from ej_3_repaso.class_empleado import Empleado
from ej_3_repaso.class_llamada import Llamada
import datetime

class Empresa(object):
    nombre = None

    def __init__(self):
        self.lista_empleados = []
        self.lista_llamadas = []

    def añadirEmpleado(self, nombre, apellido, dni, pais, telefono):
        temp_emp = Empleado()

        temp_emp.setNombre(nombre)
        temp_emp.setApellido(apellido)
        temp_emp.setDNI(dni)
        temp_emp.setPaisResidente(pais)
        temp_emp.setTelefono(telefono)

        self.lista_empleados.append(temp_emp)

    def llamarEmpleado(self,telefono_origen, nombre, apellido):
        for empleado in self.lista_empleados:
            if empleado.nombre == nombre and empleado.apellido == apellido:
                temp_llamada = Llamada()

                temp_llamada.telefono_origen = telefono_origen
                temp_llamada.telefono_destino = empleado.telefono
                temp_llamada.fecha_inicial = datetime.date.today()

                return temp_llamada

        return False

    def colgarEmpleado(self, llamada_inc, duracion):