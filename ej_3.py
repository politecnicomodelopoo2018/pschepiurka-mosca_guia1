from class_equipo import Equipo
from random import randint

def randbool():
    ran = randint(1,2)
    if ran == 1:
        return True
    return False


eq = Equipo("Los Verdes", "Liniers")
disphoraria = []
for i in range(6):
    disphoraria.append([randbool(),randbool(),randbool()])
eq.setDispHoraria(disphoraria)
del disphoraria

lista_nombres = [
    "Hugo", "Enrique", "Ricardo", "Jorge", "Jeremias", "Chad", "Juan", "Alejandro", "Ramiro", "Johnson", "Raul", "Ricky",
    "Arturo", "Gerardo", "Ulises", "Pablo"
]

temp_nombres = lista_nombres
num_cap = randint(0,9)
for i in range(10):
    fechanac = str(randint(1,28)) + " " + str(randint(1,12)) + " " + str(randint(1979, 1999))
    es_cap = False
    if num_cap == i:
        es_cap = True

    id_nombre = randint(0, len(temp_nombres) - 1)
    eq.agregarJugador(temp_nombres[randint(0, len(temp_nombres) - 1)], fechanac, es_cap)
del lista_nombres
del num_cap

print("Jugadores para el equipo " + eq.getNombre() + " localizado en " + eq.getBarrio() + ":")
for i, jug in enumerate(eq.getJugadores()):
    cap = ""
    if eq.getCapitan() == i:
        cap = " [capitan]"
    print("Jugador #" + str(i + 1) + cap + ": " + jug.getNombre())

#print("Disp Horaria:")
#for disp in eq.getDispHoraria():
#