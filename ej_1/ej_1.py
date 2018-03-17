from ej_1.alumno_class import Alumno
import datetime

julio = Alumno()

n = input("Ingrese su nombre: ")
julio.setNombre(n)

a = input("Ingrese su apellido: ")
julio.setApellido(a)

fn_y = int(input("Ingrese su año de nacimiento: "))
fn_m = int(input("Ingrese su mes de nacimiento: ")) % 12
fn_d = int(input("Ingrese su dia de nacimiento: ")) % 31
julio.setNacimiento(datetime.date(fn_y, fn_m, fn_d))

for item in range(4):
    nota = input("Ingrese una nota: ")
    julio.agregarNota(nota)

print(julio.getNombre()+ " " +julio.getApellido())

print(julio.getNacimiento())
print(julio.calcularEdad())

for item in julio.getNotas():
    print(item, end=", ")

print("\n")
