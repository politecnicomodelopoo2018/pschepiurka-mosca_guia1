from class_alumno import Alumno
from class_profesor import Profesor
from class_plato import Plato
from class_pedido import Pedido

lista_alumnos = []
lista_profesores = []
lista_platos = []
lista_pedidos = []

while True:
    print("Bienvenido al buffet del colegio")
    print("¿Qué desea realizar?")
    print("1. Realizar alguna acción con los platos")
    print("2. Realizar alguna acción con los profesores")
    print("3. Realizar alguna accion con los alumnos")
    print("4. Realizar alguna acción con los pedidos")
    opcion = input("Opcion: ")

    if opcion == '1':
        print("¿Qué desea realizar con los platos?")
        print("1. Agregar Plato")
        print("2. Eliminar Plato")
        print("3. Modificar Plato")
        opcion2 = input("Opcion: ")

        if opcion2 == '1':
            temp_food = Plato

            print("¿Qué nombre tiene el plato?")
            nombre = input("Nombre: ").title()
            print("¿Cuánto sale el plato?")
            precio = input("Precio: ")

            temp_food.setNombre(nombre)
            temp_food.setPrecio(precio)

            lista_platos.append(temp_food)

        elif opcion2 == '2':
            print("¿Qué nombre tiene el plato que desea eliminar?")
            nombre = input("Nombre: ").title()

            for food in lista_platos:
                if food.nombre == nombre:
                    lista_platos.remove(food)
                    break
                else:
                    print("El plato ingresado es inexistente")

        elif opcion2 == '3':
            print("¿Qué nombre tiene el plato que quiere modificar?")
            nombre = input("Nombre: ").title()

            for food in lista_platos:
                if food.nombre == nombre:
                    print("¿Qué desea modificar?")
                    print("1. Nombre")
                    print("2. Precio")
                    print("3. Ambos")
                    opcion_modif = input("Opcion: ")

                    if opcion_modif == '1':
                        print("¿Cuál es el nuevo nombre?")
                        nomb = input("Nombre: ")


