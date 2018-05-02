from class_alumno import Alumno
from class_profesor import Profesor
from class_plato import Plato
from class_pedido import Pedido

while True:
    print("Bienvenido al buffet del colegio")
    print("¿Qué desea realizar?")
    print("1. Realizar alguna acción con los platos")
    print("2. Realizar alguna acción con los profesores")
    print("3. Realizar alguna accion con los alumnos")
    print("4. Realizar alguna acción con los pedidos")
    opcion = input()

    if opcion == 1:
        print("¿Qué desea realizar con los platos?")
        print("1. Agregar Plato")
        print("2. Eliminar Plato")
        print("3. Modificar Plato")
        opcion2 = input()

        if opcion2 == 1:
            print("¿Qué nombre tiene el plato?")
            nombre = input()
            print("¿Cuánto sale el plato?")
            precio = input()
