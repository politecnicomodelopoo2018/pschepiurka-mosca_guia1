from Empleados_class import Empleado

class Empresa(object):
    nombre = None

    def __init__(self):
        self.lista_empleados = []

    def setNombre(self, n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    def encontrarEmp(self, emp_nom):
        for emp in self.lista_empleados:
            if emp.getNombre() == emp_nom:
                return emp

        return None

    def agregarEmpleado(self, emp_nom, emp_ape, emp_tel, emp_fec):
        if not self.encontrarEmp(emp_nom) == None:
            return False

        emp = Empleado()
        emp.setNombre(emp_nom)
        emp.setApellido(emp_ape)
        emp.setTelefono(emp_tel)
        emp.setFechaNac(emp_fec)

        self.lista_empleados.append(emp)

