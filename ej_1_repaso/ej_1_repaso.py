from ej_1_repaso.class_persona import Persona
from random import randint
import datetime

alfred = Persona()

alfred.nombre = "Alfred"
alfred.apellido = "Alfred"
alfred.fecha_nacimiento = datetime.date(1990, 12, 12)

for i in range(2):
    peso = randint(1, 100)
    altura = randint(40, 160)
    fecha = datetime.date(1990, randint(1, 12), randint(1, 30))
    print(peso)
    print(altura)
    print(fecha)

    print("\n")

    alfred.setMedicion(peso, altura, fecha)

for i in range(2):
    peso = randint(1, 100)
    altura = randint(40, 160)
    fecha = datetime.date(2004, randint(1, 12), randint(1, 30))
    print(peso)
    print(altura)
    print(fecha)

    print("\n")

    alfred.setMedicion(peso, altura, fecha)

peso = 20
altura = 100
fecha = datetime.date(1991, 11, 24)

alfred.setMedicion(peso, altura, fecha)

print(alfred.getMedicion(fecha))
print(alfred.getPromMedicionPeso(2004))
print(alfred.getPromMedicionAltura(2004))
print(alfred.getProgresoPeso(1990, 2004))
print(alfred.getProgresoAltura(1990, 2004))