from ej_4.Empresa_class import Empresa
import datetime

nombre_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
def mostrarPorc(emp, año, mes):
    print("Porcentaje de ingreso de " + emp.getNombre() + " en el mes de " + nombre_meses[mes - 1] + ": " + str(emp.porcAsistencia(año, mes)) + "%")

año = datetime.date.today().year

e = Empresa()
e.setNombre("Kellogg's")
e.agregarEmpleado("Ulises", "Geronimo", "45722754", datetime.date(1992, 6, 12))
e.agregarEmpleado("Pablo", "Escobar", "54911457", datetime.date(1949, 12, 1))

# EMPLEADO ULISES
uli = e.encontrarEmp("Ulises")
uli.setAsistencia([True, False, False, False, True, False, False])

# Ingresos a la empresa en febrero
dias_ingreso = [2, 12, 16, 23]
for dia in dias_ingreso:
    uli.ingresoEmpresa(datetime.date(año, 2, dia), datetime.time(5, 0, 0, 0))
# Ingresos a la empresa en marzo
dias_ingreso = [5, 9, 12, 16, 19, 30]
for dia in dias_ingreso:
    uli.ingresoEmpresa(datetime.date(año, 3, dia), datetime.time(5, 0, 0, 0))

mostrarPorc(uli, año, 2)
mostrarPorc(uli, año, 3)

# EMPLEADO PABLO
pab = e.encontrarEmp("Pablo")
pab.setAsistencia([True, True, False, False, True, False, False])

# Ingresos a la empresa en febrero
dias_ingreso = [2, 5, 6, 9, 12, 13, 16, 19, 20, 23, 26, 27]
for dia in dias_ingreso:
    pab.ingresoEmpresa(datetime.date(2018, 2, dia), datetime.time(12, 30, 0, 0))
# Ingresos a la empresa en marzo
dias_ingreso = [2, 5, 6, 9, 12, 13, 16, 19, 20, 23, 26, 27, 30]
for dia in dias_ingreso:
    pab.ingresoEmpresa(datetime.date(2018, 3, dia), datetime.time(12, 30, 0, 0))

mostrarPorc(pab, año, 2)
mostrarPorc(pab, año, 3)

# Porcentajes de ingreso totales empresa
print("Porcentaje de asistencia total en el mes de " + nombre_meses[1] + ": " + str(e.porcAsistTotal(año, 2)) + "%")
print("Porcentaje de asistencia total en el mes de " + nombre_meses[2] + ": " + str(e.porcAsistTotal(año, 3)) + "%")