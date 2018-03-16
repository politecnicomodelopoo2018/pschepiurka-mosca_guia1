from Empresa_class import Empresa
import datetime

e = Empresa()
e.setNombre("Kellogg's")
e.agregarEmpleado("Ulises", "Geronimo", "45722754", datetime.date(1992, 6, 12))

uli = e.encontrarEmp("Ulises")
uli.ingresoEmpresa(datetime.date(2018, 1, 12), datetime.time(5, 0, 0, 0))

