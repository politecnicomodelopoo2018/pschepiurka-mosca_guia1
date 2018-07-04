from TPº1 import Sistema
import os
bool = True

while bool:
    os.system("clear")
    print("\n Ejercicios disponibles: 1, 2, 3, 4, 5, 6, 7")
    print("Para salir ingrese 8 \n")
    opcion = int(input("Que ejercicio desea realizar?: "))

    if opcion == 1:
        temp_bool = True
        temp_bool2 = True

        while temp_bool2:
            print("Opciones: 1, 2")
            op = int(input("Desea ver los de un vuelo solo?  1. Si  2. No \n"))
            if op == 1:
                while temp_bool:
                    print("\n Vuelos disponibles: 1, 2, 3, 4")
                    nro_vuelo = int(input("Que vuelo desea seleccionar?: ")) - 1
                    if nro_vuelo >= 4:
                        print("\n Vuelva a ingresar el numero de vuelo \n")
                    else:
                        temp_bool = False

                pasajeros = Sistema.mostrarPasajerosVuelo(nro_vuelo)

                os.system("clear")
                for pasajero in pasajeros:
                    print("\n Nombre: " + pasajero.getNombre())
                    print("Apellido: " + pasajero.getApellido())
                    print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                    print("DNI: " + pasajero.getDNI())
                input("\n Presione una tecla para continuar...")
                temp_bool2 = False
            elif op == 2:
                pasajeros = Sistema.mostrarPasajerosVuelos()

                print(pasajeros)

                os.system("clear")
                for pasajero in pasajeros:
                    print("\n Nombre: " + pasajero.getNombre())
                    print("Apellido: " + pasajero.getApellido())
                    print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                    print("DNI: " + pasajero.getDNI())

                input("\n Presione una tecla para continuar...")
                temp_bool2 = False
            elif op not in range(2):
                print("\n El numero ingresado no es una opcion seleccionable, por favor, vuelva a ingresar \n")

    elif opcion == 2:

        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = int(input("Que vuelo desea seleccionar?: ")) - 1
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        men_pasaj = Sistema.pasajeroJovenVuelo(int(nro_vuelo))

        os.system("clear")
        print("\n Nombre: " + men_pasaj.getNombre())
        print("Apellido: " + men_pasaj.getApellido())
        print("Fecha nacimiento: " + str(men_pasaj.getFechaNac()))
        print("DNI: " + men_pasaj.getDNI())

        input("\n Presione una tecla para continuar...")
    elif opcion == 3:

        vuelos_incompletos = Sistema.tripulacionMinima()
        os.system("clear")
        for vuelo in vuelos_incompletos:
            print("Avion del vuelo incompleto: " + vuelo.getAvion().getModelo())

        input("\n Presione una tecla para continuar...")

    elif opcion == 4:

        vuelos_corruptos = Sistema.tripulantesNoAutorizados()
        os.system("clear")
        for vuelo in vuelos_corruptos:
            print("Avion del vuelo con personal no autorizado: " + vuelo.getAvion().getModelo())

        input("\n Presione una tecla para continuar...")

    elif opcion == 5:

        tripulantes_corruptos = Sistema.tripRuleBreaker()
        os.system("clear")
        for tripulante in tripulantes_corruptos:
            print("\nNombre: " + tripulante.getNombre())
            print("Apellido " + tripulante.getApellido())
            print("DNI: " + tripulante.getDNI() + "\n")

        input("\n Presione una tecla para continuar...")

    elif opcion == 6:
        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = int(input("Que vuelo desea seleccionar?: ")) - 1
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        pasajeros_especiales = Sistema.mostrarVIPyNecesidadesEspeciales(nro_vuelo)

        os.system("clear")
        for pasajero in pasajeros_especiales:
            if pasajero.getVIP() == "Tiene":
                print("Nombre: " + pasajero.getNombre())
                print("Apellido: " + pasajero.getApellido())
                print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                print("DNI: " + pasajero.getDNI())
                print("VIP: " + pasajero.getVIP())
                print("Solicitudes Especiales: " + pasajero.getNecesidadesEspeciales() + "\n")

            elif pasajero.getVIP() == "No tiene" and pasajero.getNecesidadesEspeciales() != "Tiene":
                print("Nombre: " + pasajero.getNombre())
                print("Apellido: " + pasajero.getApellido())
                print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                print("DNI: " + pasajero.getDNI())
                print("VIP: " + pasajero.getVIP())
                print("Solicitudes Especiales: " + pasajero.getNecesidadesEspeciales() + "\n")

        input("\n Presione una tecla para continuar...")

    elif opcion == 7:
        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = int(input("Que vuelo desea seleccionar?: ")) - 1
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        lista_servicio_vuelo = Sistema.idiomasServicio(nro_vuelo)

        os.system("clear")
        for servicio in lista_servicio_vuelo:
            print("\n Nombre: " + servicio.getNombre())
            print("Apellido: " + servicio.getApellido())
            print("Fecha nacimiento: " + str(servicio.getFechaNac()))
            print("DNI: " + servicio.getDNI())

            print("Lenguajes: ")
            for lenguaje in servicio.getIdiomas():
                print("-" + lenguaje)
            print("\n")

        input("\n Presione una tecla para continuar...")

    elif opcion == 8:
        os.system("clear")
        print("\n Cerrando programa... \n")
        bool = False

        input("\n Presione una tecla para continuar...")


    elif opcion not in range(8) or opcion == 0:
        print("\n El numero que ingreso es incorrecto, por favor vuelva a ingresar otra vez. \n")
        input("\n Presione una tecla para continuar...")


