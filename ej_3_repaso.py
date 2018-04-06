from class_empresa import Empresa

nasa = Empresa()

nasa.nombre = "Nasa"

nasa.añadirEmpleado("Rodolfo", "Aguirre", 30658974, "Andorra", 85976532)
nasa.añadirEmpleado("Pedro", "Rodriguez", 31548679, "España", 26543187)
nasa.añadirEmpleado("Juan", "Perez", 31648795, "Argentina", 58718606)

llamada_inc = nasa.llamarEmpleado(nasa.lista_empleados[0].telefono, "Pedro", "Rodriguez")