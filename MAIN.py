import Sistema
import os
bool = True

while bool:
    os.system("cls")
    print("Ejercicios disponibles: 1, 2, 3, 4, 5, 6, 7")
    print("Para salir ingrese 8")
    opcion = input("Que ejercicio desea realizar?: ")

    if opcion == 1:
        temp_bool = True

        print("Opciones: 1, 2")
        op = input("Desea ver los de un vuelo solo?  1. Si  2. No \n")

        if op == 1:

            while temp_bool:
                os.system("cls")
                print("Vuelos disponibles: 1, 2, 3, 4")
                nro_vuelo = (input("Que vuelo desea seleccionar?: ") - 1)
                if nro_vuelo >= 4:
                    print("\n Vuelva a ingresar el numero de vuelo \n")
                else:
                    temp_bool = False

            pasajeros = Sistema.mostrarPasajerosVuelo(nro_vuelo)

            os.system("cls")
            for pasajero in pasajeros:
                print("\n Nombre: " + pasajero.getNombre())
                print("Apellido: " + pasajero.getApellido())
                print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                print("DNI: " + pasajero.getDNI())

            os.system("pause")

        elif op == 2:
            pasajeros = Sistema.mostrarPasajerosVuelos()

            print(pasajeros)

            os.system("cls")
            for pasajero in pasajeros:
                print("\n Nombre: " + pasajero.getNombre())
                print("Apellido: " + pasajero.getApellido())
                print("Fecha nacimiento: " + str(pasajero.getFechaNac()))
                print("DNI: " + pasajero.getDNI())

            os.system("pause")



    elif opcion == 2:
        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = (input("Que vuelo desea seleccionar?: ") - 1)
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        men_pasaj = Sistema.pasajeroJovenVuelo(nro_vuelo)

        os.system("cls")

        print("Nombre: " + men_pasaj.getNombre())
        print("Apellido: " + men_pasaj.getApellido())
        print("Fecha nacimiento: " + str(men_pasaj.getFechaNac()))
        print("DNI: " + men_pasaj.getDNI())

        os.system("pause")

    elif opcion == 3:
        os.system("cls")

        vuelos_incompletos = Sistema.tripulacionMinima()
        for vuelo in vuelos_incompletos:
            print("Avion del vuelo incompleto: " + vuelo.getAvion().getModelo())

        os.system("pause")

    elif opcion == 4:
        os.system("cls")

        vuelos_corruptos = Sistema.tripulantesNoAutorizados()
        for vuelo in vuelos_corruptos:
            print("Avion del vuelo con personal no autorizado: " + vuelo.getAvion().getModelo())

        os.system("pause")

    elif opcion == 5:
        os.system("cls")

        tripulantes_corruptos = Sistema.tripRuleBreaker()
        for tripulante in tripulantes_corruptos:
            print("\nNombre: " + tripulante.getNombre())
            print("Apellido " + tripulante.getApellido())
            print("DNI: " + tripulante.getDNI() + "\n")

        os.system("pause")

    elif opcion == 6:
        os.system("cls")
        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = (input("Que vuelo desea seleccionar?: ") - 1)
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        pasajeros_especiales = Sistema.mostrarVIPyNecesidadesEspeciales(nro_vuelo)

        os.system("cls")

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

        os.system("pause")

    elif opcion == 7:
        os.system("cls")
        temp_bool = True
        while temp_bool:
            print("\n Vuelos disponibles: 1, 2, 3, 4")
            nro_vuelo = (input("Que vuelo desea seleccionar?: ") - 1)
            if nro_vuelo >= 4:
                print("\n Vuelva a ingresar el numero de vuelo \n")
            else:
                temp_bool = False

        lista_servicio_vuelo = Sistema.idiomasServicio(nro_vuelo)

        os.system("cls")

        for servicio in lista_servicio_vuelo:
            print("\n Nombre: " + servicio.getNombre())
            print("Apellido: " + servicio.getApellido())
            print("Fecha nacimiento: " + str(servicio.getFechaNac()))
            print("DNI: " + servicio.getDNI())

            print("Lenguajes: ")
            for lenguaje in servicio.getIdiomas():
                print("-" + lenguaje)
            print("\n")

        os.system("pause")

    elif opcion == 8:
        os.system("cls")
        print("\n Cerrando programa... \n")
        bool = False

        os.system("pause")

    elif opcion not in range(8):
        print("\n El numero que ingreso es incorrecto, por favor vuelva a ingresar otra vez. \n")


