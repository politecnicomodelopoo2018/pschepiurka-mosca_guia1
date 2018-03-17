from ej_2.alumno_class_ej2 import Alumno
import datetime

adolfito = Alumno()

#Ingresar Nombre
n = input("Ingrese su nombre: ")
adolfito.setNombre(n)

#Ingresar Apellido
a = input("Ingrese su apellido: ")
adolfito.setApellido(a)

#Ingresar Fecha de Nacimiento
fn_y = int(input("Ingrese su año de nacimiento: "))
fn_m = int(input("Ingrese su mes de nacimiento: ")) % 12
fn_d = int(input("Ingrese su dia de nacimiento: ")) % 31
adolfito.setNacimiento(datetime.date(fn_y, fn_m, fn_d))

#Crear Materia
nombreMat = input("Ingrese el nombre de la materia que desee crear: ").title()
adolfito.agregarMateria(nombreMat)

#Calcular Promedio
nombreMat = input("Ingrese el nombre de la materia en la que desee ingresar una nota: ").title()
for item in range(3):
    nota = int(input("Ingrese una nota: "))
    adolfito.agregarNota(nombreMat, nota)
print("El promedio de la materia es: " + str(adolfito.promMat(nombreMat)))

#Encontrar Menor Nota
nombreMat = input("Ingrese el nombre de una materia: ")
menorNota = adolfito.getMenorNota(nombreMat)
if menorNota == False:
    print("No se encontro la materia solicitada")
else:
    print("La menor nota de la materia es: " + str(menorNota))

#Promedio Notas Alumno
nombreMat = input("Ingrese el nombre de una materia: ")
adolfito.agregarMateria(nombreMat)
for item in range(4):
    nota = int(input("Ingrese una nota: "))
    adolfito.agregarNota(nombreMat, nota)
promAlumno = adolfito.promedioMats()
print("El promedio de " + adolfito.getNombre() + " es " + str(promAlumno))

#Menor Promedio
menProm = adolfito.menProm()
print("El menor promedio de " + adolfito.getNombre() + " es " + str(menProm))

#Mayor Promedio
mayProm = adolfito.mayProm()
print("El mayor promedio de " + adolfito.getNombre() + " es " + str(mayProm))