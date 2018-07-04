from TPº1 import carga_json

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

print(lista_pasajeros)