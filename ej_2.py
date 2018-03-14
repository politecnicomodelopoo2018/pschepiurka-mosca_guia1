from alumno_class_ej2 import Alumno
import datetime

adolfito = Alumno()

n = input("Ingrese su nombre: ")
adolfito.setNombre(n)

a = input("Ingrese su apellido: ")
adolfito.setApellido()

fn_y = int(input("Ingrese su año de nacimiento: "))
fn_m = int(input("Ingrese su mes de nacimiento: ")) % 12
fn_d = int(input("Ingrese su dia de nacimiento: ")) % 31
adolfito.setNacimiento(datetime.date(fn_y, fn_m, fn_d))


