# //////////////////////////////////////////////
# /// ARCHIVO EXCLUSIVO PARA CARGAR EL JSON ///
# ////////////////////////////////////////////

from TPº1.Pasajero import Pasajero
from TPº1.Piloto import Piloto
from TPº1.Servicio import Servicio
from TPº1.Avion import Avion
from TPº1.Vuelo import Vuelo

import json

f = open("datos.json", "r")

d = json.loads(f.read())

passenger_list = []
pilot_list = []
service_list = []
tripulant_list = pilot_list + service_list

fly_list = []
plane_list = []

def load_passengers():
    for person in d["Personas"]:
       if person["tipo"] == "Pasajero":
           temp_pass = Pasajero()

           temp_pass.setNombre(person["nombre"])
           temp_pass.setApellido(person["apellido"])

           birthdate = str.split(str(person["fechaNacimiento"]), "-", 2)
           temp_pass.setFechaNac(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))

           temp_pass.setDNI(person["dni"])

           if person["vip"] == 1:
               temp_pass.setVIP("Tiene")

           else:
               temp_pass.setVIP("No tiene")

           if "solicitudesEspeciales" in person:
               temp_pass.setNecesidadesEspeciales(person["solicitudesEspeciales"])

           else:
               temp_pass.setNecesidadesEspeciales("No tiene")

           passenger_list.append(temp_pass)

def load_pilots(lista_aviones):
    for person in d["Personas"]:
        if person["tipo"] == "Piloto":
            temp_pilot = Piloto()

            temp_pilot.setNombre(person["nombre"])
            temp_pilot.setApellido(person["apellido"])

            birthdate = str.split(str(person["fechaNacimiento"]), "-", 2)
            temp_pilot.setFechaNac(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))

            temp_pilot.setDNI(person["dni"])

            for model in person["avionesHabilitados"]:
                for plane in lista_aviones:
                    if plane.getModelo() == model:
                        temp_pilot.setAviones(plane)

            pilot_list.append(temp_pilot)

def load_service(lista_aviones):
    for person in d["Personas"]:
        if person["tipo"] == "Servicio":
            temp_serv = Servicio()

            temp_serv.setNombre(person["nombre"])
            temp_serv.setApellido(person["apellido"])

            birthdate = str.split(str(person["fechaNacimiento"]), "-", 2)
            temp_serv.setFechaNac(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))

            temp_serv.setDNI(person["dni"])

            for model in person["avionesHabilitados"]:
                for plane in lista_aviones:
                    if plane.getModelo() == model:
                        temp_serv.setAviones(plane)

            for language in person["idiomas"]:
                temp_serv.setIdiomas(language)

            service_list.append(temp_serv)

def load_planes():
    for plane in d["Aviones"]:
        temp_avion = Avion()

        temp_avion.setModelo(plane["codigoUnico"])
        temp_avion.setCantidadPersonas(plane["cantidadDePasajerosMaxima"])
        temp_avion.setCantidadTripulacionMinima(plane["cantidadDeTripulacionNecesaria"])

        plane_list.append(temp_avion)

def load_flies(lista_tripulacion, lista_pasajeros):
    for fly in d["Vuelos"]:
        temp_vuelo = Vuelo()

        for plane in plane_list:
            if plane.getModelo() == fly["avion"]:
                temp_vuelo.setAvion(plane)

        date = str.split(str(fly["fecha"]), "-", 2)
        temp_vuelo.setFechaSalida(int(date[0]), int(date[1]) ,int(date[2]))

        time = str.split(str(fly["hora"]), ":", 1)
        temp_vuelo.setHoraSalida(int(time[0]), int(time[1]))

        temp_vuelo.setOrigen(fly["origen"])

        temp_vuelo.setDestino(fly["destino"])

        for tripulant in lista_tripulacion:
            for dni in fly["tripulacion"]:
                if tripulant.getDNI() == dni:
                    temp_vuelo.setListaTripulacion(tripulant)

        for passenger in lista_pasajeros:
            for dni in fly["pasajeros"]:
                if passenger.getDNI() == dni:
                    temp_vuelo.setListaPasajeros(passenger)

        fly_list.append(temp_vuelo)