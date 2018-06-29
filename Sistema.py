# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# CARGA DE LAS LISTAS
import carga_json

carga_json.load_planes()

lista_aviones = carga_json.plane_list


carga_json.load_passengers()
carga_json.load_pilots(lista_aviones)
carga_json.load_service(lista_aviones)

lista_pasajeros = carga_json.passenger_list
lista_pilotos = carga_json.pilot_list
lista_servicio = carga_json.service_list

lista_tripulacion = lista_servicio + lista_pilotos


carga_json.load_flies(lista_tripulacion, lista_pasajeros)

lista_vuelos = carga_json.fly_list
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from Servicio import Servicio

def mostrarPasajerosVuelos():
    lista_pasajeros_vuelos = []
    for vuelo in lista_vuelos:
        for pasajero in vuelo.getListaPasajeros():
            lista_pasajeros_vuelos.append(pasajero)

    return lista_pasajeros_vuelos

def mostrarPasajerosVuelo(nro_vuelo):
    temp_lista_pasaj = []
    lista_dni_pas = lista_vuelos[nro_vuelo].getListaPasajeros()

    for pasajero in lista_dni_pas:
        temp_lista_pasaj.append(pasajero)

    return temp_lista_pasaj


def pasajeroJovenVuelo(nro_vuelo):
    lista_pasajeros_vuelo = lista_vuelos[nro_vuelo].getListaPasajeros()
    men_pasaj = None

    for pasajero in lista_pasajeros_vuelo:
        if men_pasaj == None:
            men_pasaj = pasajero
        elif pasajero.getFechaNac() > men_pasaj.getFechaNac():
            men_pasaj = pasajero

    return men_pasaj

def tripulacionMinima():
    lista_vuelos_trip_min = []
    for vuelo in lista_vuelos:
        tripulacion_vuelo = len(vuelo.getListaTripulacion())
        tripulacion_minima = vuelo.getAvion().getCantidadTripulacionMinima()

        if tripulacion_vuelo < tripulacion_minima and vuelo not in lista_vuelos_trip_min:
            lista_vuelos_trip_min.append(vuelo)

    return lista_vuelos_trip_min

def tripulantesNoAutorizados():
    lista_vuelos_corruptos = []
    for vuelo in lista_vuelos:
        for trip in vuelo.getListaTripulacion():
            modelo_avion = vuelo.getAvion()
            aviones_habilitados = trip.getAviones()

            if modelo_avion not in aviones_habilitados and vuelo not in lista_vuelos_corruptos:
                lista_vuelos_corruptos.append(vuelo)

    return lista_vuelos_corruptos

def tripRuleBreaker():
    lista_trip_corruptos = []

    for vuelo in lista_vuelos:
        for vuelo2 in lista_vuelos:
            if not vuelo == vuelo2:
                if vuelo.getFechaSalida() == vuelo2.getFechaSalida():
                    for trip in vuelo.getListaTripulacion():
                        if trip in vuelo2.getListaTripulacion() and trip not in lista_trip_corruptos:
                            lista_trip_corruptos.append(trip)


    return lista_trip_corruptos

def mostrarVIPyNecesidadesEspeciales(nro_vuelo):
    lista_pasajeros_vuelo = lista_vuelos[nro_vuelo].getListaPasajeros()
    pasajeros_especiales = []

    for pasajero in lista_pasajeros_vuelo:
        if pasajero.getVIP() == "Tiene":
            pasajeros_especiales.append(pasajero)
        elif pasajero.getNecesidadesEspeciales() != "No tiene":
            pasajeros_especiales.append(pasajero)

    return pasajeros_especiales

def idiomasServicio(nro_vuelo):
    lista_tripulacion_vuelo = lista_vuelos[nro_vuelo].getListaTripulacion()
    lista_servicio_vuelo = []

    print(lista_tripulacion_vuelo)
    for servicio in lista_tripulacion_vuelo:
        if type(servicio) is Servicio:
            lista_servicio_vuelo.append(servicio)

    return lista_servicio_vuelo