from class_equipo import Equipo
from class_torneo import Torneo
from random import randint, seed

def randbool():
    ran = randint(1,2)
    if ran == 1:
        return True
    return False

def generar_disph():
    disphoraria = []
    for i in range(6):
        disphoraria.append([randbool(), randbool(), randbool()])
    return disphoraria

lista_nombres = [
    "Hugo", "Enrique", "Ricardo", "Jorge", "Jeremias", "Chad", "Juan", "Alejandro", "Ramiro", "Johnson", "Raul", "Ricky",
    "Arturo", "Gerardo", "Ulises", "Pablo"
]

def generar_jugadores(equipo):
    temp_nombres = lista_nombres
    num_cap = randint(0, 9)
    for i in range(10):
        fechanac = str(randint(1, 28)) + " " + str(randint(1, 12)) + " " + str(randint(1979, 1999))
        es_cap = False
        if num_cap == i:
            es_cap = True

        jug_nombre = temp_nombres[randint(0, len(temp_nombres) - 1)]
        equipo.agregarJugador(jug_nombre, fechanac, es_cap)
        temp_nombres.remove(jug_nombre)

seed()

equipos = []
# Equipo Los Verdes de Liniers
eq_lv = Equipo("Los Verdes", "Liniers")
eq_lv.setDispHoraria(generar_disph())
generar_jugadores(eq_lv)
equipos.append(eq_lv)

eq_lr = Equipo("Los Rojos", "Lanus")
eq_lr.setDispHoraria(generar_disph())
generar_jugadores(eq_lr)
equipos.append(eq_lr)

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
for eq in equipos:
    print("Jugadores para el equipo " + eq.getNombre() + " localizado en " + eq.getBarrio() + ":")
    for i, jug in enumerate(eq.getJugadores()):
        cap = ""
        if jug.esCapitan():
            cap = " [capitan]"
        print("Jugador #" + str(i + 1) + cap + ": " + jug.getNombre())

    print("Disponibilidad Horaria:")
    for i, disp in enumerate(eq_lv.getDispHoraria()):
        lista_disp = ""
        if disp[0]:
            lista_disp += " Mañana "
        if disp[1]:
            lista_disp += " Tarde "
        if disp[2]:
            lista_disp += " Noche "
        if lista_disp == "":
            lista_disp = "No disponible"
        print("Disponibilidad " + dias_semana[i] + ": " + lista_disp)

obj_torneo = Torneo("Invitacional Liniers 2018")
