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
        emp = Empleado()
        emp.setNombre(emp_nom)
        emp.setApellido(emp_ape)
        emp.setTelefono(emp_tel)
        emp.setFechaNac(emp_fec)

        self.lista_empleados.append(emp)

    def porcAsistTotal(self, mes):
        if len(self.lista_empleados) == 0:
            return False

        porc = 0
        for emp in self.lista_empleados:
            porc += emp.porcAsistencia(mes)

        return porc / len(self.lista_empleados)